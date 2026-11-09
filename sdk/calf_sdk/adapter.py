"""Public provider/check wire-format helpers, not a second execution engine."""
from __future__ import annotations
from dataclasses import dataclass, field
import copy
import json
import os
from pathlib import Path
import re
import sys
from typing import Any


def _argv(value: list[str]) -> list[str]:
    if not isinstance(value, list) or not value or len(value) > 32 or not all(isinstance(x, str) and "\0" not in x and len(x.encode()) < 4096 for x in value):
        raise ValueError("Expected an executable-and-arguments array")
    if not Path(value[0]).is_absolute():
        raise ValueError("Use an absolute executable path")
    return list(value)


@dataclass
class Check:
    id: str
    command: list[str]
    inputs: list[str]
    env_keys: list[str] = field(default_factory=list)
    resource_class: str = "light"
    profile: dict | None = None

    @classmethod
    def from_discovered(cls, value: dict) -> "Check":
        """Retain the native profile and exact command; do not rebuild either."""
        if not isinstance(value, dict) or set(value) != {"id", "command", "inputs", "envKeys", "class", "profile"}:
            raise ValueError("Expected a native discovered check")
        return cls(value["id"], copy.deepcopy(value["command"]), copy.deepcopy(value["inputs"]),
                   copy.deepcopy(value["envKeys"]), value["class"], copy.deepcopy(value["profile"]))

    def to_dict(self) -> dict:
        if self.resource_class not in ("light", "heavy"):
            raise ValueError("Invalid check resource class")
        result = {"id": self.id, "command": _argv(self.command), "inputs": list(self.inputs),
                  "envKeys": list(self.env_keys), "class": self.resource_class}
        if self.profile is not None:
            if not isinstance(self.profile, dict) or self.profile.get("schema") not in (1, 2, 3):
                raise ValueError("Unsupported Check Profile schema")
            # Strict interpretation and identities belong to the native core.
            result["profile"] = copy.deepcopy(self.profile)
        return result


@dataclass
class ProviderConfig:
    command: list[str]
    checks: list[Check]
    max_attempts: int = 4
    timeout_ms: int = 300000
    resource_class: str = "light"

    def to_dict(self) -> dict:
        if type(self.max_attempts) is not int or not 1 <= self.max_attempts <= 8:
            raise ValueError("Attempt budget must be 1..8")
        if type(self.timeout_ms) is not int or not 100 <= self.timeout_ms <= 300000:
            raise ValueError("Operation timeout must be 100..300000 ms")
        if not 1 <= len(self.checks) <= 16 or self.resource_class not in ("light", "heavy"):
            raise ValueError("Invalid checks/resource class")
        return {"schema": 1, "provider": _argv(self.command), "providerClass": self.resource_class,
                "checks": [c.to_dict() for c in self.checks], "maxAttempts": self.max_attempts,
                "timeoutMs": self.timeout_ms}

    def write_new(self, path: str | os.PathLike) -> None:
        """Create a new configuration only; never overwrite an existing one."""
        raw = json.dumps(self.to_dict(), ensure_ascii=False, allow_nan=False, indent=2).encode()
        if len(raw) > 65536:
            raise ValueError("Provider configuration exceeds 64 KiB")
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)


def read_request(path: str | os.PathLike) -> dict[str, Any]:
    from .client import _json
    with open(path, "rb") as stream:
        raw = stream.read(256 * 1024 + 1)
    if len(raw) > 256 * 1024:
        raise ValueError("Provider input exceeds 256 KiB")
    value = _json(raw)
    if value.get("schema") != 1 or value.get("phase") not in ("plan", "repair", "review"):
        raise ValueError("Unsupported provider protocol")
    if not isinstance(value.get("requestHash"), str) or not re.fullmatch(r"[0-9a-f]{64}", value["requestHash"]):
        raise ValueError("Missing request identity")
    return value


def action(path: str, content: str, expected_sha: str | None) -> dict:
    """None means create-only. A hash means replace exactly that file version."""
    if expected_sha is not None and not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
        raise ValueError("Expected a SHA-256 digest or None for create-only")
    if len(content.encode("utf-8")) > 32768:
        raise ValueError("Proposed file content exceeds 32 KiB")
    return {"path": path, "content": content, "expectedSha": expected_sha}


def plan(request: dict, *, scope: list[str], requirements: list[dict], actions: list[dict]) -> dict:
    if request.get("phase") not in ("plan", "repair"):
        raise ValueError("Plans are accepted only during plan/repair")
    return {"requestHash": request["requestHash"], "scope": scope,
            "requirements": requirements, "actions": actions}


def review(request: dict, verdict: str, reason: str) -> dict:
    if request.get("phase") != "review" or verdict not in ("pass", "fail", "unknown"):
        raise ValueError("Review phase and an explicit verdict are required")
    return {"requestHash": request["requestHash"], "verdict": verdict, "reason": reason}


def emit(response: dict) -> None:
    raw = json.dumps(response, ensure_ascii=False, allow_nan=False).encode("utf-8")
    if len(raw) > 128 * 1024:
        raise ValueError("Provider response exceeds 128 KiB")
    sys.stdout.buffer.write(raw + b"\n")
    sys.stdout.buffer.flush()
