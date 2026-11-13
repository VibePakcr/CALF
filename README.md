# CALF

**Controlled Agent Lifecycle Framework**

A lightweight, local-first harness and workbench for one AI agent. CALF keeps a task's request, changes, checks, evidence and recovery in one flow. It supports Codex, Antigravity and Claude Code, with a shared Rust core behind the headless Harness and Rust + Tauri Workbench.

**Free to use · Proprietary binary core · macOS / Windows / Linux**

[Download](DOWNLOADS.md) · [English manual](CALF_mannual.html) · [한국어](README_KR.md) · [Latest update](CURRENT_RELEASE.md)

## Latest release

Harness **1.8.18** · Workbench **1.9.15** · SDK **0.2.11**

Engineering references now live in the shared Rust core. Search the built-in 367-entry starter or explicitly import a local collection, then read only the references needed for the task. The full private qualification dataset is not included. New tasks retain the same selected context when they resume; knowledge never replaces an executed check. [What changed](RELEASE-NOTES.md) · [Knowledge guide](ENGINEERING_KNOWLEDGE.md).

## How it helps

- **Delegate one bounded task.** Keep a single-agent workflow and the host's existing account and approval rules.
- **See the actual work.** Task Flow, Git Graph, Diff, worker output and result summaries connect the request to the files and check receipts.
- **Require evidence.** Registered checks must match the current files and execution context. A normal tool exit or an AI's claim is not completion.
- **Continue safely.** Retained attempts, explicit resume, protected inputs and recoverable artifact quarantine help you continue without discarding prior records.
- **Use focused local context.** Repository Intelligence and engineering references use bounded CPU queries. No extra agent, local model or background indexing service is required.
- **Connect the tools you choose.** Local MCP, adapters and the SDK extend the controlled execution path. VibePackr is optional and CALF works independently.

The optional local model transport remains a preview. Model-list connection is separate from a completed task; read the [Ollama/MLX qualification limits](LOCAL_MODELS.md).

## Harness or Workbench

Use **Harness 1.8.x** for headless CLI, host hooks and MCP integrations. Open **Workbench 1.9.x** against the same CALF data home to inspect those records. Workbench adds a desktop view; it does not introduce a second completion engine. Keep older task runtimes and records when updating.

## See CALF

![Task Flow and execution evidence](workbench-task-flow.png)

![File changes in Diff](workbench-diff.png)

These are earlier released Workbench examples. The current knowledge panel and connection fields are described in the linked guides.

## Guides and extensions

[Getting started](INSTALL.md) · [Host connections](HOST_CONNECTIONS.md) · [First task](FIRST_TASK.md) · [Repository Intelligence](REPOSITORY_BUILTIN.md) · [Artifacts](ARTIFACT_LIFECYCLE.md) · [MCP tool evaluation](MCP_TOOL_EVALUATION.md) · [SDK](sdk/README.md) · [Verification scope](VERIFICATION.json)

Repository Intelligence is built into the core. The separate [CALF Extensions](https://github.com/VibePakcr/CALF-Extensions) repository contains the FFmpeg extension; it is optional.

## Distribution terms

CALF is free to use. Its core source is not published and CALF is not an open-source licence grant. Unauthorised modification, tampering, reverse engineering or redistribution may lead to legal action under the applicable terms and law. Use the separately provided SDK, adapters and MCP interfaces for extensions; their own licence applies. See the licence files supplied with each package. Connected AI services retain their own fees and terms.

## Architecture overview

![CALF architecture — English](calf-overview-en-20261111.png)

![CALF 구조 — 한국어](calf-overview-kr-20261111.png)
