# Artifact ownership, quarantine and restore

[한국어](ARTIFACT_LIFECYCLE_KR.md) · [Design review](ARTIFACT_LIFECYCLE_DESIGN.md)

Harness 1.8.16 · Workbench 1.9.12 · SDK 0.2.9.

Inspect files already referenced by CALF's records, and see which tasks need them. New small disposable text can carry creation receipts, references and a retention deadline from the start. Everything runs on demand in the shared Rust core, using the existing journal. No additional database, background watcher, model call or process sampler is required.

## Read a native workspace

Pass a JSON request to the newly built core. Replace the example absolute path with your workspace; on Windows use an absolute Windows path.

```sh
calf artifacts <<'JSON'
{"operation":"inventory","source":"native","workspace":"/absolute/project","task":"registered-task","limit":128,"hashBudgetBytes":8388608}
JSON
```

Native history supplies contract paths, check-scope references and recorded host operations. It does not establish which individual files the external agent created. The original history and disposable ontology index are also identified. Aggregate CHECK snapshot hashes are never presented as individual file hashes.

## Read a standalone/runtime journal

```json
{
  "operation": "plan",
  "source": "journal",
  "workspace": "/absolute/project",
  "state": "/absolute/records",
  "task": "recorded-task",
  "limit": 128,
  "hashBudgetBytes": 8388608
}
```

The journal's stored workspace identity must match. For universal runtime work, the workspace is the work's own task directory and state is its `records` subdirectory. This reader includes recorded workspace writes, small change/recovery blobs, provider-input references and per-attempt candidate manifests. It retains old candidates as well as current ones.

An existing API client can forward the same request through the native desktop/SDK transport:

```json
{"op":"artifacts","request":{"operation":"inventory","source":"native","workspace":"/absolute/project"}}
```

An optional transport `home` does not create a directory for these core requests. Workbench has an on-demand Artifacts panel; no additional MCP tool is installed.

## Interpret the response

- `owners` and `references` explain the original record linkage. A task filter retains other owners of a shared path. The full reference count is retained; at most eight reference previews are returned.
- `RECORDED_CREATE` requires a completed core write with no previous file. `lineage` binds the original intent and completion receipts. It is historical provenance, not permission to delete. Candidate-manifest observations identify the task and attempt without claiming an unrecorded file creation time.
- `retentionReasons` explains why contracts, test inputs, source, original records, recovery snapshots and candidates stay retained.
- `observation.state` distinguishes `MATCH`, `CHANGED`, `PRESENT`, `MISSING`, `UNKNOWN` and `UNVERIFIED`. `PRESENT` has no expected per-file hash. Truth files/indexes use `METADATA_ONLY`; the source-chain validation is separate. `RECORD_SET` summarizes retained segments.
- `exactContentGroups` contains currently hashed matching paths in this response. It excludes duplicate workspace/state aliases. Logical overlap is not physical savings: hard links and filesystem compression/deduplication are not measured. A group does not authorize removal.
- `pendingOperations` reports recorded starts without matching ends, plus unconfirmed cleanup records. It does not query OS liveness, interpret a missing PID as success, restart work or kill a process. `allSourcePendingOperationCount` still includes other tasks.
- `KEEP`, `REVIEW`, `REBUILDABLE_INDEX_REVIEW` and `MANAGED_QUARANTINE_REVIEW` are advisory. Both inventory and plan are read-only; `cleanup.executable` is false and `reclaimedBytes` is zero.

## Create disposable text with known ownership

This optional path is for new temporary notes, logs or cache text created by CALF itself. It does not import or relabel existing files. Source, test inputs, candidate files, contracts and recovery evidence stay protected.

```json
{"operation":"create","source":"journal","workspace":"/absolute/project","state":"/absolute/records","task":"registered-task","requestId":"build-note-1","role":"temporary","label":"Build note","content":"Small disposable note\n","retentionSeconds":86400,"confirm":true}
```

The task must already exist in that journal. The core chooses an exclusive path under `state/managed-artifacts/ID/payload`, records the intent before writing, verifies the bytes and records a creation receipt. The default retention is 24 hours; the maximum is 30 days. Content is UTF-8, limited to 16 KiB per file and 128 managed artifacts per journal. Expiry starts at the saved intent time. It never schedules deletion.

Reuse the same `requestId` only for the same task, role, label, content and retention. A replay returns the observed state without repeating a write. An interrupted creation remains unconfirmed; replaying it does not manufacture a completion receipt.

Use `pin` to add a reference from another registered task. After an owner reaches a recorded terminal state, release that task's reference explicitly:

```json
{"operation":"release","source":"journal","workspace":"/absolute/project","state":"/absolute/records","task":"registered-task","artifactId":"RETURNED_ARTIFACT_ID","confirm":true}
```

`pin` uses the same shape. All active references must be released and retention must have expired before quarantine becomes eligible. Resumed work, unresolved execution, incomplete coverage, changed bytes or unconfirmed creation block the action. Releasing a reference neither moves a file nor establishes current task completion.

In Workbench, select a completed task and use **Review reference release**. This only releases the selected task's reference after confirmation. The panel shows other owners and the retention deadline. It does not release their references for you.

Python provides `client.artifacts(workspace, operation="plan", state=state)`; Node provides `client.artifacts(workspace, {operation: "plan", state})`. See the SDK's managed-artifact example. The bindings forward requests to the same core; they never edit the journal directly.

## Bounds and incomplete information

The projection accepts at most 512 known path entries, displays 128 by default (maximum 256), and uses an 8 MiB default additional hashing allowance (maximum 64 MiB). Zero requests metadata without reading artifact contents. `hashBytesUpperBound` includes reserved failed reads. Existing source-chain reading has separate native/journal limits.

`TRUNCATED` is explicit; `knownPathsLowerBound` signals that the internal path cap was reached. Duplicate coverage is only the displayed, hashed paths. Unrecorded files are not scanned or classified, including arbitrary files produced outside CALF's mediated path. User files, test code and databases are not considered disposable from age, name, duplication or Git untracked state.

Traversal, links/reparse points, special files, changed checkpoints and invalid record chains are rejected or remain unknown. File metadata and source identity are rechecked; this is not an OS sandbox or a guarantee against hostile change-and-restore races. Inventory results never establish current task completion, change approval policies or replace native checks.

## Quarantine and restore an index

Open **Artifacts** in Workbench, choose workspace records or a task in that workspace, then refresh. **Preview index quarantine** shows the exact file and digest without moving anything. Confirm only after reviewing the preview. Retained moves offer **Review restore**, followed by a separate confirmation.

The core CLI/API accepts the same flow:

```json
{"operation":"prepare","source":"native","workspace":"/absolute/project"}
```

Use `plan.operationId` and `digest` from that response:

```json
{"operation":"quarantine","source":"native","workspace":"/absolute/project","operationId":"RETURNED_ID","digest":"RETURNED_DIGEST","confirm":true}
```

Change `operation` to `retained` (without the confirmation fields) to inspect saved moves. Use `restore` with the same operation ID, digest and confirmation to restore one copy. For runtime records, use `source: "journal"` and the original `state` path on every request.

The digest and confirmation field bind the requested action. They do not grant host permissions or prove that a human approved it; the caller's existing execution permissions still apply.

Index maintenance accepts only `.calf/ontology.sqlite` or a journal's `index.sqlite`, after its schema and contents match the current authoritative records. The managed-text path additionally accepts only a sealed core-created file with no active references and expired retention. Add `"domain":"state","path":"managed-artifacts/ID/payload"` to **every** prepare, quarantine and restore request for that file. Pending work, protected references, hard links, unknown database contents or SQLite sidecars block the move. Existing logs, source, tests, settings, contracts, recovery snapshots, candidate files and unclassified databases are never eligible.

Quarantine uses a private directory beside the index and preserves the full file. **It does not free disk space.** The intent is saved before the move; later inspection reconciles the actual paths and hashes even if the final receipt was interrupted. No permanent-delete operation is provided.

Restore never overwrites a newer file. An index also requires unchanged source records. A managed file may be restored after later references were appended, provided its original creation receipt and exact bytes still match and no execution is pending. Refresh and inspect conflicts; keep the retained copy. There is no automatic retry, record rollback or settings restoration. Metadata/hash checks handle ordinary concurrency and interruption; they are not a hostile-filesystem isolation boundary or a universal power-loss guarantee.

## Verification

### Current release · 12 November 2026

Harness 1.8.16, Workbench 1.9.12 and SDK 0.2.9 have been published for macOS ARM64, Windows x64 and Linux x64. The release packages were downloaded and their SHA-256 hashes checked after publication.

The macOS core suite passed 138 tests. The artifact tests passed natively on Windows (26) and Linux (28); two Unix-only cases are excluded on Windows. The UI suite passed 46 tests and the SDK passed 18 tests on each operating system. Index preview, quarantine and restore were observed in native windows on all three systems. Final Light | Dark toggle clicks were observed on macOS; the final appearance contracts passed on all three systems.

Publishing makes packages available; it does not update another user's installed app or hooks automatically. Follow the installation/update guide and keep the existing records home, contracts, settings and older task runtimes. Native synthetic execution and independent checks are separate from a new paid AI-session benchmark. See the release's `VERIFICATION.json` for exact binary hashes and the scope of each check.

See the release's `VERIFICATION.json` for exact binary hashes, platform results and observed window interactions. Native synthetic execution verifies the runtime and independent checks; it is not a new paid AI benchmark. Earlier index-only evidence is retained below as historical evidence, not as proof of later managed-text functionality.

### Pre-release index-only tests — historical record

The macOS core suite passed 130 tests, including 20 lifecycle tests. The lifecycle tests also ran natively on Windows (18; two Unix-only cases are excluded) and Linux (20). On all three systems, real CLI and Workbench API calls quarantined/restored synthetic indexes, blocked conflicting restores, and preserved protected file contents and modification times. The six new UI behavior tests passed on each system; the complete 43-test UI suite passed on macOS and Linux. All three native UI shells built successfully.

At that earlier stage, preview, confirmation, quarantine and restore had been observed in the macOS Workbench window. Windows/Linux evidence then covered native execution, the API bridge and UI behavior tests. This paragraph describes pre-release tests. The current-release section above covers the later publication and Windows/Linux window verification.
