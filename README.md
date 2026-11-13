# CALF

**Controlled Agent Lifecycle Framework**

Keep track of the work you give your AI. CALF brings your request, changed files and check results together, so you can review the result and continue work that stopped.

Use it with Codex, Antigravity or Claude Code. CALF is built with Rust and Tauri and is free to use on macOS, Windows and Linux.

[Website](https://calf.vibepackr.com/en/) · [Download](https://calf.vibepackr.com/en/#downloads) · [Install](INSTALL.md) · [Manual](https://calf.vibepackr.com/manual/?lang=en) · [한국어](README_KR.md)

## Start with Workbench

1. [Download Workbench for your OS](https://calf.vibepackr.com/en/#downloads) and extract it to a new folder.
2. Open the app, choose your project folder and connect the AI you already use.
3. Describe what you want done and what to keep unchanged. Follow the guide to check that your project tools are ready, then submit the task.

The [installation guide](INSTALL.md) and [illustrated manual](https://calf.vibepackr.com/manual/?lang=en#start) walk you through each step.

![Workbench 1.9.16 first-task guide](ui-macos-first-task.png)

The first-task screen in Workbench 1.9.16. See the [Windows and Linux screens](UI_GUIDE.md) too.

## Material connects automatically

Built-in references need no setup. To add your own material, choose a Markdown or text folder once in **Engineering knowledge → Add a material folder…**. CALF checks the files, builds a search index and connects new tasks. [Read the guide](ENGINEERING_KNOWLEDGE.md).


## What you can do

- **Review changes.** Open Diff to see which files changed and the checks run for them.
- **See what needs attention.** Read the current result, earlier records and the next step together.
- **Continue a task.** Keep earlier attempts and use Resume when you are ready to continue.
- **Find useful context.** Look up earlier decisions with Repository Intelligence and browse development references in Engineering knowledge.

Repository Intelligence is included with CALF. GCN/MCL helps organize the order of work, file scope and checks. The Computer Engineering Pack / Pattern / Method catalogue provides 367 reference entries, and you can add your own material.

## Choose how to use CALF

| Use | Choose |
| --- | --- |
| A desktop app for following tasks and reviewing files | **Workbench 1.9.17** |
| Terminal commands, host hooks or MCP | **Harness 1.8.20** |
| Connect your own tools | **SDK 0.2.11** |

Workbench and Harness use the same core. Point them to the same CALF data folder to see the same tasks. Keep that folder and older task runtimes when updating.

[Downloads](DOWNLOADS.md) · [Release notes](RELEASE-NOTES.md) · [Earlier versions](LEGACY.md)

## More help

[First task](FIRST_TASK.md) · [Connect your AI](HOST_CONNECTIONS.md) · [Repository Intelligence](REPOSITORY_BUILTIN.md) · [Development references](ENGINEERING_KNOWLEDGE.md) · [Saved files](ARTIFACT_LIFECYCLE.md) · [Local MCP tools](MCP_TOOL_EVALUATION.md) · [SDK](SDK_README.md)

Local model connections are in preview. See [Ollama and MLX](LOCAL_MODELS.md) before choosing that route.

CALF works on its own. The optional [FFmpeg extension](https://github.com/VibePakcr/CALF-Extensions) helps manage video work. [CALF Connect](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/INSTALL.md), a development preview, opens Workbench from VS Code, Cursor, PyCharm or Antigravity IDE.

## Use and licence

CALF is free to use. Its core source is not published and CALF is not an open-source licence grant. Unauthorised modification, tampering, reverse engineering or redistribution may lead to legal action under the applicable terms and law. Use the separately provided SDK, adapters and MCP interfaces for extensions; their own licence applies. See the licence files supplied with each package. Connected AI services retain their own fees and terms.

## How CALF fits together

![CALF architecture — English](calf-overview-en-20261111.png)

![CALF 구조 — 한국어](calf-overview-kr-20261111.png)
