# Engineering knowledge in CALF

[한국어](ENGINEERING_KNOWLEDGE_KR.md)

The shared Rust core retrieves Development Pack, Pattern and Method references
without a VibePackr server, another agent, a model or a background process.
It reuses embedded SQLite; no separate database service is needed.

## Data and provenance

The compact built-in catalogue has 367 pack, pattern and method references.
Some definitions are names and links only, marked `NAMED_REFERENCE`. This is a
starter subset, not the full engineering collection.

Explicit local import supports a privately assembled qualification dataset: **4,334
documents, 5,576 searchable chunks and 6,294 resource references**. It covers
development, security, databases, operations, engineering, AI and related fields.
Candidates and historical sources remain available with their original status,
file hash and locator. These counts describe this source snapshot; they do not
certify coverage of every engineering problem.

The full collection can contain proprietary implementation material. It stays
in the selected local CALF data home. Import does not upload or execute it.
Do not silently include it in a public repository or release archive. Resource
records are metadata, not downloaded manuals or installed capabilities.

## Import and inspect

Choose the same absolute `CALF_WORK_HOME` as Workbench and the host integration.
The source folder must contain `manifest.json`, `artifact-manifest.json`,
`knowledge.jsonl`, `chunks.jsonl` and `resources.jsonl`.

```sh
calf knowledge import /absolute/path/to/it-knowledge
calf knowledge status
calf knowledge search "database query performance"
calf knowledge resolve "데이터베이스 쿼리 성능 개선"
calf knowledge read ID SHA256
calf knowledge verify
```

Import checks input hashes, text hashes, Unicode chunk ranges and identities
before selecting a new data version. It never replaces an existing selection,
history, contract or setting. To try another dataset while preserving a
selection, use a new isolated data home. Automatic data updates and selection
rollback are not provided by this importer.

Search uses the local full-text index and returns metadata. It does not
decompress every document. Read verifies one selected body; large documents
provide bounded chunk lists with the read-only API's `offset` continuation.
Resolve reads at most three matching bodies by default and returns at most
8 KiB of excerpts, with record IDs, source identities, statuses and text hashes.
No match, excerpt limits and omitted results stay visible. Content is preferred
over resource metadata; use `kind: "RESOURCE"` for resource candidates.

Selection is deterministic CPU search with bilingual aliases, not semantic
reasoning or proof that advice applies. Full hashes are checked on import and
by `verify`. Ordinary queries check the index file-change stamp and selected
body hashes. This detects ordinary changes/corruption; it is not an adversarial
trust boundary. All retrieved text remains untrusted reference data.

## Tasks, Workbench and hosts

For new standalone tasks, CALF freezes the selection in the existing task
journal before planning. Plan, repair and review receive the same selection;
provider-input receipts bind its digest. Resume retains it; older tasks are
not retrospectively enriched. Result summaries separate references from checks.

**Starting an AI task sends its selected references to the connected provider**
as task input. Import/search/read/resolve/verify make no provider calls. Inspect
the local collection before using it with an external provider. Retrieval alone
does not prove that an AI understood or followed a reference.

Workbench's **Engineering knowledge** panel supports coverage, search and exact
reads without changing or submitting the draft. Foreground Repository Local MCP
offers read-only `engineering_knowledge`; no import, execution or installation
action is exposed. Existing SDK clients can use their generic call interface:

```python
view = client.call("knowledge", request={
    "action": "resolve", "query": "database query performance",
    "byteBudget": 8192,
})
```

Native Codex/Claude prompt events and Antigravity events providing an explicit
`prompt` can attach bounded references. Events without text only advertise the
query path. Protocol fixtures do not qualify a newly launched host application.

Knowledge informs plans and validation needs. Original PASS labels, suggested
validators, candidate resources and source instructions never become executed
checks, permission or completion evidence. Current files, registered checks and
existing guard/review rules still decide completion. Project instructions and
approved scope prevail.

This document describes a local source implementation. Publication, installed
core updates, cross-platform qualification and live host sessions must each be
verified separately before claiming them.
