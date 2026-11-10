# CALF SDK 0.2.6 — Developer Preview

Universal Work v1 adds frozen contracts, checks tied to the exact output files, runtime adapters, dependency-free Node/Python clients and optional-control Local MCP. [Protocol and runnable examples](docs/WORK_PROTOCOL.md). Workbench 1.9.2 shows the same work under **Runtime Work**. Existing code-job API calls remain compatible.


[한국어](README_KR.md) · [Protocol](docs/PROTOCOL.md) · [Extension license](LICENSE-SDK.txt)

A small integration layer for **CALF Harness 1.8.7–1.8.13** and the native core included in **CALF Workbench 1.9.2–1.9.9**. Python 3.10+ and the standard library are sufficient. The SDK adds no background service, model runtime, database or network dependency. CALF's execution engine remains proprietary and is not included.

Qualification details for the native cores and SDK are in `VERIFICATION.json` in the archive. Runtime tests use real Python/Node processes and a loopback HTTP service; no new live AI-service benchmark is claimed.

[Download SDK 0.2.6](https://github.com/VibePakcr/CALF/releases/tag/sdk-v0.2.6). One portable source archive includes this SDK, English/Korean guides, both protocol documents, examples and the test runner. Install a matching CALF native release separately; the SDK archive contains no core runtime.

## Start with existing records

Extract this SDK and run your integration from its root, or add the extracted root to your Python import path. Select the installed native `calf` / `calf.exe` and **the same records home used by CALF**. The SDK deliberately does not guess or migrate it. Run `calf task home` in your normal CALF environment to see that location. For a first experiment, use a new absolute folder instead.

```python
from pathlib import Path
from calf_sdk import CalfClient, is_satisfied

client = CalfClient(
    Path("/absolute/path/to/calf"),
    Path("/absolute/path/to/CALF/workbench"),
)
print(client.version())
for job in client.tasks()["jobs"]:
    print(job["task"], job["view"]["state"])
    current = client.inspect(job["task"])
    print("Verified now:", is_satisfied(current))
```

On Windows use absolute paths such as `Path(r"C:\Tools\CALF\calf.exe")`. Select the native core, not a shell script, GUI launcher or `.app` directory. Keep executable and workspace paths on storage available throughout the operation. Provider/check executables should use their physical paths, e.g. `Path(sys.executable).resolve()`.

The archive can also be installed locally with `python -m pip install --no-build-isolation .` when setuptools is already available. It has no third-party runtime dependencies. This SDK is not published to PyPI.

## Submit and control work

Configure a working AI connection through CALF first. The convenience queue discovers supported Python `unittest`, configured `pytest`, and bounded Cargo integration-test profiles. A folder without supported tests is refused; it does not become an unchecked task.

```python
job = client.submit(Path("/absolute/project"), "Fix the invoice rounding bug")
task = job["task"]
print(client.control(task, "pause"))
print(client.control(task, "resume"))
```

Submission queues a task. It does **not** start an AI process. Use the Workbench's existing worker, or deliberately run the foreground worker:

```python
import subprocess
subprocess.run(client.worker_argv(), check=True)  # may perform queued work
result = client.inspect(task)                    # fetch current evidence
print(is_satisfied(result))
```

The caller owns that foreground process and should allow CALF's pause/cancel handling to finish. Worker exit zero means the worker returned normally, not that every task succeeded. `control(task, "cancel")` requests cancellation; it is not a completion receipt. A cancelled task cannot resume. `recheck` uses the existing budget and guard rules.

`tasks()` returns the most recent 32 tasks. `changes(task, mode="task")` exposes the existing read-only projection; supported modes are `task`, `attempt` and `recovery`. Use `path` to load one file and `attempt` to select an attempt. Missing historical text stays missing. Working-tree Git diff is a separate Workbench feature, not an SDK `changes` mode.

`reuse(task)` obtains a recipe; passing it to `submit(..., reuse=recipe)` creates a new task. A recipe is not evidence of success and its digest must still match. `preferences(text)` appends a working-style preference through CALF; an empty string clears that preference's current value. Calling `preferences()` without an argument reads the current value.

## Local Sources and MCP

```python
root = "/absolute/reference-folder"
registry = client.sources("add", root=root)
source = next(s for s in registry["sources"] if s["root"] == root)
listing = client.sources("browse", source=source["id"])
uri = listing["resources"][0]["uri"]
preview = client.sources("read", source=source["id"], uri=uri)
reference = client.reference(source["id"], preview)
# Only this explicit submission attaches the selected content to a new task:
job = client.submit(Path("/absolute/project"), "Use the attached requirements",
                    attachments=[reference])
```

Adding, browsing or previewing a folder does not send it to an AI. If the file changes after preview, CALF refuses the stale reference. Up to four references and 8 KiB of serialized context can be attached. Hidden, credential-related and linked paths are excluded by the native folder adapter. These rules control context submission; they do not sandbox an external provider's existing filesystem permissions.

`client.mcp_server(Path("/absolute/reference-folder"))` returns `command` and `args` for an MCP client to launch CALF's read-only stdio resource server. It supports initialization, `resources/list` and `resources/read`; it is not an arbitrary MCP tool/plugin host. Close stdin and wait for process exit after use. See [the protocol](docs/PROTOCOL.md).

## Provider and check adapters

`Check` and `ProviderConfig` create the existing native JSON configuration. `read_request`, `plan`, `action`, `review` and `emit` help a provider implement that protocol. Providers propose actions; the native core checks identities, protects registered tests, applies allowed changes, executes checks and produces the verdict. An extension cannot mark a task complete by returning exit zero.

```python
import sys
from calf_sdk import Check, ProviderConfig

python = str(Path(sys.executable).resolve())
config = ProviderConfig(
    command=[python, "/absolute/path/to/my_adapter.py"],
    checks=[Check("unit", [python, "-m", "unittest"], ["test_invoice.py"])],
    max_attempts=4,
)
config.write_new("/absolute/path/to/new-provider.json")
```

Use a check that fails for empty, skipped or incomplete verification as appropriate to your contract. A generic exit-code check cannot infer whether your test command was meaningful. `write_new` refuses to overwrite existing configuration.

Run custom adapters with the native foreground interface:

```text
calf run WORKSPACE REQUEST PROVIDER.json STATE
calf run-status WORKSPACE STATE TASK
```

This explicit-state adapter path is separate from the Workbench queue; it is **not automatically imported into the Workbench task list**. Use `client.submit` for shared Workbench jobs. A provider receives one JSON request-file path appended to its arguments and returns one JSON object on stdout. Diagnostic text belongs on stderr. `examples/provider_demo.py` is a deterministic fixture that intentionally fails once, repairs and reviews; it makes no AI call. Keep this SDK importable by the provider process.

## Failure semantics and limits

- `CalfError`: native command reported a failure; its structured response is available as `error.response`.
- `CalfTransportError`: timeout, output limit, launch or parsing failure. The operation's effect is unknown. **Inspect before retrying; mutations are never retried automatically.**
- `is_satisfied` recognizes only an explicit `outcome == "SATISFIED"` in the response supplied to it. It does not validate arbitrary data, verify signatures or refresh a saved response. Use a fresh `inspect`/`run-status` response from the selected trusted binary.
- API input is limited to 64 KiB. The client defaults to 30 seconds and 8 MiB response data; stdout/stderr are spooled to temporary files and read into memory only within bounds. A producer can transiently exceed the disk limit between polling intervals. Nothing is cached between calls.
- Even lookup operations may let CALF create its own directories or rebuild indexes. The SDK never directly rewrites journals, contracts or settings.
- The SDK is not an OS sandbox. Provider/check programs retain host permissions. Execute only trusted adapters. It does not change approval policy, install models or manage credentials.

## Verify the preview

From this SDK root:

```text
python -m unittest discover -s tests -v
python ops/verify.py --harness /absolute/calf-1.8.11 --workbench /absolute/calf-1.9.6 --output /absolute/new-test-folder
```

The integration check uses fresh state, synthetic providers and actual Python tests. It verifies a failed check followed by repair, stale evidence after an external edit, shared records, control operations, CJK text, MCP shutdown and refusal of stale attachments. It does not call an AI service, touch your existing CALF home or perform a memory benchmark. The output folder must not already exist; failed reports are retained.

## Check Profiles and updates (0.2.2)

Requires Harness 1.8.7 or Workbench 1.9.2 for native check discovery. Existing 0.1 APIs remain available.

```python
from calf_sdk import Check, ProviderConfig
checks = [Check.from_discovered(c) for c in client.discover_checks(project)]
# Preserve these definitions exactly when constructing a custom provider config.
config = ProviderConfig(command=[python, adapter_path], checks=checks)
```

`discover_checks` probes installed tool metadata; it does not run tests, install dependencies or queue a task. Python profiles select `.venv`, `venv`, an activated environment, then PATH. An explicit unavailable environment is refused. Python v2 binds interpreter, environment configuration and package metadata; it does not hash every installed package file. Cargo supports one locked package's integration tests, not general workspaces or doctest certification.

The native core records baseline failures, distinguishes existing/new/resolved failures and stops repeated unsuccessful checks with unchanged files and results. Empty, skipped-only or incomplete checks never imply completion. Do not turn `no_progress`, `UNKNOWN` or a request acknowledgment into a successful result.

New queued jobs retain one shared executable per version in the selected records home. Keep that complete home when updating; `control(task, "resume")` followed by the foreground worker uses the original runtime and remaining attempt budget. Missing/changed runtimes are refused. `runtime_unavailable` is not a provider failure. Old contracts are not rewritten. The advanced `calf run` path still uses its explicitly pinned binary/config/state and is not automatically moved into the queue.


### JavaScript / TypeScript

CALF 1.8.7 / 1.9.2 supports Node 24+ built-in node:test profiles. `Check.from_discovered()` retains profile v3 and its command. See `examples/check_profiles.py`. npm scripts, Jest, Vitest and TypeScript typechecking are outside this profile.


## Saved results and current status

With Harness 1.8.10 / Workbench 1.9.5, use `client.registered_tasks(workspace)` to list registered tasks and `client.registered_status(workspace, task)` to read the current verdict and diagnostic `statusView`. `is_satisfied(response)` checks only the current top-level outcome. Historical `SATISFIED` is not current completion. These calls do not run checks or AI, or change environment variables. [Example](examples/status_context.py) · [Guide](docs/STATUS_CONTEXT.md).

## Claude connection kit (0.2.4)

`hosts/` now includes the nine-hook macOS Claude Code adapter and its install/update/recovery tool, with support for cores 1.8.11 and 1.9.6. `PostToolBatch` resolves matched denied non-check calls; registered checks still require real native receipts. Existing Python/Node APIs and MCP protocols remain unchanged. [Installation](hosts/README.md) · [Approval, status and limits](hosts/claude/README.md). Windows/Linux core and SDK support does not establish Claude host installation support.

## MCP tool policies (0.2.6)

The new MCP path requires Harness **1.8.12** or Workbench **1.9.8**. Python's `tool_contract` normalizes contracts, `tool_status` reads current native completion, and `prepare_tool` creates a reviewable intent only. It neither executes nor approves the tool. Review the returned `argv` and run it through the host's existing permission flow. A ticket is not independent proof that a human clicked an approval button.

```python
prepared = client.prepare_tool(policy_path, exact_policy_sha256, request)
assert prepared["state"] == "REQUIRE_APPROVAL"
assert prepared["authorityGranted"] is False
print(prepared["review"])
print(prepared["argv"])
```

Python's `tool_mcp_server` and Node's `toolMcpServer` return the same foreground stdio descriptor. Status is the only default tool. Explicit `control=True` or `{control:true}` also exposes read invocation and intent preparation. These helpers do not register a host setting, leave a daemon running or grant permissions. See `examples/mcp_policy.py` for a runnable status/preparation example.

The qualified profile covers reviewed local reads, creation of absent candidates and local recovery enabled in the original policy. Uncertain calls are never automatically resubmitted. Delete, overwrite, external transmission and remote-job reconciliation remain outside this profile. Existing host permissions and completion criteria remain authoritative.

## Workbench 1.9.9

The SDK remains a small, one-shot integration layer. This documentation update includes the new Attention and Workbench controls guide; it adds no background service or automatic provider call. See [the guide](docs/WORKBENCH_CLARITY.md).
