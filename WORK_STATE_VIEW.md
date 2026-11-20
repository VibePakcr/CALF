# Workbench 1.9.24 — work flow and review requests

[한국어](WORK_STATE_VIEW_KR.md)

1. Select a managed task. Read its request, recorded state and state explanation above the work trail.
2. Choose **Flow** for work/check/repair lanes or **History** for the same steps in execution order. Both views retain the selected step and keyboard focus.
3. Select a step to read its detail, status, time and available journal sequence, operation ID or process ID. A recorded process does not establish that it is still running.
4. Choose **Task evidence** to read that task's current evidence. **Review requests** opens the existing Attention panel.
5. In Attention, choose **Needs review**, **Observation gaps** or **All observed**. Expand **Observation evidence** for last progress and the exact recorded sequence/hash when available. **Open task** reads the task; opening a card is not approval.

The work trail shows at most 12 recent projected steps. Earlier records remain retained; this view is not a complete journal export. Flow arrows express observed execution order, not an inferred dependency graph. History uses the same bounded steps.

Attention retains the native query's scope, bounds and freshness. Its current decision classes cover artifact-adoption and recovery review; it is not a universal inbox for every CLI question, login request or provider approval. Missing and stale observations stay visible, and age alone is not failure. Historical success remains historical until current checks support completion.

The selected older task's result remains visible outside the collapsed work list. Narrow windows keep the request controls reachable while the flow area scrolls. The UI reuses existing records and native reads without adding a database or background worker.

Update from 1.9.23 using Updates or a new extracted folder. Keep records, contracts, settings and pinned task runtimes. Host tasks continue in their original host. Harness 1.8.25 and SDK 0.2.11 are unchanged.
