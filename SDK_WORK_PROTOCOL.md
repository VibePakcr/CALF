# Universal Work v1

Compatible with CALF **1.8.7–1.8.8 / 1.9.2–1.9.3** and SDK **0.2.2**. [한국어](SDK_WORK_PROTOCOL_KR.md).

This additive protocol supervises file-producing work across runtimes. Python text processing, Node data aggregation and a loopback HTTP service use the same contract. It does not require an AI model, a multi-agent framework, or a background service. A single connected agent or application can drive it. The core remains private; the SDK and example adapters contain no execution engine.

## Contract → candidate → check → adoption

`WorkSpec` freezes a logical request key, adapter, parameters, input file hashes, output paths and bounds, required checks, attempt budget and adoption policy. `submit` snapshots inputs, pins the core executable and registered tools, and records the contract hash. It does not execute work. Duplicate keys return the original work only when the complete spec matches; a different spec is rejected.

`step` runs the registered adapter once or reconciles the existing request. Each attempt has a new candidate directory and a stable `requestId`. An executor's `succeeded` response means only that production ended. CALF inventories and hashes every declared artifact, runs every required check, rechecks inputs/tools/artifacts, and binds the check receipt to the manifest digest. Missing, extra, linked, oversized or changing files cannot pass. `UNKNOWN` and `VIOLATED` never permit adoption.

`adopt` selects a validated manifest; it does not overwrite source files, publish files, or deploy anything. Manual adoption supplies the exact manifest digest. Automatic adoption must already be specified in the frozen contract. Previous attempts and adoption journal events are retained. The current API selects the current candidate only; selecting an earlier adoption is not yet exposed.

## API and SDK

Send one JSON object to `calf api`:

```json
{"op":"work","home":"/absolute/records","action":"inspect","work":"work-<64 hex digits>"}
```

Python (standard library only):

```python
from calf_sdk import CalfClient
client = CalfClient("/absolute/calf", "/absolute/records", timeout=35)
accepted = client.work("submit", spec=work_spec)
result = client.work("step", work=accepted["work"])
verified = client.work("inspect", work=accepted["work"])
assert verified["verified"] and verified["outcome"] == "SATISFIED"
```

Node ESM (no npm dependencies):

```js
import {CalfClient, isSatisfied} from './node/index.mjs';
const client = new CalfClient('/absolute/calf', '/absolute/records');
const accepted = await client.work('submit', {spec: workSpec});
await client.work('step', {work: accepted.work});
const result = await client.work('inspect', {work: accepted.work});
if (isSatisfied(result)) console.log(result.manifest.digest);
```

On Windows use absolute native `calf.exe`, interpreter and records paths. Inputs must resolve to physical regular files. Output paths use portable `/` separators. Set the client timeout above the contract's operation timeout plus cleanup time. Neither SDK retries mutations after a transport failure: inspect/reconcile first. Configure the client's temporary directory using the host's normal local policy.

| Action | Meaning |
|---|---|
| `register(adapter=...)` | Register a pinned executable, adapter files, role and capabilities. Replacing an existing ID is rejected; use a versioned ID. Local API only. |
| `adapters`, `list` | Bounded registry/task discovery. Inspect an individual work for verified evidence. |
| `submit(spec=...)` | Freeze contract and inputs; no execution. |
| `inspect(work=...)` | Verify journal, current file identity and adoption validity. A busy projection is explicitly unverified/UNKNOWN. |
| `step(work=...)` | Execute once, query an unresolved job, or finish validation. A single call need not finish asynchronous work. |
| `cancel(work=...)` | Record a cancellation request; use step/query to confirm termination. |
| `retry(work=...)` | Make a settled work ready for a new attempt within its original budget; retains prior candidate and adoption. |
| `recheck(work=...)` | Check an existing candidate again without running its producer. |
| `adopt(work=..., digest=...)` | Select the exact current validated version. |

See [schema](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip), [runnable client](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip), [Python executor](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip), [Node executor](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip), [independent validator](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip), and [HTTP bridge](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip).

## Runtime adapter contract

An adapter is an explicitly registered argv vector, never a shell string. CALF appends one request-file path. It runs on demand with a cleared environment and a small allowlist of system/runtime/temp variables; credentials are not inherited. It owns and cleans up the process group (Windows: Job Object). Interpreter and declared adapter files are hashed before and after execution. This does not attest every transitive library or OS component; pin and package dependencies in your adapter distribution.

The request is `calf.runtime.v1` with `operation`, `requestId`, `work`, `attempt`, `providerJobId`, `parameters`, copied `inputs`, declared `outputs`, `outputDirectory`, and `extra`. Operations are `execute`, `query`, `cancel`, or `validate`. The adapter reads the file and writes one JSON response to stdout; diagnostics belong on stderr.

Executor response:

```json
{"schema":"calf.runtime.v1","requestId":"work-...:1","state":"succeeded","providerJobId":null,"usage":null}
```

States: `running`, `succeeded`, `failed`, `cancelled`, `unknown`, `not_found`. A synchronous executor cannot return `running` or `unknown`. Asynchronous adapters must support query by stable request ID even when no provider ID was received. A known provider job ID cannot change. `not_found` must be an authoritative response that no request was accepted, not a timeout guess. Unknown async state holds the home-wide execution slot and must be reconciled; CALF never substitutes another execute call. Cancellation/query capabilities are explicit. The HTTP example uses loopback only and performs no proxy, redirect, or retry.

Validator response binds `checkId` and `manifestDigest` from `extra`, plus `outcome` (`SATISFIED`, `VIOLATED`, `UNKNOWN`) and a bounded `reason`. Registered validator executables run separately from producers. Built-in checks are exact SHA-256, JSON Pointer equality, and text containment. Every output requires at least one check. Media quality, correctness of a model's opinion, business rules and completeness depend on the checks you supply.

## Local MCP

`calf work-mcp /absolute/records` is a foreground JSON-lines stdio MCP server (2025-11-25). It exposes `work_list`, `work_inspect`, `work_adapters` by default. Add `--control` to expose submit, step, cancel, retry, recheck and adopt. Registration is not exposed. `client.work_mcp_server(control=True)` / `client.workMcpServer({control:true})` returns the launch configuration; it does not write host settings or launch a server. Existing folder/source MCP remains unchanged.

MCP does not grant OS permissions. The host chooses whether an agent may call mutation tools. `explicit-client` records an authorized client action, not proof of a human click. No sampling or multiple-agent orchestration is introduced. This server processes calls sequentially; cancel during a blocking call must use a separate native API/SDK process. Inspect remains available from a separate client as an explicitly unverified busy projection.

## Bounds, recovery and guarantees

* WorkSpec <48 KiB; frozen contract and runtime envelope ≤64 KiB; up to 16 inputs, 16 outputs, 32 checks and 8 attempts. Input total, output total and each artifact ≤512 MiB. These are upper bounds; adapters may impose smaller limits.
* Output inventory ≤112 entries / 6 directory levels, at most 16 files. JSON/text checks load at most 1 MiB. Hashes and input copies stream in 32 KiB chunks. Runtime output is captured with the existing bounded process layer; JSON response ≤64 KiB. No artifact-history preload, embedding index, model, or new resident cache.
* The existing resource fader and the same worker lock are reused. One unresolved universal execution per records home; legacy code workers wait behind its reservation. Different homes are separate execution scopes.
* Records live under additive `work-v1`; old code-job records, settings, contracts and source MCP need no migration. Each task retains its starting core executable for resumption after an update. A missing/tampered retained executable blocks that task.
* An unconfirmed process-group cleanup or async submission stays UNKNOWN and reserved. If a synchronous process is durably recorded as stopped but its response was lost, recovery settles UNKNOWN without pretending its artifacts passed. A crash before that termination receipt may require host-level investigation; the system does not infer safety from a PID disappearing.
* Hash binding detects changes at recorded inspection boundaries; it is not an OS sandbox, a tamper-proof authority, or protection against a malicious process racing file reads. Run only trusted registered adapters with appropriate host isolation. Output bounds are checked at collection, not kernel disk quotas. This first contract covers file artifacts; remote DB mutations, external payments and arbitrary app side effects need specific adapters and validators.
* `usage` is retained as provider-reported metadata, not a verified cost ledger or refund guarantee. Monetary budget enforcement, remote credentials/allowlists, remote service authentication and monetary accounting are not included. Workbench Runtime Work projects the same native records.
