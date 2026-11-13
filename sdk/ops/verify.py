"""Use released binaries in new isolated folders. Never access an owner's home."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

SDK = Path(__file__).resolve().parents[1]
PYTHON = str(Path(sys.executable).resolve())
sys.path.insert(0, str(SDK))
from calf_sdk import CalfClient, CalfError, Check, ProviderConfig, is_satisfied


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def native(binary, *args, environment=None):
    result = subprocess.run([str(binary), *map(str, args)], capture_output=True, timeout=60,
                            encoding="utf-8", env=environment)
    value = json.loads(result.stdout)
    if result.returncode:
        raise RuntimeError(f"native command failed: {result.returncode}, {value}")
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--harness", type=Path, required=True)
    parser.add_argument("--workbench", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    report = {"status": "FAIL", "platform": sys.platform, "provider": "synthetic; no AI or network call", "checks": []}
    try:
        suite = unittest.defaultTestLoader.discover(str(SDK / "tests"))
        tested = unittest.TextTestRunner(verbosity=2).run(suite)
        assert tested.wasSuccessful() and tested.testsRun > 0
        report["unitTests"] = tested.testsRun
        home = args.output / "records"
        h = CalfClient(args.harness, home)
        w = CalfClient(args.workbench, home)
        assert h.version()["version"] == "1.8.16"
        assert w.version()["version"] == "1.9.12"
        report["binaries"] = {"harness": h.binary_sha256(), "workbench": w.binary_sha256()}
        assert h.tasks()["jobs"] == []
        prefs = h.preferences("한국어 中文 日本語 · keep small")
        assert w.preferences() == prefs
        report["checks"].append("released 1.8.16/1.9.12 share Unicode preferences and task home")

        ws = args.output / "workspace"
        ws.mkdir()
        (ws / "result.py").write_text("VALUE = 'initial'\n")
        (ws / "test_result.py").write_text("import unittest\nfrom result import VALUE\nclass TestValue(unittest.TestCase):\n def test_value(self): self.assertEqual(VALUE, 'expected')\n")
        for name in ("history.html", "contract.json", "settings.json"):
            (ws / name).write_text("Preserve existing data · 한국어 中文 日本語\n", encoding="utf-8")
        preserved = {p.name: sha(p) for p in ws.iterdir() if p.name != "result.py"}
        check_code = "import unittest,sys,os;sys.path.insert(0,os.getcwd());s=unittest.defaultTestLoader.discover('.');r=unittest.TextTestRunner().run(s);sys.exit(0 if r.wasSuccessful() and r.testsRun>0 else 1)"
        config = ProviderConfig([PYTHON, str(SDK / "examples/provider_demo.py")],
                                [Check("unit", [PYTHON, "-I", "-c", check_code], ["test_result.py"])],
                                timeout_ms=10000)
        provider = args.output / "provider.json"
        config.write_new(provider)
        environment = dict(os.environ, PYTHONPATH=str(SDK), PYTHONDONTWRITEBYTECODE="1")
        state = args.output / "adapter-state"
        outcome = native(args.harness, "run", ws, "Return the expected fixture value", provider, state, environment=environment)
        (args.output / "adapter-result.json").write_text(json.dumps(outcome, ensure_ascii=False, indent=2))
        assert is_satisfied(outcome) and outcome["evidence"]["attempt"] == 2, outcome
        status = native(args.workbench, "run-status", ws, state, outcome["task"], environment=environment)
        # run-status adds a diagnostic projection without changing the saved
        # execution result. Compare every execution field and check the fresh
        # observer verdict separately; historical success is not sufficient.
        assert {k: v for k, v in status.items() if k != "statusView"} == outcome
        assert is_satisfied(status)
        assert status["statusView"]["schema"] == 1
        assert status["statusView"]["currentObserver"]["outcome"] == "SATISFIED"
        assert all(sha(ws / n) == digest for n, digest in preserved.items())
        report["checks"].append("SDK provider: real failing test, repair, independent check and review at attempt 2")

        # These APIs only manage new core-owned text in the existing journal.
        created = h.artifacts(ws, operation="create", state=state, task=outcome["task"],
                              requestId="sdk-owned-note", role="temporary", label="SDK verification note",
                              content="Retain original source · 한국어 中文 日本語\n", retentionSeconds=0, confirm=True)
        assert created["state"] == "SEALED" and not created["automaticDeletion"]
        artifact_id = created["artifact"]["artifactId"]
        plan = w.artifacts(ws, operation="plan", state=state)
        row = next(v for v in plan["artifacts"] if v["managed"] and v["managed"]["artifactId"] == artifact_id)
        assert row["suggestion"] == "KEEP" and "MANAGED_ACTIVE_REFERENCE" in row["retentionReasons"]
        released = h.artifacts(ws, operation="release", state=state, task=outcome["task"],
                               artifactId=artifact_id, confirm=True)
        assert released["artifact"]["activeReferences"] == []
        scope = {"domain": "state", "path": created["path"]}
        preview = w.artifacts(ws, operation="prepare", state=state, **scope)
        move = dict(scope, operationId=preview["plan"]["operationId"], digest=preview["digest"], confirm=True)
        assert h.artifacts(ws, operation="quarantine", state=state, **move)["state"] == "QUARANTINED"
        assert w.artifacts(ws, operation="restore", state=state, **move)["state"] == "RESTORED"
        assert all(sha(ws / n) == digest for n, digest in preserved.items())
        report["checks"].append("managed text: creation receipt, active-reference protection, explicit release, quarantine and restore")
        (ws / "result.py").write_text("VALUE = 'expected'\n# externally edited\n")
        stale = native(args.workbench, "run-status", ws, state, outcome["task"], environment=environment)
        assert stale["state"] == "evidence_stale" and not is_satisfied(stale), stale
        report["checks"].append("external file edit invalidates prior success")

        discovered = h.discover_checks(ws)
        profiled = Check.from_discovered(discovered[0])
        assert profiled.profile["schema"] == 2 and profiled.profile["kind"] == "unittest"
        profile_config = ProviderConfig([PYTHON, str(SDK / "examples/provider_demo.py")],
                                        [profiled], timeout_ms=10000)
        profile_file = args.output / "profile-provider.json"
        profile_config.write_new(profile_file)
        # Demo provider names the registered criterion, as the actual wire
        # contract requires; no relaxation of the discovered check is allowed.
        (ws / "result.py").write_text("VALUE = 'initial'\n")
        profile_result = native(args.harness, "run", ws, "Profile fixture", profile_file,
                                args.output / "profile-state", environment=environment)
        assert is_satisfied(profile_result) and profile_result["evidence"]["attempt"] == 2, profile_result
        assert profile_result["evidence"]["checks"][0]["verification"]["effective"] == 1
        assert all(sha(ws / n) == digest for n, digest in preserved.items())
        report["checks"].append("native Python v2 discovery roundtrip and actual profiled fail/repair/check")

        # Register a deliberately unavailable connection, but never execute it.
        h.call("connection", connection={"kind": "codex", "helper": str(args.harness), "executable": str(args.output / "missing-codex"), "model": "", "account": "sdk-fixture"})
        job = h.submit(ws, "Queued fixture · 한국어 中文 日本語")
        assert w.tasks()["jobs"][0]["task"] == job["task"]
        assert h.control(job["task"], "pause")["requested"]
        native(args.harness, *h.worker_argv()[1:])
        assert w.tasks()["jobs"][0]["view"]["state"] == "paused"
        assert h.control(job["task"], "resume")["requested"]
        assert h.control(job["task"], "cancel")["requested"]
        native(args.harness, *h.worker_argv()[1:])
        assert not is_satisfied(w.inspect(job["task"]))
        try:
            h.control(job["task"], "resume")
        except CalfError as exc:
            assert "cancelled_job_is_final" in str(exc)
        else:
            raise AssertionError("cancelled job resumed")
        assert h.changes(job["task"])["readOnly"]
        recipe = h.reuse(job["task"])
        assert recipe["sourceTask"] == job["task"] and len(recipe["digest"]) == 64
        report["checks"].append("submit/shared list/pause/resume/cancel/inspect/diff/reuse; no provider launched")

        source = args.output / "참고자료"
        source.mkdir()
        document = source / "메모.txt"
        document.write_text("한국어 中文 日本語 reference", encoding="utf-8")
        (source / ".env").write_text("SYNTHETIC_ONLY=true")
        entry = h.sources("add", root=str(source))["sources"][0]
        listing = w.sources("browse", source=entry["id"])
        assert listing["connection"]["closed"] is True
        assert [r["name"] for r in listing["resources"]] == ["메모.txt"]
        uri = listing["resources"][0]["uri"]
        read = h.sources("read", source=entry["id"], uri=uri)
        assert read["contents"][0]["text"] == document.read_text(encoding="utf-8")
        reference = h.reference(entry["id"], read)
        count = len(h.tasks()["jobs"])
        document.write_text("changed after preview", encoding="utf-8")
        try:
            h.submit(ws, "Do not submit changed reference", attachments=[reference])
        except CalfError as exc:
            assert "local_context_changed" in str(exc)
        else:
            raise AssertionError("stale attachment was accepted")
        assert len(h.tasks()["jobs"]) == count

        # A complete MCP session using the generated stdio launch fields.
        launch = h.mcp_server(source)
        messages = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25", "capabilities": {}, "clientInfo": {"name": "sdk-test", "version": "0.2.0"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "resources/list", "params": {}},
            {"jsonrpc": "2.0", "id": 3, "method": "resources/read", "params": {"uri": uri}},
        ]
        process = subprocess.run([launch["command"], *launch["args"]], input="".join(json.dumps(m) + "\n" for m in messages), capture_output=True, encoding="utf-8", timeout=10)
        replies = [json.loads(line) for line in process.stdout.splitlines()]
        assert process.returncode == 0 and [v["id"] for v in replies] == [1, 2, 3]
        assert all("result" in v and "error" not in v for v in replies)
        assert replies[2]["result"]["contents"][0]["text"] == "changed after preview"
        assert h.sources("remove", source=entry["id"])["sources"] == []
        assert all(sha(ws / n) == digest for n, digest in preserved.items())
        report["checks"].append("Local MCP CJK list/read/EOF shutdown; hidden files omitted; stale attachment refused before queue write")
        report.update(status="PASS", protectedFiles=len(preserved), adapterTask=outcome["task"], queueTask=job["task"])
    except BaseException as exc:
        report["failure"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        (args.output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
