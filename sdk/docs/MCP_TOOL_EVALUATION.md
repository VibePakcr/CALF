# MCP tool contracts and evaluation

CALF checks whether a tool fits an existing task, whether a particular call is permitted through CALF, and whether its result meets independently specified conditions. It does not build MCP servers or grant the agent new authority.

This is a **Harness 1.8.12 / Workbench 1.9.8 interface**. The qualified profile covers pinned local **stdio reads, host-admitted candidate creation and explicitly configured local recovery on macOS ARM64, Windows x64 and Linux x64 (Debian 13)**. The full program remains `FOUNDATION_READY`; `INTEGRATION_VERIFIED` applies only to the tested local profile in the attached evidence. Qualification does not establish arbitrary provider, transport or OS support. Existing releases, installed hosts, records and settings are not updated by preparing this interface.

## Separate decisions

| Decision | States | Meaning |
| --- | --- | --- |
| Contract | `VALID`, `INVALID`, `INCOMPLETE`, `UNVERIFIED`, `INCOMPATIBLE` | Formal declarations and supported schema/protocol checks. `VALID` is not an authority or safety certificate. |
| Selection | `SUITABLE`, `UNSUITABLE`, `AMBIGUOUS`, `INSUFFICIENT_CONTEXT` | Compares the task's required capability with capabilities independently reviewed in the local policy. It never changes the task objective. |
| Invocation | `ALLOW`, `DENY`, `REQUIRE_APPROVAL`, `REQUIRE_REVALIDATION` | Checks task/policy/server/tool identity, arguments, exact targets, selected lane and effect classification before `tools/call`. |
| Result | `RESULT_VALID`, `RESULT_INVALID`, `RESULT_INCOMPLETE`, `RESULT_UNVERIFIED` | Separates transport response, output schema, native file evidence, expected values and confirmed process cleanup. Tool `success=true` is insufficient. |

Tool names, descriptions, annotations, resources, errors and result text are untrusted data. No `readOnlyHint`, returned instruction or `approved` argument grants access. The caller's normal host/OS permission boundary remains in force.

## Prepare a local policy

Start with an **already accepted native TASK**. Its scope and criteria remain unchanged. A policy binds its workspace, task ID and exact TASK envelope hash to a pinned server and reviewed rules.

1. Inspect the server source/executable and its intended startup effects under your existing permissions. Discovery starts that process; it is not automatically safe or read-only.
2. Use the existing native executable pinning contract through `tool-contract` action `pin-server`. Its `adapter` input is the normal CALF runtime descriptor (`schema`, `id`, `role`, `command`, `files`, `capabilities`, `class`). This hashes local files without executing them.
3. Normalize a captured tool list with action `normalize`, `server: {id, protocolVersion}` and `tools`. Review the tool names, schemas and returned fingerprints. A reviewed capability belongs to the local rule, not to the tool's own prose.
4. Create a policy with schema `calf.mcp.policy.v1` and hash its exact file bytes. A changed policy needs an explicit new hash; tool contract drift still requires revalidation.

Policy fields:

| Field | Contract |
| --- | --- |
| `workspace`, `task`, `taskHash` | Physical workspace and exact existing accepted TASK envelope. |
| `server` | `{id, adapter}`; `adapter` is the native pinned descriptor/identities result. The reviewed command is absolute and its executable/script identities are rechecked. |
| `requiredCapability` | The capability required for this task; never inferred from a server's instructions. |
| `rules` | At most 32 exact tool rules, described below. |
| `timeoutMs` | 100–5000 ms for the bounded connection/request path, plus owned cleanup. No automatic retry. |
| `gcn` | `null`, or the existing `guard` request with the selected lane/module and this same workspace. A scope guard is not a gate PASS or permission. |

Each rule has `name`, `fingerprint`, `capabilities`, `effect`, `enabled`, `paths`, `postconditions`, and `resultChecks`. Effects are `read`, `write`, `delete`, `external`, or `unknown`. Reviewed reads can execute directly. A write needs the exact prepared intent to pass through the existing host execution entry point; the current write profile creates new candidates and refuses existing targets. Delete, external and unknown effects remain approval-gated and unsupported. Every path binding is `{pointer, allowed}`: a JSON pointer to the input argument and exact relative file names already in TASK scope. No parent traversal, arbitrary absolute path, symlink or hardlink is accepted for these targets.

Native postconditions are nonempty `{path, sha256}` entries within TASK scope. Result checks are nonempty entries of either `{kind:"equals", pointer, value}` or `{kind:"file-sha256", pointer, path}`. The latter binds returned data to an independently read file hash. The complete scoped snapshot must remain unchanged for a read. For candidate creation, every target must be absent before execution, covered by an exact postcondition, and owned by the selected GCN module if a plan is supplied. All other TASK files must stay unchanged. The current profile permits at most four targets of at most 4 MiB each. These checks do not verify arbitrary semantic quality or changes outside that scope.

A write rule may also declare `recovery:"local-artifact-and-native-checks"` **before execution**. This authorizes a separate, host-admitted verification of the local artifact when the original response is lost. It does not make the original response valid. Omitting the option, or setting `recovery:"none"`, leaves uncertain calls unresolved. The option cannot be added retroactively to a failed call because recovery requires the original policy hash.

## Use the explicit interface

```sh
calf tool-contract < normalize-request.json
calf tool-call /absolute/policy.json EXACT_POLICY_SHA256 < request.json
```

A call request is:

```json
{"action":"invoke","name":"read_asset","arguments":{"path":"notes.txt"},"requestId":"read-notes-1"}
```

Other request actions are `discover`, `status` and `reconcile`. Discovery starts and closes the pinned server, while status reads existing native completion. Reconcile records a safe-stop inspection and a current snapshot; it does not resubmit, clear an outstanding invocation, restore a file or infer success.

An optional foreground MCP endpoint is available:

```sh
calf tool-mcp /absolute/policy.json EXACT_POLICY_SHA256
calf tool-mcp /absolute/policy.json EXACT_POLICY_SHA256 --control
```

The default exposes only `calf_tool_status`. Explicit `--control` also exposes `calf_tool_invoke` within the frozen policy. This flag is not a new user approval or OS grant. Registration, policy editing and approval creation are never MCP tools. EOF stops the foreground endpoint; it does not leave a daemon. No host settings are written automatically.

## Host-admitted candidate creation

`--control` also exposes **`calf_tool_prepare`**, with arguments `{request: {...}}`. It prepares an exact intent and local bookkeeping, then returns `REQUIRE_APPROVAL`, a review summary and a command. It does not execute the requested tool. The equivalent CLI is:

```sh
calf tool-prepare /absolute/policy.json EXACT_POLICY_SHA256 < write-request.json
```

The request uses the same `invoke` fields shown above. Review the returned task/version, policy and tool fingerprint, exact arguments/targets, registered checks and expiry. Then run the returned `argv` through the host's existing permission flow. Its form is `calf execute TICKET TICKET_SHA256`. The reserved inner dispatch is not a public direct-write command.

The existing native execution entry point validates and claims the ticket once. The intent binds the selected core, policy, request, target/scope versions, task version and expiry. Changing arguments, the policy, the core or a reviewed file invalidates the handoff. The normal lifetime is 120 seconds, configurable from 100 ms to 300 seconds for CLI preparation. Expiry is checked before dispatch; preparing an intent grants no authority and does not extend its lifetime silently.

**Admission is evidence that this exact command passed through the host execution path. It is not an independently signed proof that a human clicked an approval button.** The host may allow or deny it according to its existing policy. CALF adds no persistent allow rule, credential, global permission or separate approval engine. It never interprets a tool annotation or caller-supplied approval bit as consent.

After a valid write, the wrapper runs every registered native criterion and returns current native completion. A valid tool response or process exit zero alone does not complete the task. Prior approved versions are never selected as write targets by this profile. Candidate adoption remains a separate Work contract operation.

## Evidence and recovery

Discovery, contract validation, selection, invocation, result and safe-stop decisions become collector ACTION records in the task's **existing `history.html` chain**. Summaries bind policy/tool/arguments/result hashes. Untrusted response text is not copied into those events. The original response is returned as data to the requesting client, not treated as instructions or as CHECK evidence.

The existing native `begin`/`finish` contract tracks execution. A successful tool/process observation is an ACTION, not a successful CHECK. Reads still need the task's registered independent checks. Host-admitted candidate creation runs those checks automatically. Invalid/incomplete results and uncertain cleanup leave the start unresolved; native completion stays `UNKNOWN`, even if a later unrelated file check passes. A real failing criterion remains `VIOLATED`.

Validated candidates also carry a required **`mcpArtifact` ACTION contract** that binds the task version and exact scoped snapshot. Completion rejects later drift even if a weak registered command exits zero. A core that does not implement this extension rejects the record and reports `UNKNOWN` rather than ignoring the obligation. `calf --version` advertises `mcp-host-intent-v1` and `mcp-artifact-v1` capabilities. Existing records are not migrated or rewritten.

The same logical request ID cannot execute twice within a task, including after a policy revision or server alias change. An unresolved invocation also prevents using a new ID to submit around it. Timeouts and disconnections retain their evidence. The original safe-stop `reconcile` action still inspects only.

For an original write policy that explicitly enabled local recovery, prepare this separate request:

```json
{"action":"settle","sourceTicket":"/absolute/original-ticket.json","sourceTicketHash":"EXACT_ORIGINAL_TICKET_SHA256"}
```

Send it through `calf_tool_prepare` or `tool-prepare`, review it, then use the same existing host execution flow. Recovery requires the original recorded intent, retained runtime, exact native terminal receipt and confirmed owned-group shutdown. It freezes that receipt and the current scope in the new intent. It then checks the candidate's exact expected hash, unchanged protected files and fresh registered native checks. It never submits `tools/call` again. The original receipt, error/result classification and prior history remain unchanged; new reconciliation and CHECK records are appended.

Missing/changed/foreign receipts, changed contracts or artifacts, unconfirmed cleanup and explicit cancellation prevent settlement. Cancellation is final for that intent. The existing native cancellation marker and host lease signal are checked alongside interrupts during the response wait and independent checks. No monitoring daemon is added. A different remote provider job requires its own authoritative query/cancellation contract; local file recovery cannot establish that remote work stopped or refund incurred charges.

## Limits

- Protocol qualification is MCP `2025-11-25`, JSON-lines stdio, one explicitly pinned local server per policy. An incomplete paged catalogue, duplicate keys/identities, protocol drift or a tool-list change fails closed.
- The bounded schema subset supports boolean schemas, primitive `type`, object `properties`/`required`/`additionalProperties`, array `items`/length bounds, string length/pattern bounds, numeric bounds, `enum`, and `const`. Root input/output schemas must be objects. Unknown keywords, `$ref`, `format`, union types and unsupported dialects remain `UNVERIFIED`; no resolver/network fetch occurs. Numeric matching is limited to finite values within ±(2^53−1).
- Limits include 64 discovered tools, 32 policy rules, 12 schema levels/512 schema nodes, 2 KiB call arguments, bounded frames and the existing native history record limit. Processing is CPU-only, per request; there is no persistent evaluation cache, model or worker pool.
- Starting a pinned MCP process does not sandbox that process's filesystem/network access. CALF checks arguments and observes selected state through this path. Independently launched calls, transient side effects and changes outside selected scope are outside this guarantee.
- GCI/external ETS contracts were not found in this working tree. The owner selected the currently verified GCN/MCL and native record boundaries. General destructive/external operations, remote-job recovery, automatic Repository module mapping and support for other OS/transport combinations remain pending.

See [the implementation audit](MCP_TOOL_EVALUATION_AUDIT.md) and [verification summary](MCP_TOOL_EVALUATION_VERIFICATION.json).

## Released SDK helpers

SDK 0.2.5 provides Python `tool_contract`, `tool_status`, `prepare_tool` and `tool_mcp_server`. Node provides `toolMcpServer`. A descriptor is not registration, and preparing an intent is not permission to execute it. See [the SDK guide](../README.md) and its `examples/mcp_policy.py` example. Native policies and requests use UTF-8; keep the exact policy bytes and published lowercase SHA-256 together.

The Windows recovery test uses a 1500ms request budget, and the Unix test uses 400ms. In the first Windows 400ms trial, the budget expired before dispatch: zero calls, no candidate and UNKNOWN. That trial is retained separately. The successful recovery qualification observed an actual write before response timeout. No completion criterion or expected candidate hash was relaxed.
