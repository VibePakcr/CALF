# Workbench: decisions, results and request guidance

Current release: Workbench 1.9.16. The new UI was observed in the actual macOS, Windows and Debian 13 release executables. The 62-test regression evidence is reused for identical UI source. See [the current screen guide](UI_GUIDE.md). Dated development notes below retain their original scope and limitations.

[한국어](WORKBENCH_CLARITY_KR.md)

Usage guide for Harness 1.8.13 and Workbench 1.9.9. Keep the existing records home, contracts, settings and older task runtimes when updating.

## Attention

Open **Attention** to see native work records that require a human decision.
The list distinguishes decisions, unreadable observations and stale progress.
An empty decision list does not establish that every project is complete.

**Open task** collapses the list and opens either the task's result summary or
its existing Runtime Work view. Opening it never runs, resumes, retries, adopts
or approves work. Use the existing task actions after reviewing the evidence.
Artifact adoption remains separate from execution permission.

The view reuses the native `calf.attention.v1` projection. It reads on open,
explicit refresh, changed visible queue observations and runtime actions. It has
no independent polling timer or resident process. Hidden windows release its
rows. Cards render in groups of twelve. The native observation limits and
unsupported legacy/MCP-host receipt inventories remain unchanged. These are
in-app indicators; this increment does not send system notifications.

## Result summary

Expand **Result summary** below a task's state. It reads current native status
and captured task-write metadata, then shows:

- changed files and whether their current versions match the write receipts;
- recorded check groups, available test totals and the saved model review;
- current completion, the historical result and the observation time;
- limitations and an existing next action, including opening Diff.

Closing the summary releases its evidence text. Reopening revalidates current
files. Saved test totals are historical execution facts, not a new completion
rule. Missing change observations are unavailable, not zero changes. A saved
PASS with a current UNKNOWN remains unconfirmed.

Runtime Work also has a summary. A validated candidate is not automatically
adopted, and an unconfirmed adopted-file version is not displayed as verified.

Long task requests show a compact preview. **Show full request** reveals the
original text; folding it never truncates or rewrites the saved request.

## Shape request

Choose **Shape request…**, then describe the result, what must remain unchanged
and how to check the result. Task types change the prompts, not native rules.

**Find existing checks** runs the existing local setup diagnosis on demand.
Discovery is not test execution. **Use check guidance** fills an empty check
field with the discovered registered check identities. A changed workspace
invalidates discovery while retaining the user's draft for review.

**Add to request** appends guidance to the exact existing draft. It does not
submit or freeze a contract. **Undo helper text** restores that draft only if
the user has not subsequently edited it. Repeated insertion of the same block
is disabled. Requests are checked against the native 8 KiB UTF-8 limit.
Composition input is respected; CJK text stays plain text throughout.

Review the request and choose **Submit** through the existing single-agent
workflow. Native planning freezes the actual criteria. Supported project tests
are still required, and unsupported requested behaviour needs its own evidence.
The helper does not create tests, install dependencies, grant permission or
waive a required check.

## Day and Night

The control beside Refresh changes only the central workspace. Side panels and
the header retain midnight blue. Day uses light surfaces with darker text,
Diff colours and node outlines. Night retains black terminal and input areas.

Night is the default. An explicit choice is saved only in the Workbench home's
`appearance.json` (schema 1), separately from `ui.json`, task contracts and agent
preferences. Reading a missing preference creates nothing. Invalid or linked
appearance data is refused rather than replaced. This preference grants no
execution authority.

## Find a recent task

Use **Find task…** or **Cmd/Ctrl + K** to search recent tasks by request, task ID,
workspace or observed state. Korean, Chinese and Japanese text are supported.
The finder uses the task list already on screen; it does not scan the full journal
or contact an AI service. Runtime Work retains its separate work selector.

Use the arrow keys to move, **Enter** to inspect and **Esc** to close. Opening a
task selects its graph and revalidates its result summary. It does not submit,
resume, retry, approve or adopt anything. Search labels say **Observed** because
they describe the last queue observation, rather than a new completion check.
Closing the finder clears its results and returns focus. Your request draft stays
untouched, and composing text with an IME does not trigger shortcuts.

## More room for the task

Below 1,200 pixels of window width, system and worker monitors start folded.
**Show monitors** opens them over the right edge, leaving the central layout in
place. Use **Hide monitors**, **Close**, or **Cmd/Ctrl + Shift + M** to fold them.
Wider windows show the monitors alongside the task by default.

A manual choice lasts for the current window. Reopening follows the window width
again; no global preference is added. Folding the monitors stops their system
sampling and elapsed-time updates and releases their displayed rows. Task Flow
and task execution continue. Showing the monitors requests a fresh sample.

## Initial validation — 10 November 2026

Actual macOS window interaction, local native fixtures and one real Codex task
were used. That task passed four registered tests, a separate review and an
independent four-test run while retaining its tests and owner note. Actual
external change to a separate synthetic fixture produced historical SATISFIED
and current UNKNOWN. Windows/Linux GUI qualification and release/install
activation are separate work; previous cross-platform core evidence is not
presented as fresh GUI validation. No memory/soak test was added.

## Follow-up validation — 11 November 2026

The responsive monitor controls and task finder passed 37 UI tests on macOS,
Windows and Linux. Both remote hosts ran fresh synthetic-provider tasks through
real native checks, independent Python tests and the native desktop bridge.
These are offline integration fixtures, not fresh AI-provider sessions.

The actual Mac window passed keyboard, Esc and narrow-overlay checks. Actual
WebView rendering was also observed on Windows and Linux. The owner's Windows
screenshot confirms the task graph, CJK text and monitors; its `FAIL / no_progress`
belongs to the deliberately failing fixture. An earlier view of Explorer and an
empty window title from the remote shell did not establish an application failure.

The owner also confirmed Windows search, monitor controls and Day switching.
Those clicks were assisted by the owner, rather than independently reproduced
through remote input. Linux remote click/key delivery remains unqualified.
Native appearance tests passed on macOS (4), Windows (3) and Linux (4), including
Day/Night persistence and preservation of unrelated settings. See
[the verification record](WORKBENCH_NAVIGATION_VERIFICATION.json). This section describes pre-release validation. Follow the existing update procedure to apply the new version to your environment.
