# CALF — Controlled Agent Lifecycle Framework

CALF is a lightweight, local harness and workbench for supervising AI work. Submit a task to an AI agent, follow its execution, inspect the changes, and check the result against your requirements. Failed and incomplete attempts stay in the local record so you can investigate or resume them.

**Harness 1.8.x** runs without a desktop window. **Workbench 1.9.x** adds a Rust + Tauri interface to the same runtime and task records. Codex and Antigravity connect through native hooks; Claude CLI and desktop local Code use a separate macOS adapter. Each host keeps its own account, model and permission policy.

**New in Harness 1.8.8 / Workbench 1.9.3:** Antigravity commands with long, truncated output now retain their actual exit result. The result must match the session, step and transcript location; missing or conflicting evidence still stays UNKNOWN. English and Korean guides have also been revised for clarity.


**Repository Navigator:** [free extension and illustrated manuals](#free-repository-navigator-extension).

## Host connection companion

[CALF 1.8.8 three-host kit](https://github.com/VibePakcr/CALF/releases/tag/hosts-v1.8.8.1) documents Codex, Antigravity and Claude local Code connections. [English](hosts/README.md) · [한국어](hosts/README_KR.md). The Claude adapter has been tested on macOS. [Local Pack Tools + Repository pack](https://github.com/VibePakcr/CALF-Extensions/releases/tag/packs-v0.1.0-preview.1) separately supports verified installation and recovery on macOS, Windows and Linux. This kit is a separate download from the native engine and Workbench.


[English](README.md) · [한국어](README_KR.md)

**[Direct downloads · 바로 다운로드](DOWNLOADS.md)** — choose your OS without opening the Releases list. If an embedded browser reports a Releases error, use these links or open them in your browser.

## What you can do

- **Define and check work:** set the allowed changes and required checks, retain each attempt’s outputs, and require the adopted files to match the hashes recorded by their checks.
- **Follow the work:** inspect Task Flow, Git Graph, Diff and Evidence. Runtime Work brings Python, Node and local HTTP adapter jobs into the same record.
- **Resume after updates:** new tasks keep their starting runtime, checks and remaining attempts. Lost responses are queried by their existing request ID to avoid duplicate execution.
- **Connect your tools and references:** use the Python or Node SDK, or Local MCP. Attach only the local references you choose. Enable MCP control tools explicitly when you need them.
- **Use project checks:** discover unittest, pytest, single-package Cargo integration tests and node:test. Prepare the required tools and dependencies in your project first.

CALF focuses on one agent’s work at a time. It loads the selected work and files as needed, without adding a model or resident service.

## Free use, closed core, official extensions

**CALF is distributed free of charge for use. Its core source code is not publicly released.** A public download repository does not make CALF open-source or transfer rights to its implementation.

**Illegal or unauthorized alteration of CALF is prohibited.** The distribution policy does not permit reverse engineering, decompilation, disassembly, binary patching or modification of the proprietary CALF runtime. Violations may result in legal action under applicable law. Free use does not grant permission to extract, modify or redistribute a modified core.

Extensions are provided through official **SDK, adapter and MCP** interfaces, without modifying the core. **Available interfaces:** provider and check adapter specifications with explicit limits, the local JSON task interface and the source-reader MCP and optional-control Universal Work MCP. **Developer SDK 0.2.2 is now available separately:** [English guide](SDK_README.md), [한국어 안내](SDK_README_KR.md), and [download](https://github.com/VibePakcr/CALF/releases/download/sdk-v0.2.2/CALF-SDK-0.2.2.zip). Verified on macOS ARM64, Windows x64 and Linux x64. SDK source is supplied under its integration license; the CALF core remains private.

These restrictions concern the proprietary CALF implementation, not the user's own project code or supported configuration and extension interfaces. Bundled third-party components retain their own licenses and notices in `THIRD-PARTY-NOTICES.txt`.

| Edition | Version | Use |
|---|---|---|
| **Harness** | [1.8.8](https://github.com/VibePakcr/CALF/releases/tag/v1.8.8) | Native headless tasks and existing Codex / Antigravity hooks; no WebView |
| **Workbench** | [1.9.3](https://github.com/VibePakcr/CALF/releases/tag/v1.9.3) | Rust + Tauri desktop for the same execution core and new task records |

**Start with the illustrated [CALF_mannual.html](https://raw.githubusercontent.com/VibePakcr/CALF/main/CALF_mannual.html)** — download and open locally. It includes fixed top navigation and an **EN / KR** switch for the full manual, contents and screenshot captions. Each package retains its version’s offline manual; the link above provides the latest wording revision. See [release notes](RELEASE-NOTES.md) and [SHA256SUMS](SHA256SUMS).

## Downloads

| Platform | Harness 1.8.8 | Workbench 1.9.3 |
|---|---|---|
| macOS Apple Silicon | [ZIP](https://github.com/VibePakcr/CALF/releases/download/v1.8.8/CALF-Harness-1.8.8-macos-arm64.zip) | [ZIP](https://github.com/VibePakcr/CALF/releases/download/v1.9.3/CALF-Workbench-1.9.3-macos-arm64.zip) |
| Windows x64 | [ZIP](https://github.com/VibePakcr/CALF/releases/download/v1.8.8/CALF-Harness-1.8.8-windows-x86_64.zip) | [ZIP](https://github.com/VibePakcr/CALF/releases/download/v1.9.3/CALF-Workbench-1.9.3-windows-x86_64.zip) |
| Linux x64 | [tar.gz](https://github.com/VibePakcr/CALF/releases/download/v1.8.8/CALF-Harness-1.8.8-linux-x86_64.tar.gz) | [tar.gz](https://github.com/VibePakcr/CALF/releases/download/v1.9.3/CALF-Workbench-1.9.3-linux-x86_64.tar.gz) |

Extract the complete package. Open **CALF Workbench.app**, `calf-terminal.exe`, or `./calf-terminal` for the desktop. Run `./calf --help` or `.\calf.exe --help` for Harness. The simple task workflow discovers supported unittest, pytest, Cargo or node:test checks; your project check tools remain separate prerequisites.

```sh
./calf task connect codex
./calf task run "/absolute/path/project" "Fix the bug and preserve the tests."
./calf task list
```

New headless tasks and Workbench share `CALF_WORK_HOME`. Existing 1.8.4 hook `history.html`, contracts and settings are preserved; legacy hook history is not automatically imported into the Workbench task list. Upgrade hooks using the same installation root and retain old versioned binaries.

Workbench provides Task Flow, Git Graph, Diff, Evidence, Light Edit, detected/manual external editors, worker terminals and explicit local references. Git observation is read-only. The interface defaults to English with Unicode/CJK text support.

These are early public **binary** releases, not a published core source repository. Registered evidence defines the scope of PASS; missing or stale evidence stays UNKNOWN. CALF does not replace host approval or sandbox policies. Remote AI use still sends the selected task context to the provider.

macOS 14+ ARM64; Windows x64 with WebView2 for Workbench; Linux glibc x64 with GTK 3 / WebKitGTK 4.1 for Workbench (Debian 13 tested). No Intel Mac, ARM64 Windows/Linux or musl build is included. macOS has an ad-hoc integrity signature, not Apple notarization; Windows has no publisher signature. Read the exact qualification limits in the release notes.

한국어 설명: [README_KR.md](README_KR.md).

Legacy hook release: [CALF 1.8.4](https://github.com/VibePakcr/CALF/releases/tag/v1.8.4).

## Check Profiles and update-safe tasks

Both editions now use native Check Profiles for Python unittest, pytest and a bounded Cargo integration-test profile. CALF records pre-existing failures, separates test failures from missing tools or invalid evidence, and stops repeated attempts that make no measurable progress. A pre-existing failure is not a waiver: unresolved required checks cannot become PASS.

Python selection prefers the project's `.venv`, then `venv`, an explicitly active environment, and finally a bounded PATH probe. The selected interpreter and installed package metadata are recorded with the check. CALF does not install Python, pytest or project dependencies. A broken explicit environment is reported instead of silently selecting another one. Cargo currently covers a single package's integration tests with locked, offline execution; it does not claim workspace-wide, unit-test or doctest coverage.

New queued tasks retain a hash-verified copy of their originating runtime in the local records home. After an update, Resume uses that runtime and the original task's checks and evidence. Keep the complete records home and its `runtimes` directory. Old jobs without a provable runtime remain unresolved; they are not silently migrated. Direct advanced `calf run` states still require their original compatible runtime.

**SDK 0.2.2** provides `CalfClient.discover_checks()` and `Check.from_discovered()` to preserve native profile definitions in custom adapters. See [SDK guide](SDK_README.md), [protocol](SDK_PROTOCOL.md) and the included `examples/check_profiles.py`. The SDK provides small Python standard-library and dependency-free Node clients; it does not add an agent engine or background service.

[Update details / 업데이트 내용](UPDATE.md) · [Universal Work SDK / 범용 작업 SDK](SDK_WORK_PROTOCOL.md)

<!-- workbench-gallery:start -->
## See the Workbench

Real Workbench 1.9.2 captures; only OS title-bar chrome is cropped. [Capture context and verification scope](SHOWCASE.md).

### Task Flow · execution and evidence

![Task Flow · execution and evidence](workbench-task-flow.png)

Workbench 1.9.2 opens a retained, real Codex invoice example: three baseline failures resolved and six registered tests passed. The original run used Harness 1.8.6; this is a record-compatibility demonstration, not a new AI benchmark.

### Diff · the exact checked change

![Diff · the exact checked change](workbench-diff.png)

Before / After shows the recorded change and its matching CHECK receipt. Light Edit and external-editor controls remain separate from validation.

### Runtime Work · file artifacts across runtimes

![Runtime Work · file artifacts across runtimes](workbench-runtime.png)

A Python adapter produced a CJK document in the retained 1.9.2 example. A separate check verified the exact UTF-8 content. The adoption record refers to the same file manifest. The same adopted record was verified after reopening Workbench.

<!-- workbench-gallery:end -->

## Free Repository Navigator extension

**Repository Navigator 0.1.0-dev.1** is a free, optional download for exploring Local Git and manually registered GitHub.com / GitLab.com repositories through one relationship map, descriptions, code and Diff view. It runs with Python 3.10+, Git 2.43+ and a modern browser; the CALF core, SDK and models are not required.

- **Preview download and checksums:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/releases/tag/navigator-v0.1.0-dev.1) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/releases/navigator-v0.1.0-dev.1).
- **Screenshot manuals:** [English - 9 chapters, 6 screenshots](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/README.md) · [한국어 - 9개 장, 실화면 6장](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/README_KR.md).
- **English PDF:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/en.pdf) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/en.pdf).
- **한국어 PDF:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/ko.pdf) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/ko.pdf).

The ZIP includes both offline HTML/PDF manuals. See [extension qualification and limits](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/NAVIGATOR_PACK_VERIFICATION.json) for the installed preview scope.
