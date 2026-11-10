# CALF for Claude Code

[한국어](CLAUDE_CONNECTION_KR.md) · [Installation, update and recovery](HOST_CONNECTIONS.md)

Connect Claude CLI or the Claude desktop app's **local Code mode** to CALF. The adapter supports the qualified Harness 1.8.7–1.8.12 cores and Workbench 1.9.8. Ordinary Claude chat, Cowork and cloud sessions are separate modes. The Claude host adapter is qualified on **macOS only**; the native core and SDK have separate Windows/Linux checks.

The adapter runs when a hook fires, using Python 3.10+, its standard library, local files and a SHA-256-pinned native executable. It adds no model, daemon or network listener. Claude retains its account, model and approval policy. No prompts or transcripts are stored by this adapter.

## What changed

Claude can deny a command after `PreToolUse` without sending `PostToolUseFailure`. CALF previously retained that non-check call as pending. The ninth hook, `PostToolBatch`, now supplies the resolved batch. CALF closes a pending non-check call only when the session, turn, tool ID and input all match. It stores a result fingerprint, not the response text. A resolved denial has no inferred exit code and is not a successful execution.

The whole batch is validated before any result is recorded. Missing results or conflicting identities stay `UNKNOWN`. Batch text cannot complete a registered check: CALF requires its actual owned-execution terminal and matching file hashes. Claimed checks remain pending until their real result arrives. Never-started, unclaimed check tickets can be cancelled through the native core without launching the verifier. Earlier failed and denied attempts remain in the record.

## Install or update

The Harness, Workbench and SDK archives include `hosts/hostkit.py`, this adapter and both language guides. A standalone Host Connections ZIP is also available. Follow the [host installation guide](HOST_CONNECTIONS.md), using physical absolute paths and a private state folder. Prepare a new revision beside the old one, inspect the current settings hash, then apply that exact revision. The kit refuses changed settings, symlinks and an unreviewed existing CALF route.

For new installations the kit merges these nine hooks: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Stop`, `StopFailure`, `SessionEnd`. `PostToolBatch` has no tool matcher. Existing permissions, MCP configuration, unrelated hooks and original settings backups are retained. Review the hooks in Claude and start a new local Code session; an existing session is not proof that it reloaded them.

Use `register WORKSPACE CONTRACT.json --config CONFIG.json` with the selected native executable. Keep the returned check command, scope and criteria unchanged. The adapter may replace the check command with its pinned execution ticket, but never forwards `permissionDecision: allow`. The rewritten command still passes through Claude's approval flow.

## If Auto blocks a check

Inspect the exact registered command. If you authorize that check, use Claude's individual approval flow. In the verified desktop session, the owner temporarily selected Manual, chose **Allow once** for that check, then restored Auto. An always-allow rule is a separate persistent setting; it is not required by CALF and is not added by the adapter.

Do not rerun an unknown or still-running check blindly. Inspect its existing ticket and evidence first. A host message or exit code zero alone does not establish completion. Failed checks remain `VIOLATED`; missing or stale evidence remains `UNKNOWN`.

## Read the result

Workbench **Task status** shows **Recorded completion** and **Current observer** separately. A saved `SATISFIED` can coexist with a current `UNKNOWN` when `LC_ALL` differs. Check **File version** and **Execution context**. The SDK exposes the same read-only view through `registered_status`. CALF does not change environment variables to make a verdict pass.

The real macOS desktop Code session used core 1.8.10: report generation, one check, eight tests, matching file hashes, a native Stop verdict of `SATISFIED`, and return to Auto. That model-session evidence is reused here. New 1.8.11/1.9.6 release binaries receive isolated hook-boundary and installation/update/recovery checks. The separate denied CLI trial verified batch resolution but did not finish its intended work; it is not presented as a successful task.

## Recovery and limits

Keep old versioned binaries, the whole records home, contracts and private kit backups. `recover` reconciles interrupted installation bookkeeping only when saved before/after hashes match; it never restores user settings or rewrites task history. An edited managed hook requires review before an update can continue.

The adapter uses POSIX file locks. Claude Windows/Linux host installation remains unqualified and is refused by this installer. Hooks do not restrict unrelated filesystem access already held by Claude. There is no general Claude Interrupt hook, so immediate cleanup at every UI interruption is not guaranteed. No transcript parsing, model retry, permanent permission rule or automatic adoption is added.

Official host reference: [Claude Code hooks](https://code.claude.com/docs/en/hooks).
