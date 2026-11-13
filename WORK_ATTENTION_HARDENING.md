# Work attention: current observation rules

[한국어](WORK_ATTENTION_HARDENING_KR.md) · [Original qualification](WORK_ATTENTION.md)

These changes ship in Harness 1.8.19 and Workbench 1.9.16. They do not switch an installed runtime, approve execution or replace previous qualification records.

- Cancel and pause files are requests. An unmatched operation or existing reconciliation requirement remains visible until its effects are settled. A live operation is not labelled stopped because a request file exists.
- An explicit unavailable runtime or stale evidence stays UNKNOWN. A new attempt supersedes an old stop; that record alone cannot establish that work is running.
- An uncertain adapter's query capability is checked against the existing native call budget. Exhausted capacity needs a recovery decision; missing or invalid capacity stays UNKNOWN. Observation never invokes a query or resubmits work.
- Attention covers managed `jobs` and Universal Work `work-v1`. Legacy registered tasks and direct MCP receipts are outside this list. It is not an inventory of every agent or IDE session.
- The limits are 256 tasks per namespace, 4,096 records / 8 MiB per journal and 8,192 records / 16 MiB across a query. Reaching a journal/query limit produces an individually identified UNKNOWN row. A namespace overflow refuses the query; it does not return an empty all-clear.
- Open an unknown row to inspect its existing task and receipts. Refresh after a concurrent writer settles. For a history exceeding the read limit, use the existing task-specific inspect/status path. Do not delete history or start a duplicate request to clear the badge.
- A stale observation is neither a failed task nor execution permission. Results retain NOT_EVALUATED completion; current completion still comes from native revalidation.

The projection remains read-only and disposable. No new database, timer, daemon, provider call or authority owner was added. Existing resolution actions remain explicit and use the original journal.

## IDEs and the Workbench

VS Code, Cursor, PyCharm and Antigravity IDE can remain the places where you edit and debug. CALF manages the work contract, execution evidence and recovery through its documented CLI/SDK/MCP interfaces. An IDE's presence does not prove its agent is connected to CALF.

Use the IDE's integrated terminal for the CLI instructions. No IDE extension, global setting or hook is changed by this follow-up. Product-specific agent connections must still be configured and qualified through their supported interfaces.

## Verification scope

The local report identifies the exact binaries, native tests, UI projection tests, CLI/API scenarios, load fixtures and target hosts actually exercised. Synthetic fixtures establish contract behaviour, not real-provider correctness, aesthetic media quality, a novice-user study or a token-saving percentage. Historical reports remain unchanged.
