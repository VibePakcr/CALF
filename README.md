# CALF — Controlled Agent Lifecycle Framework

[한국어](README_KR.md) · [Downloads](DOWNLOADS.md) · [EN/KR manual](CALF_mannual.html)

CALF is a lightweight local harness and workbench for supervising one AI agent's work, from execution through checking and recovery. It links requests, actual changes and check evidence, while keeping failed and unfinished attempts in the record. Codex and Antigravity use native hooks; Claude CLI and the desktop app's local Code mode use a macOS adapter. Each host keeps its own account, model and approval policy.

## Latest release · 2026-11-09

**Harness 1.8.11 · Workbench 1.9.6 · SDK 0.2.4**

A non-check command denied before execution no longer has to remain pending when Claude supplies its resolved `PostToolBatch` result. CALF matches the session, turn, tool and input before recording resolution. A denial never becomes execution success or a passing CHECK. All product archives and the SDK now include the nine-hook adapter, install/update/recovery tools and English/Korean guides.

An actual Claude desktop Code session ran one registered check with eight passing tests and recorded `SATISFIED`. Auto initially denied that check; it ran after an individual Allow once approval, then the session returned to Auto. This is not a claim of unattended Auto approval. Fresh release-binary checks and reused model-session evidence are separated in [verification](VERIFICATION.json).

| Edition | Purpose |
|---|---|
| Harness 1.8.x | Headless core and hooks for an existing agent |
| Workbench 1.9.x | Rust + Tauri interface for the same execution and records |
| SDK | Python/Node clients, Local MCP and runtime adapters |

## What you can do

- Define a work contract and require checks tied to the current files.
- Follow Task Flow, Git Graph, Diff, Evidence and worker terminals.
- Use unittest, pytest, Cargo integration tests and node:test, with tools prepared in your project.
- Attach selected local references and connect other runtimes through MCP, SDK and adapters.
- Continue work from the same records home, retaining each older task's pinned runtime and remaining attempt budget.

Workbench **Task status** separates recorded completion from the current observer verdict. Even matching files can keep a current `UNKNOWN` if `LC_ALL` differs; CALF shows that difference. Details load when needed. No additional model, resident server or GPU control compute is required.

## Install and update

Choose macOS ARM64, Windows x64 or Linux x64 in [Downloads](DOWNLOADS.md), then extract into a new folder. Keep the complete existing records home (`CALF_WORK_HOME`), contracts, settings and older executables. Review hook updates in the same installation root and verify them in a new session. Publishing a release does not replace hooks in running sessions or add permanent allow rules.

[Host connections](HOST_CONNECTIONS.md) · [Claude guide](CLAUDE_CONNECTION.md) · [SDK guide](SDK_README.md) · [Status guide](STATUS_CONTEXT.md) · [Earlier releases](https://github.com/VibePakcr/CALF/releases)

The Claude host adapter is qualified on macOS only, separately from Windows/Linux core and SDK tests. macOS apps have an ad-hoc integrity signature and are not Apple-notarized. Windows packages have no publisher signature.

## See the Workbench

![Saved completion and current observer](workbench-status.png)

Actual Workbench 1.9.5 capture of the Claude check: saved success is separate from the current UNKNOWN caused by LC_ALL. Version 1.9.6 retains this status interface.

[Task Flow](workbench-task-flow.png) · [Diff](workbench-diff.png) · [Runtime Work](workbench-runtime.png): earlier actual 1.9.2 record views remain available. 

![Diff · retained actual 1.9.2 view](workbench-diff.png)

![Runtime Work · retained actual 1.9.2 view](workbench-runtime.png)

## Free use, closed core, official extensions

**CALF is free to use. Its core source is not publicly released.** A public download repository does not make the runtime open-source. Unauthorized reverse engineering, decompilation, disassembly, binary patching and alteration of the proprietary core are prohibited and may lead to legal action under applicable law. Free use does not grant rights to extract, modify or redistribute a modified core.

Build extensions through the provided **SDK, Adapter and MCP** interfaces. SDK source follows its separate integration license; the core implementation remains private. These restrictions concern the proprietary runtime, not your own project code or supported configuration and extension interfaces. Bundled third-party licenses and notices remain in force.

[Separate Repository extensions](https://github.com/VibePakcr/CALF-Extensions) · [Release notes](RELEASE-NOTES.md)
