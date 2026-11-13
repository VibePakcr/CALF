# CALF — personal workflows

<!-- calf:current-release:start -->
harness: 1.8.19
workbench: 1.9.16
sdk: 0.2.11
Release state: published
<!-- calf:current-release:end -->

Harness **1.8.19** · Workbench **1.9.16** · SDK **0.2.11** (unchanged).

Work attention now keeps unresolved effects visible after cancel/pause requests, reports missing runtime/evidence as unknown and bounds observation without returning a false all-clear. [Attention changes](WORK_ATTENTION_HARDENING.md). The optional [CALF Connect](https://github.com/VibePakcr/CALF-Extensions/tree/main/ide-connect) opens Workbench and reads attention from four IDEs; its [manual](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/MANUAL.md) contains actual screens across three operating systems.

## Previous release: engineering references


Harness **1.8.18** · Workbench **1.9.15** · SDK **0.2.11**.

The shared Rust core adds bounded engineering references, local full-text import, frozen task context and a Workbench knowledge panel. The built-in starter has 367 references; the private 4,334-document qualification dataset is not included. [Engineering guide](ENGINEERING_KNOWLEDGE.md) · [Local model preview and limits](LOCAL_MODELS.md).

Windows and Debian passed actual import, resume, repair and independent checks with deterministic providers. A real Codex-connected Mac task passed its registered checks and a separate review. Local Qwen MLX/Ollama trials were stopped by unchanged resource guards; completed-task support for these models is not qualified. No new model is required by CALF.

## Previous published release


This guide covers Harness 1.8.17, Workbench 1.9.14 and SDK 0.2.10. Verify the published release and your installed version separately. Use the [latest public release](https://github.com/VibePakcr/CALF/releases/latest) for the current distributed version.

CALF remains free to use on its own. Connected AI services keep their own accounts, fees and approval rules. VibePackr is optional; CALF does not require an organisation account or upload your history in the background.

## From first request to result

The five-step guide helps you choose a folder, connect your AI, describe a useful result, find the folder’s checks and review a result. Check discovery does not run or pass tests. Existing task contracts and completion rules still apply.

**Shape your request → My saved outlines** stores up to eight named outlines on this device. Load them only when needed. An outline fills an empty helper form, leaving your request draft alone. Review it before adding it to the request. Saving and removal append to the existing personal journal; earlier records and working-style preferences remain intact. A new task always needs its own checks.

When a task stops, the next-step hint points to its evidence, AI connection, retained runtime or failed checks. It does not retry work, grant permission or mark it complete.

## Export a task summary

Open a task’s **Result summary → Export task summary**. Preview the exact JSON, then choose **Confirm local export**. Nothing is uploaded. Source contents, file paths, configuration and original evidence files are excluded. Request text is excluded unless you select it; review it for private information before sharing.

The summary contains a checkpoint, contract digest, up to 32 record references and the recorded outcome. Its current verdict is always `NOT_EVALUATED`. The digest detects an inconsistent document; it is not a signature, proof of origin or a current completion certificate. Changes after preview require another preview. Export never overwrites an existing file.

The SDK exposes `release_info`, `request_templates`, `handoff` and `validate_handoff`. See `examples/task_handoff.py` for a local preview. A receiving VibePackr integration must validate this input and apply its own work contract, authorisation, original-evidence requirements and current checks. No VibePackr endpoint is assumed, and no live enterprise import is claimed by this release.

## Installation checks

macOS ARM64 requires macOS 14 or newer. Distribution signing and notarisation must be verified on the final bundle. Windows x64 requires WebView2; publisher signing is a separate release check. Linux x64 requires GTK 3 and WebKitGTK 4.1; Debian 13 is the currently qualified distribution. These requirements do not guarantee every OS configuration.

Existing releases, task runtimes, records, contracts and settings are retained. Publishing a release does not automatically update another user’s app or host hooks.

Task Flow runs from left to right in observed execution order. The **Work / Checks / Repair / retry** lanes identify phase categories, and their labels stay visible during horizontal scrolling. Vertical position does not indicate success or importance; node spacing is not proportional to duration.


## Workbench 1.9.14: monitor and sidebar update

Mint usage bars and values now sit on thin unused tracks. CPU shows its detected total and three busiest cores. The left panel scrolls independently to its bottom menus and version. Qualified on macOS, Windows and Debian; earlier packages and records are retained. Harness 1.8.17 and SDK 0.2.10 are unchanged. [English details](MONITOR_UI_FIX.md) · [한국어](MONITOR_UI_FIX_KR.md).
