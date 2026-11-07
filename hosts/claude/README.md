# CALF for Claude Code

[한국어](README_KR.md)

This local host adapter connects Claude Code's official lifecycle hooks to the unchanged CALF 1.8.7 Rust engine. It applies to the CLI and local Code sessions in the Claude desktop application. Ordinary Claude chat, Cowork, cloud sessions and other computers do not automatically acquire these hooks.

The adapter starts only when a hook fires. It uses Python's standard library, a pinned native binary and local files. There is no daemon, model proxy, additional model, vector database or network listener. Claude keeps its own account, model and permission policy.

## What it does

- Records session, request and tool observations without storing prompts or reading transcripts.
- Sends an exact registered check through CALF's owned execution ticket.
- Requires current native evidence for a completed registered work item. A tool's text or exit status alone is insufficient.
- Rejects a stale check after files change and retains incomplete/error states as UNKNOWN.
- Records failed tools, API failures and unfinished session endings without resubmitting work.

The 1.8.7 engine already exposes a Codex-compatible hook transport. This adapter translates Claude events into that **pinned internal wire interface**, in a separate Claude-owned state directory. Native low-level rows therefore name that port `codex`; the adapter's receipts identify the real host as `claude`. No Codex model or session is started. This is not a promise that arbitrary future CALF releases accept the same interface.

The adapter removes native `permissionDecision: allow` output. A rewritten command still goes through Claude's permission checks. Existing deny/ask rules, sandbox settings, MCP configuration and credentials are preserved. Hooks are not an OS sandbox and cannot remove unrelated access already held by a host.

## Local installation

The owner-managed installation lives under the physical T9 CALF tools directory. Its `MANAGED-ROUTING.ko.txt` names the conditional installation/recovery helper. The standard Claude user settings file points to its T9 `claude-settings.json`; an existing T9 Claude profile uses the same definition. Only eight CALF hook events are added. New sessions load them automatically; `/hooks` shows the installed definitions.

Each work item needs an explicit contract with scope and independent checks. Use the installed binary's `register WORKSPACE CONTRACT.json --config CONFIG.json` command, then use the returned check command. Preserve the chosen contract; never weaken it to make an agent pass. Unregistered sessions still produce observation records, but those observations do not establish task completion.

SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, Stop, StopFailure and SessionEnd are connected. Claude does not supply a general Interrupt hook. An unfinished turn is marked interrupted when a new request or session-ending/failure event arrives. Immediate cleanup of every background process at an arbitrary UI interruption is not guaranteed by this adapter.

Claude can deny a command after PreToolUse without emitting a tool-result hook. At Stop, or when another request arrives, the adapter closes a matching **never-started, unclaimed** owned check as cancelled. It verifies the ticket identity and cancellation marker, then lets the pinned core write its own cancelled terminal without launching the check command. A claimed ticket is left UNKNOWN until its real terminal is available. Existing passing checks and the denied attempt remain on record; reconciliation does not rerun the work or create a passing CHECK.

Auto mode may reject a registered local check. Use the host's approval flow for the intended command; CALF does not override that decision or add permanent permission rules. Completion also depends on the check's execution environment. A status query from another environment can return UNKNOWN even when an earlier app-session completion was accepted; the historical receipt remains available.

## Preservation and recovery

Records, prior contracts and native permission settings remain in place. There is no settings reset or credential copy. The conditional restore operation removes only unchanged managed settings links that were absent before installation; it retains all CALF records and the versioned binary. If a user edits either link, stop and reconcile rather than overwriting it.

The current implementation uses POSIX file locking. Qualification covers the owner's macOS CLI and an actual local session in the desktop Code tab: report generation, one registered check with eight tests, matching file-version evidence, permission-denial recovery and an accepted Stop verdict. Five isolated reconciliation cases cover denied, successful, legacy-pending, already-claimed and changed-ticket paths. Windows/Linux Claude host integration remains unqualified; the core's cross-platform results do not establish that claim. App-managed UI preferences can update during use and should be distinguished from CALF contracts and settings when auditing preservation.
