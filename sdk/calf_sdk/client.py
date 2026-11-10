"""One-shot calls to the released CALF executable; never edit its records directly."""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import tempfile
import time
from typing import Any


class CalfError(RuntimeError):
    def __init__(self, message: str, *, response: dict | None = None, returncode: int | None = None):
        super().__init__(message)
        self.response = response
        self.returncode = returncode


class CalfTransportError(CalfError):
    """No reliable response. A mutation may have happened; inspect before retrying."""


def _path(value: str | os.PathLike) -> Path:
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts or "\0" in str(path):
        raise ValueError("An absolute path without parent traversal is required")
    return path


def _json(raw: bytes) -> dict[str, Any]:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    def invalid_constant(value):
        raise ValueError("non-finite JSON number")
    result = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=invalid_constant)
    if not isinstance(result, dict):
        raise ValueError("CALF response must be a JSON object")
    return result


def is_satisfied(response: dict[str, Any]) -> bool:
    """Only an explicit current verdict qualifies. Process exit 0 does not."""
    return response.get("outcome") == "SATISFIED"


class CalfClient:
    """Uses an explicitly selected native executable and records home.

    No daemon, model, key storage, automatic retry, direct journal write or
    automatic worker launch. OS/host permissions and CALF guards still apply.
    """
    def __init__(self, executable: str | os.PathLike, home: str | os.PathLike, *,
                 timeout: float = 30, max_response_bytes: int = 8 * 1024 * 1024):
        self.executable = _path(executable)
        self.home = _path(home)
        if not self.executable.is_file():
            raise ValueError("CALF executable does not exist")
        if os.name == "nt" and self.executable.suffix.lower() != ".exe":
            raise ValueError("Select the native calf.exe, not a shell script")
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be positive and finite")
        if type(max_response_bytes) is not int or not 1024 <= max_response_bytes <= 32 * 1024 * 1024:
            raise ValueError("response limit must be between 1 KiB and 32 MiB")
        self.timeout = timeout
        self.max_response_bytes = max_response_bytes

    def _invoke(self, arguments: list[str], payload: dict | None = None) -> dict[str, Any]:
        encoded = b"" if payload is None else json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8")
        if len(encoded) > 65536:
            raise ValueError("CALF JSON input exceeds 64 KiB")
        # Spool output to temporary files instead of accumulating unbounded PIPE
        # buffers. Read into memory only after checking the byte limits.
        with tempfile.TemporaryFile() as source, tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
            source.write(encoded)
            source.seek(0)
            try:
                process = subprocess.Popen([str(self.executable), *arguments], stdin=source,
                                           stdout=output, stderr=errors, shell=False)
            except OSError as exc:
                raise CalfTransportError("Could not launch the selected CALF executable") from exc
            try:
                deadline = time.monotonic() + self.timeout
                while True:
                    if os.fstat(output.fileno()).st_size > self.max_response_bytes or os.fstat(errors.fileno()).st_size > 65536:
                        raise CalfTransportError("CALF output limit exceeded; inspect state before retrying")
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise CalfTransportError("CALF response timed out; task completion is unknown")
                    try:
                        process.wait(timeout=min(remaining, 0.1))
                        break
                    except subprocess.TimeoutExpired:
                        pass
                output.seek(0)
                raw = output.read(self.max_response_bytes + 1)
                if len(raw) > self.max_response_bytes or os.fstat(errors.fileno()).st_size > 65536:
                    raise CalfTransportError("CALF output limit exceeded; inspect state before retrying")
                try:
                    response = _json(raw)
                except (ValueError, UnicodeError) as exc:
                    raise CalfTransportError("CALF returned an invalid or incomplete JSON response", returncode=process.returncode) from exc
                if process.returncode != 0 or "error" in response:
                    message = response.get("error")
                    raise CalfError(message if isinstance(message, str) else "CALF command failed",
                                    response=response, returncode=process.returncode)
                return response
            finally:
                # A work API can own a running adapter. Windows terminate() is
                # forceful: request native cleanup before the last-resort kill.
                if process.poll() is None:
                    native_cancel = bool(payload and payload.get("op") == "work" and
                                         payload.get("action") in ("step", "recheck") and payload.get("work"))
                    if native_cancel:
                        cancel = {"op":"work", "action":"cancel", "home":str(self.home), "work":payload["work"]}
                        try:
                            subprocess.run([str(self.executable), "api"], input=json.dumps(cancel).encode(),
                                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2, check=False)
                        except (OSError, subprocess.TimeoutExpired):
                            pass
                    else:
                        process.terminate()
                    try:
                        process.wait(timeout=5 if native_cancel else 1)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()

    def version(self) -> dict[str, Any]:
        return self._invoke(["--version"])

    def discover_checks(self, workspace: str | os.PathLike) -> list[dict[str, Any]]:
        """Ask the native core to discover and pin checks, without queuing work.

        Discovery may execute installed Python/Rust metadata probes. It does not
        install dependencies or execute the test suite. Requires 1.8.6 / 1.9.1.
        """
        result = self._invoke(["check-discover", str(_path(workspace))])
        checks = result.get("checks")
        if not isinstance(checks, list) or not checks or not all(isinstance(c, dict) for c in checks):
            raise CalfTransportError("CALF returned an invalid check discovery response")
        return checks

    def binary_sha256(self) -> str:
        digest = hashlib.sha256()
        with self.executable.open("rb") as stream:
            for block in iter(lambda: stream.read(256 * 1024), b""):
                digest.update(block)
        return digest.hexdigest()

    def call(self, op: str, **fields: Any) -> dict[str, Any]:
        if not isinstance(op, str) or not op or {"home", "op"} & fields.keys():
            raise ValueError("operation/home cannot be overridden")
        return self._invoke(["api"], {**fields, "op": op, "home": str(self.home)})

    def tasks(self) -> dict[str, Any]:
        return self.call("list")

    def inspect(self, task: str) -> dict[str, Any]:
        return self.call("inspect", task=task)

    def registered_tasks(self, workspace: str | os.PathLike) -> dict[str, Any]:
        """List registered history tasks on demand; requires 1.8.10 / 1.9.5."""
        return self._invoke(["rpc"], {"op": "statusTasks", "root": str(_path(workspace)), "args": []})

    def registered_status(self, workspace: str | os.PathLike, task: str) -> dict[str, Any]:
        """Read current completion plus optional historical/context diagnostics.

        The top-level outcome remains authoritative. This does not rerun a
        check, normalize the environment or write a completion decision.
        """
        if not isinstance(task, str) or not task.strip():
            raise ValueError("A registered task id is required")
        return self._invoke(["status", str(_path(workspace)), task])

    def submit(self, workspace: str | os.PathLike, request: str, *, attachments: list[dict] | None = None,
               reuse: dict | None = None) -> dict[str, Any]:
        fields: dict[str, Any] = {"workspace": str(_path(workspace)), "request": request,
                                  "helper": str(self.executable)}
        if attachments is not None:
            fields["attachments"] = attachments
        if reuse is not None:
            fields.update(reuseTask=reuse["sourceTask"], reuseDigest=reuse["digest"])
        return self.call("submit", **fields)

    def control(self, task: str, action: str) -> dict[str, Any]:
        if action not in ("pause", "resume", "cancel", "recheck"):
            raise ValueError("Unsupported control action")
        return self.call(action, task=task)

    def reuse(self, task: str) -> dict[str, Any]:
        return self.call("reuse", task=task)

    def changes(self, task: str, *, mode: str = "task", path: str | None = None,
                attempt: int | None = None) -> dict[str, Any]:
        fields: dict[str, Any] = {"task": task, "mode": mode}
        if path is not None:
            fields["path"] = path
        if attempt is not None:
            fields["attempt"] = attempt
        return self.call("changes", **fields)

    def preferences(self, value: str | None = None) -> dict[str, Any]:
        return self.call("preferences", **({} if value is None else {"value": value}))

    def sources(self, action: str = "list", **fields: Any) -> dict[str, Any]:
        if action not in ("list", "add", "remove", "browse", "read"):
            raise ValueError("Unsupported source action")
        return self.call("sources", action=action, **fields)

    @staticmethod
    def reference(source: str, read_response: dict) -> dict:
        """Construct a version-bound reference; does not send it to an AI."""
        return {"source": source, "uri": read_response["contents"][0]["uri"],
                "sha256": read_response["_meta"]["calf"]["sha256"]}

    def worker_argv(self) -> list[str]:
        """Caller owns the foreground process. Its exit 0 means idle, not PASS."""
        return [str(self.executable), "worker", str(self.home)]

    def mcp_server(self, root: str | os.PathLike) -> dict:
        """Standard stdio launch fields for a compatible MCP client."""
        return {"command": str(self.executable), "args": ["local-mcp", str(_path(root))]}

    def work(self, action: str, **fields: Any) -> dict:
        """Versioned universal work; accepted/requested is not a completion verdict.

        Set client.timeout above the WorkSpec operation timeout plus cleanup when
        using step/recheck. Unknown async work must be queried, not resubmitted.
        """
        if action not in ("register","adapters","submit","list","inspect","step","cancel","retry","recheck","adopt"):
            raise ValueError("Unsupported universal work action")
        return self.call("work", action=action, **fields)

    def work_mcp_server(self, *, control: bool = False) -> dict:
        """Read-only by default; explicit control exposes registered work actions.

        Registration is never an MCP tool. Host permissions are unchanged.
        """
        return {"command": str(self.executable), "args": ["work-mcp",str(self.home)] + (["--control"] if control else [])}

    @staticmethod
    def _tool_policy(policy: str | os.PathLike, policy_sha256: str) -> list[str]:
        if (not isinstance(policy_sha256, str) or len(policy_sha256) != 64 or
                any(c not in "0123456789abcdef" for c in policy_sha256)):
            raise ValueError("The exact lowercase policy SHA-256 is required")
        return [str(_path(policy)), policy_sha256]

    def tool_contract(self, request: dict) -> dict:
        """CPU-only contract/pin evaluation; no downstream tool is launched."""
        if not isinstance(request, dict):
            raise ValueError("A contract request object is required")
        return self._invoke(["tool-contract"], request)

    def tool_status(self, policy: str | os.PathLike, policy_sha256: str) -> dict:
        """Read current native completion; never resubmit an uncertain call."""
        return self._invoke(["tool-call", *self._tool_policy(policy, policy_sha256)], {"action": "status"})

    def prepare_tool(self, policy: str | os.PathLike, policy_sha256: str,
                     request: dict, *, ttl_ms: int = 120000) -> dict:
        """Prepare only. Review returned argv through the existing host flow.

        Requires Harness 1.8.12 / Workbench 1.9.8. This writes local intent
        bookkeeping but does not run or approve the requested tool. A ticket
        is not independent proof of a human approval. No automatic retry.
        """
        if not isinstance(request, dict) or type(ttl_ms) is not int or not 100 <= ttl_ms <= 300000:
            raise ValueError("A request object and a 100–300000ms lifetime are required")
        return self._invoke(["tool-prepare", *self._tool_policy(policy, policy_sha256), str(ttl_ms)], request)

    def tool_mcp_server(self, policy: str | os.PathLike, policy_sha256: str, *, control: bool = False) -> dict:
        """Foreground descriptor. Control adds invoke/prepare, never approval."""
        if type(control) is not bool:
            raise ValueError("control must be boolean")
        return {"command": str(self.executable), "args": ["tool-mcp", *self._tool_policy(policy, policy_sha256)] + (["--control"] if control else [])}
