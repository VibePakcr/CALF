# CALF Harness 1.8.25 · Workbench 1.9.24
<!-- calf:current-release:start -->
harness: 1.8.25
workbench: 1.9.24
sdk: 0.2.11
Release channels: GitHub / GitLab
<!-- calf:current-release:end -->

## Workbench 1.9.24 — follow work and review interruptions

Switch between **Flow** and **History** for the same recent verified steps. The task request, recorded state and available state explanation stay together. Select a step to inspect its record and operation details; use **Task evidence** for current validation.

**Review requests** opens Attention. **Needs review**, **Observation gaps** and **All observed** filter the same bounded native observation. Cards separate the historical outcome from current completion, show freshness, and expose the recorded evidence reference. Open a task to inspect it before taking an existing review action.

This is a view over existing records. It adds no execution engine, task database, automatic approval, remote approval or host-task control. Earlier records and pinned runtimes remain intact. Harness 1.8.25 and SDK 0.2.11 are unchanged.

Upgrade from Workbench 1.9.23 through Updates, or extract 1.9.24 into a new folder and keep your existing records home. [Screen guide](WORK_STATE_VIEW.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#work-state).

## Previous releases / 과거 릴리즈


## 1.8.25 / 1.9.23 — incident evaluation, adversarial review and event resume

Historical incident packets exclude answers and future evidence; scores separate diagnosis from handoff usefulness. Adversarial review binds support, counterexamples and alternatives to actual current native CHECKs. Opt-in local events resume one bound managed task, reject duplicate/stale events and retain uncertain interrupted execution for review. Existing records, contracts, settings and pinned task runtimes remain intact.

Host audit logs now rotate before a new record would exceed 64 MiB. The previous bytes remain in cold segments with their size and SHA-256 receipts. Writers share an OS lock, and an audit write failure leaves the event unacknowledged for retry.

Use `calf evaluation` and `calf events` through the CLI or common API. [Usage and fields](WORKFLOW_HARDENING.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#workflow-hardening). SDK 0.2.11 is unchanged.

Upgrade from Workbench 1.9.22 through Updates or extract 1.9.23 into a new folder. Keep the original records home and pinned task runtimes. Linked host tasks continue in their original host.

## Previous releases / 과거 릴리즈

# CALF Workbench 1.9.22

## Workbench 1.9.22 — connected task status

Open a card under Connected tasks to read that exact host task. You can do this before choosing a workspace. Refresh status reads the same selected task again.

If the task is missing from a bounded or recently changed task list, Workbench retains its identity and requests that task directly. If its link is no longer readable, the view shows an error instead of displaying another task’s result. Check the existing host connection, then refresh; no restart is needed for this read-only view.

“Response ended” describes a recorded host event. It does not establish process liveness or completion of the whole task. UNKNOWN stays unknown when current completion has not been evaluated.

Sidebar utility panels occupy the central work area. Close or Esc returns to the task view. Switching between panels retains an unsaved preferences draft; Save preferences is the explicit save action.

Upgrade from Workbench 1.9.21 through Updates, or download 1.9.22 and extract it to a new folder. Keep your existing records folder, contracts, preferences and pinned task runtimes. Preparing the update leaves the current window running. Existing linked tasks continue in their original host.

## Previous releases

# CALF latest update

Under Patch 2026-11-19 adds Rust read-only model/skill label evaluation, checkpoint-bound lane failure/time/usage accounting and explicit unknown cost coverage. Local planner replies retain strict validation for nullable expected hashes. Versions remain Harness 1.8.24, Workbench 1.9.21 and SDK 0.2.11. Existing records, contracts, settings and task runtimes are retained. [Usage and measured pilot](ROUTING_EVALUATION.md)

Linked task status: Long linked conversations continue to follow the latest response without deleting old records or changing connection settings.

Under Patch 2026-11-17 adds opt-in native operation delegation between a trusted Mac broker and a separately provisioned Linux host: a fixed repository read, exact ticket, local confirmation, single-use authority and minimal results. Existing records, contracts, settings and task runtimes are retained. [Usage and scope](CALF_mannual.html#operation-delegation)

Under Patch 2026-11-16 · version numbers retained. The [model specification](ONTOLOGY_MODEL.md) and [JSON](ONTOLOGY_MODEL.json) define objects, common/variant properties, relationship domain/range and enforcement points. Native validation and public descriptions share field definitions. Every append path rejects reviving a retracted record. Stored format, contracts, settings and task runtimes are preserved.

Harness **1.8.24** · Workbench **1.9.21** · SDK **0.2.11** unchanged.

Read-only task evidence graphs, historical search and paging, reference navigation, and direct/indirect impact explanations. Existing records, contracts, settings and task execution are preserved. [Guide](ONTOLOGY_GUIDE.md)

## Earlier updates / 이전 업데이트


Connected task cards and Task status read explicitly linked Codex CALF journals and follow the latest response within the same session. They never execute, stop or restart host work. Committed records remain readable during writer contention; unavailable current validation stays unknown.

Historical results and current validation remain distinct. Unregistered completion criteria retain UNKNOWN; a response ending does not mean the whole work program completed. Existing records, contracts, settings, pinned runtimes and SDK 0.2.11 are preserved.

## Earlier updates / 이전 업데이트

# CALF latest update



Utility views now occupy the central work area, keeping underlying task buttons out of the view. Close controls, keyboard navigation, small windows, empty folders and update actions have been polished.

Task status reads the retained records for the selected folder and the task’s original runtime. Recorded and current observations remain distinct; unavailable details remain explicit. Existing records, contracts, settings and retained task runtimes are preserved. SDK 0.2.11 is unchanged.

## Earlier updates / 이전 업데이트

# CALF latest update



Choose a correction from earlier tasks for the next request. Add and undo affect the draft only. The title and Close stay visible while the contents scroll. [Actual screens and steps](REQUEST_GUIDANCE.md).

Existing records, contracts, settings and required checks are retained. SDK 0.2.11 and extensions are unchanged.

## Earlier updates / 이전 업데이트

# CALF current patch



Harness **1.8.20** · Workbench **1.9.17** · SDK **0.2.11** unchanged.

Built-in references work immediately. One folder choice checks, indexes and connects personal Markdown/text material. Existing selections, task records, contracts and settings are retained. [Engineering material guide](ENGINEERING_KNOWLEDGE.md).

## Previous published release

# CALF — personal workflows



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
