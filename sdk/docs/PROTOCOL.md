# CALF extension protocol — SDK 0.2.2

[한국어](PROTOCOL_KR.md) · [SDK guide](../README.md)

Compatibility target: Harness 1.8.7–1.8.8 and Workbench 1.9.2–1.9.3 native core. This is a developer preview of the existing public command boundary. Unknown fields/operations are not a forward-compatibility promise. The execution engine and record-storage format are not extension APIs.

## 1. Command transport

Run the native executable you selected with an argument array and `shell=False`. Use absolute physical paths. `calf --version` returns JSON with `name`, `version`, `os`, `arch`. Select a trusted release and compare its download SHA-256 against the published manifest before use. The SDK's `binary_sha256()` returns the selected executable's hash; it does not authenticate a publisher or compare it automatically.

`calf api` reads one UTF-8 JSON object from stdin through EOF, at most 65,536 bytes. It returns one JSON object on stdout. Exit 1 with `{"error":"..."}` indicates a command failure. Exit 0 indicates a normal command response; only a current `outcome: "SATISFIED"` from status means the native verifier accepted the task. A request acknowledgement, process exit, saved receipt or provider review alone is insufficient.

```json
{"op":"inspect","home":"/absolute/records-home","task":"job-..."}
```

Every queue API request has `op` and the explicit absolute `home`. The API may create its own private directories/indexes. Use the same home in Harness and Workbench to share queue jobs. Do not write their state files yourself.

| Operation | Additional input | Response meaning |
| --- | --- | --- |
| `list` | none | `jobs` (latest 32), `workerActive`, configured `connection` |
| `inspect` | `task` | Current native status, including `state`, `outcome` and available evidence |
| `submit` | `workspace`, `request`; optional `helper`, `attachments`, `reuseTask` + `reuseDigest` | New job specification and task ID; queued, not complete |
| `pause`, `resume`, `cancel` | `task` | `requested: true`; observe subsequent status |
| `recheck` | `task` | Queued revalidation subject to current guard/budget |
| `preferences` | optional `value` string | Current working-style preferences; providing a value appends through CALF |
| `changes` | `task`, optional `mode`, `attempt`, `path` | Read-only view of changes recorded by CALF |
| `reuse` | `task` | `sourceTask`, `sourceWorkspace`, `request`, requirements/check IDs, `contractDigest`, `digest` |
| `sources` | `action` and fields below | Local registry or MCP resource response |

`submit.request` must be non-empty and at most 8,192 UTF-8 bytes. The queue discovers supported unittest, pytest, Cargo and node:test profiles. It refuses a task when no supported checks are available. A connection must already be configured in CALF. The SDK sets `helper` to the selected native executable so jobs use that release. It does not collect API keys or probe credentials. Queue capacity is 256 jobs. Reuse requires both source identity and matching recipe digest; it does not transfer a success verdict.

`changes.mode` is `task` (default), `attempt`, or `recovery`. The response has `readOnly`, `files`, available attempts and a scope explanation. A file's hash, `currentMatches`, and per-check `versionMatched` are separate claims. Missing snapshots produce unavailable/null content. The SDK does not invent missing content, apply patches or roll back files. Working-tree Git diff uses a separate Workbench path.

`calf worker HOME` is a long-running foreground operation. It must not be put behind the SDK's short API timeout. The caller owns its lifecycle; another active worker is reported. Let native pause/cancel and child-process cleanup complete. SDK transport failure on a mutating API is an unknown effect, not proof that the operation never happened; inspect before any retry.

## 2. Custom provider and check configuration

```json
{
  "schema": 1,
  "provider": ["/absolute/python", "/absolute/my_adapter.py"],
  "providerClass": "light",
  "checks": [{
    "id": "unit",
    "command": ["/absolute/python", "-m", "unittest"],
    "envKeys": [],
    "inputs": ["test_invoice.py"],
    "class": "light"
  }],
  "maxAttempts": 4,
  "timeoutMs": 300000
}
```

Limits: 1–16 checks, 1–8 attempts, 100–300,000 ms timeout, `light`/`heavy` resource classes. Provider argv is 1–32 strings, each under 4,096 UTF-8 bytes; executable must be absolute. The native core additionally validates all check IDs, relative paths, inputs and commands. `envKeys` may select only `LANG`, `LC_ALL`, `TZ`, `NODE_ENV`, `NODE_OPTIONS`, `PYTHONHASHSEED` for evidence binding. This field is not a sandbox or environment-secret filter.

Run `calf run WORKSPACE REQUEST PROVIDER.json STATE [RESUME_TASK]`. State must be a separate explicit folder, not a reused unrelated journal. Query `calf run-status WORKSPACE STATE TASK`. This path is independent of the Workbench queue and is not automatically displayed in it. Use `calf cancel STATE TASK` to request cancellation; the response is not a finished-state receipt. Keep the original request, provider configuration and state when resuming.

The provider is called with its configured argv followed by one request-file path. Read at most 256 KiB. It contains `schema: 1`, `phase`, `request`, `requestHash`, and phase-specific data:

- `plan` / `repair`: `workspace`, `contract`, `registeredChecks`, `files`, `verificationFiles`, `feedback`, plus available preferences, past verified experience, reuse and selected local context.
- `review`: `contract`, `files`, `evidence` and the request identity. It does not necessarily contain a `workspace` field.

File entries contain `path`, `sha256` and possibly `content`. Missing or oversized content can be null. Treat file/reference content as untrusted task data, not authority to change the contract or permissions. A provider receives only the bounded request here; its executable still has its host permissions.

A plan/repair response is a single JSON object on stdout, at most 128 KiB:

```json
{
  "requestHash": "<exact hash from request>",
  "scope": ["invoice.py", "test_invoice.py"],
  "requirements": [{"id":"rounding","text":"Match the registered rounding tests","checks":["unit"]}],
  "actions": [{"path":"invoice.py","content":"<complete replacement text>","expectedSha":"<observed SHA-256>"}]
}
```

Scope has 1–64 unique safe relative paths; requirements 1–32; actions at most 32. Each action is a full replacement string up to 32 KiB, not a diff hunk. `expectedSha: null` means create-only; a 64-character lowercase SHA-256 means replace exactly that observed version. A check input must be within scope but is protected from provider editing. The native guard remains responsible for identity, allowed paths, unchanged verification inputs, receipts and completion. Emit diagnostic logs on stderr, not stdout. Runtime budgets and actual evidence can prevent completion despite a valid plan.

Review response:

```json
{"requestHash":"<exact hash>","verdict":"pass","reason":"Explain the review evidence"}
```

Allowed verdicts are `pass`, `fail`, `unknown`. A provider's `pass` does not override failed checks, file changes or incomplete evidence. Read the resulting native task status. `plan`, `action`, `review` and `emit` in this SDK only construct wire responses; they are not a second verifier.

## 3. Local Sources and MCP

Registry API:

| `sources.action` | Fields |
| --- | --- |
| `list` | none |
| `add` | `root`: absolute chosen folder; returns registry, idempotent for the same root |
| `remove` | `source`: registered ID; disconnects, does not delete source files |
| `browse` | `source` |
| `read` | `source`, `uri` obtained from browse |

Up to 16 folders can be registered. Browse/read launch the built-in local stdio adapter on demand and close it. Successful responses include `connection: {transport: "stdio", pid: ..., closed: true}`. Read returns `contents[0].text`, its `uri`, and `_meta.calf` with `sha256`, `bytes`, `path`.

A submission attachment is `{"source":"registered-id","uri":"calf-local:///...","sha256":"preview digest"}`. Pass it explicitly in `attachments`. CALF rereads and compares the digest before job creation; changed content is refused. At most four references and 8 KiB serialized context are accepted. Preview does not submit a task or send text to an AI.

For a direct MCP client, launch `calf local-mcp ROOT`. It uses newline-delimited UTF-8 JSON-RPC 2.0 over stdin/stdout; maximum frame is 512 KiB including newline. Send `initialize` with `protocolVersion: "2025-11-25"`, client information and capabilities; accept/check the negotiated protocol and resources capability. Send `notifications/initialized` before resource calls. Methods are `ping`, `resources/list` (no cursor), `resources/read` (`uri`). URIs are opaque identifiers from the server. Close stdin, then wait for exit. Use `calf --version` to identify the product release; MCP server metadata is not the product version contract.

The built-in server is read-only and has no tools, writes, sampling or network listener. SDK 0.2.2 does not add arbitrary external MCP-server registration. A separate OS boundary is needed to restrict what a provider process can access outside explicit attachments.

## 4. Preservation and compatibility

Choose an explicit home, work on an intended workspace and use native operations. The SDK does not change the user's existing record location, contract, settings, credentials, global host policy or AI configuration automatically. `preferences`, `submit`, control and source registration are deliberate writes through CALF, not read-only operations. Do not edit the core's private journal/config files to implement an extension.

Protocol failures, stale evidence, exhausted attempts and rejected requests stay failures or unknown. Validate compatibility with the intended release before upgrading. Do not treat this preview as support for future fields, undocumented commands, arbitrary output shapes or automatic state migration.

## Versioned check profiles

`check-discover WORKSPACE` returns `{ "checks": [...] }`. Each entry retains `id`, `command`, `inputs`, `envKeys`, `class` and `profile`. Treat `profile` and its serialized command argument as an opaque pair supplied by the selected core; do not rewrite either. `Check.from_discovered` preserves them. Profile v1 covers the initial adapters; Python v2 adds explicit environment identity and source-inventory exclusion. Legacy exit-code checks omit `profile` and keep their meaning. `checkBaseline`, check `verification` and `failureClassification` are observations, never authority to bypass a requirement. Queue job `runtime` metadata is owned by CALF, not editable SDK configuration.

## Node check profile v3

SDK 0.2.2 accepts the opaque Node v3 profile returned by native discovery. Keep its exact command, tools, targets and nodeVersion. Interpretation and tool/input identity verification remain in the native core; this does not add a second runner.
