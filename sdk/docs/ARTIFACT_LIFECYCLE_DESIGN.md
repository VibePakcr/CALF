# Artifact lifecycle: design review and first implementation

Status: inventory plus reversible index maintenance in development, 2026-11-12. Not packaged or installed. No change to task completion or agent execution authority.

## Existing mechanisms to reuse

- `history.rs` validates native TASK/ACTION/CHECK/DECISION chains. Contracts and original check receipts stay authoritative.
- `journal.rs` provides checkpoint-bound read-only observations of standalone/runtime records. Its SQLite index is disposable; the HTML segments are truth.
- `runner.rs` already records writes, pre-existing versus missing inputs, content snapshots, registered checks and owned operation lifecycles.
- `changes.rs` already stores small before/after content under its hash and checks an existing blob before reusing it; do not add a second deduplication store.
- `work.rs` retains per-attempt output manifests and adoption references.
- `owned.rs` owns process groups/Job Objects. An inventory must not substitute PID existence for those receipts or stop arbitrary processes.
- Repository context is a projection for finding records; it does not own artifact deletion.

Missing: one bounded projection that explains artifact provenance, current file identity, retention reasons, exact duplicates and unresolved operation records together. Existing event recording is reused; no additional database, daemon, recursive project scan or model is needed.

## Common abstraction

`Artifact = domain + relative path + owner references + roles + retention reasons + expected identity + current observation`.

Domains are the explicitly selected workspace and its explicitly supplied journal directory. References bind the original record sequence/hash and task. The same physical artifact may have several owners; task filtering must not erase references from other tasks. Record text is untrusted data. A recorded write to a previously absent path is provenance, not delete permission.

Two readers feed this model:

1. Native history: contract paths, verification inputs and host operation references.
2. Runtime journal: contract paths, write receipts, change-snapshot blobs, provider input and per-attempt output manifests.

All original records and contracts remain untouched. No migration or broad filesystem discovery is performed. Unrecorded files are outside coverage; an absent inventory entry does not establish disposability.

## First implementation boundary

Read-only `inventory` and `plan` use the shared Rust core CLI and existing desktop/SDK API envelope. The plan reports `KEEP`, `REVIEW` and `REBUILDABLE_INDEX_REVIEW`; reading a plan never executes a move. Separate `prepare`, `quarantine`, `retained` and `restore` operations implement the bounded index-maintenance path below. No provider call, permanent deletion or process termination is exposed. Retained copies still occupy disk space; reclaimed bytes remain zero.

Contract files, registered test inputs, before/after snapshots, runtime request evidence and retained/approved candidates have explicit retention reasons. Project tests and databases are not disposable merely because an agent created them. Indexes can be reconstructed only from the validated source records; index review remains advisory.

Exact duplicate detection uses current content hashes and sizes. Similar source text, timestamps, extensions and Git untracked state do not prove duplication. Duplicate bytes are potential overlap, not promised disk savings, and retention references still apply.

## Budgets and observations

- At most 512 known artifact paths and 128 displayed paths by default (maximum 256).
- Existing native history limit: 4096 records/16 MiB. Existing journal observation limit: 4096 records/8 MiB.
- Default aggregate file hashing budget: 8 MiB; configurable from zero to 64 MiB. Files stream through the existing 32 KiB hasher. No file contents are returned.
- Source-chain reads keep their existing independent bounds. Truth files and disposable indexes use metadata in the inventory; the source reader verifies the chain separately. The per-file hashing metric is an upper bound reserved before IO, including failed reads.
- Retain only eight reference previews per path while preserving the full count. Segment files are represented as one retained record set. Task filters do not hide other tasks' pending operations from shared-index review, and overlapping workspace/state paths share retention reasons.
- Preserve unknown/missing/changed/unreadable identities and report truncation explicitly. Never interpret an incomplete projection as a complete cleanup plan.
- Reject traversal, symlinks, Windows reparse points and special files. Do not follow a record to another root.
- Recheck the source checkpoint/head and observed file metadata after observation. This detects ordinary concurrent edits; it is not an OS sandbox or protection against hostile change-and-restore races.
- Operation start/end pairs report recorded lifecycle state only. They do not establish present OS liveness. Open operations or unconfirmed cleanup remain review items.

## Acceptance

Verify existing bytes/mtime and directory membership remain unchanged during queries; both readers; CJK paths; shared references and pinned duplicates; changed/missing files; zero hashing budget; output truncation; invalid paths/symlinks; tampered/changing source; open operations; and the public API wrapper. Run a real installed-project readback using the freshly built core, preserving the existing verdict and originals. No new provider or memory/soak test is required.

The local core suite passed 120 tests, including ten lifecycle acceptance tests; one existing subprocess helper is intentionally excluded from direct execution and exercised by its parent test. A previously completed real Codex task was read through the new CLI and shared API without changing its files or verdict. The existing test-only Rust provider also drove a normal synthetic EDIT → CHECK → REPAIR → CHECK run. Queries against those native-written receipts left the fixture unchanged and did not classify its unrecorded database. No model call was used.

These were the foundation checks, retained as historical evidence. Follow-up validation covers the reversible path and Workbench separately; foundation success alone does not establish those outcomes. Small synthetic fixtures are retained with their manifests.

## Reversible index maintenance

The eligible paths are exactly the native `.calf/ontology.sqlite` and a selected runtime journal's `index.sqlite`. An index is eligible only if its bounded SQL schema and logical contents are reconstructible from the current verified records. Unknown tables, extra columns, triggers, views, hard links and SQLite WAL/SHM/journal sidecars prevent a move. A familiar filename alone is insufficient.

`prepare` is read-only and binds a one-operation identifier, workspace/journal identity, source checkpoint, exact file hash and length. `quarantine` requires that digest and explicit confirmation. The executor takes the existing workspace execution lease and the native writer lock or existing journal writer-file lock, then repeats reference and identity checks. It refuses pending operations, incomplete coverage and any retention reference, including workspace/state aliases. Windows separator and ASCII-case normalization must join those aliases before evaluating retention.

An intent receipt is synced before an exclusive same-filesystem rename. The destination is a private `artifact-quarantine/<operation-id>/payload` beneath the original index's parent. Receipt files describe this filesystem transaction; they do not duplicate task history, establish completion, or add a database. Canonical histories and their existing hash chains are not rewritten. The native no-replace rename APIs are used on macOS, Windows and Linux; unsupported platforms/filesystems fail without falling back to an overwrite or copy-and-delete operation.

`retained` compares both paths with the recorded hash instead of trusting a success flag. Missing/incomplete receipts remain visible as unknown. At most 128 operations and 8 MiB of aggregate file hashing are observed per list call. A repeated committed request returns its observed state without performing another move.

`restore` also requires explicit confirmation and the exact receipt digest. It requires an empty original location, no pending work or sidecars, unchanged authoritative records and the matching retained file. A rebuilt/replaced index, changed records or an uncertain identity leaves the retained copy intact. Restoration preserves the moved file's bytes and filesystem modification time. OS isolation against hostile path replacement, power-loss guarantees beyond filesystem sync support, and physical-space recovery are not claimed.

Workbench's lazy Artifacts panel exposes recorded paths, retention reasons, retained moves and an explicit preview/confirm flow. Its bridge resolves the selected workspace/job from existing local settings rather than accepting caller-supplied roots. Closing or hiding the panel releases rows and previews; it adds no timer or background scanner. Existing user preferences are not changed by artifact operations.

## Core-created managed text and the general-artifact boundary

The existing journal now stores `artifact_intent`, `artifact_created` and `artifact_ref` records. Only the core can seal newly created managed text through the supported API, within its own journal state. Content is limited to 16 KiB and 128 artifacts per journal. Every retained reference and creation receipt is projected from the original chain; no second event database is introduced. Expiry is advisory, bounded to 30 days, and starts at the intent timestamp. There is no cleanup timer.

All references must be released after recorded owner termination, retention must expire, and content identity and full source closure must match before an explicit preview/digest/confirmation can move a managed file. Unsealed intents remain protected. A repeated creation request never repairs or seals an incomplete attempt. Version-2 move receipts bind the original creation hash; old version-1 index receipts remain readable. Managed restoration can tolerate appended references while still requiring that same creation and file identity, no pending execution and an empty destination. Index restoration retains its stricter exact-source-head requirement.

Source, tests, existing logs, arbitrary databases, candidates and recovery snapshots remain outside this executor. Other generated files would require independent ownership and reference closure rather than a filename, age, duplicate hash or model claim. Whole-project cleanup and arbitrary LLM-created files remain outside its scope. The implementation adds no dependency, daemon or provider call and does not weaken completion gates.
