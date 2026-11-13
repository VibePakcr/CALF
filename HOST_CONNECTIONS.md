# CALF host connections

[한국어](HOST_CONNECTIONS_KR.md) · [Native host kit](hosts/README.md)

CALF supervises one agent working in Codex, Antigravity or Claude Code. Each host
keeps its own account, model, approval rules and settings. The current adapters
use the shared Rust core; no extra agent, local model or resident service is
needed. Ordinary Claude chat, Cowork and cloud Code sessions are separate modes.

Use the **host kit included with the exact core package**. Follow its
[installation guide](hosts/README.md) or [Claude guide](hosts/claude/README.md).
Older kits may contain a Python adapter; keep them with their original version
rather than mixing old adapter commands with a newer core.

Inspect an existing managed installation first. Keep the same root, retained
binaries and state. Apply only the reviewed CALF hook definitions. New Codex
commands need normal /hooks trust review; Antigravity and Claude retain their
own execution approval. A new session is needed to verify the selected route.

A configured route, protocol test, native-core test and actual AI session are
different evidence. Check the release verification report for the exact OS and
host mode. Windows/Linux core qualification does not by itself qualify every
host application on those systems. Likewise, a prompt-bearing event can attach
local engineering references only when that feature is present in the selected
core and the correct CALF_WORK_HOME is supplied to that process.

A tool process exiting normally is not task completion. Registered checks must
match the current files and execution context. If a host denies a command,
retain the denial and use its ordinary approval flow. Do not weaken checks,
add blanket allow rules or treat historical PASS as a current verdict.

Inspect any local reference collection before running an AI task: selected
references may be sent to the connected provider as task input. Read-only
knowledge and Repository MCP queries themselves make no AI calls. Extension
packs do not automatically replace the native core or update host hooks.
