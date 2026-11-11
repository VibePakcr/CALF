# CALF native host connections

[한국어](CLAUDE_CONNECTION_KR.md)

Harness 1.8.15 and Workbench 1.9.11 supervise one agent in Codex, Antigravity or local Claude Code. Accounts, models, command permissions and unrelated hooks remain with each host. No additional model, daemon or local LLM is required.

Codex and Antigravity use `calf install` and the existing native hooks. Codex requires its normal `/hooks` review when a command changes. An existing T9 or other owner-managed protection bridge must be preserved; do not silently replace it with a second route.

## Claude Code

The lifecycle adapter and versioned setup/update/recovery are now Rust commands in the native core. Python is not needed for this connection. Ordinary Claude chat, Cowork and cloud sessions are separate modes.

```sh
/absolute/calf install --root /absolute/native-calf --no-hooks
/absolute/calf host prepare --root /absolute/claude-kit --revision 1.8.15-hosts.1 --core /absolute/calf --config /absolute/native-calf/config.json
/absolute/calf host inspect --settings /absolute/claude/settings.json
/absolute/calf host apply --root /absolute/claude-kit --revision 1.8.15-hosts.1 --settings /absolute/claude/settings.json --expected-sha256 HASH_FROM_INSPECT
```

Use physical absolute paths and run `prepare` with that exact selected core executable. For a durable installation, use the versioned binary returned by `install` for subsequent commands. A new revision is stored beside earlier revisions. `apply` backs up the exact original settings and retains permissions, MCP entries and unrelated hooks. It refuses an unmanaged existing CALF route; migration of such a route needs an explicit comparison, not a second installation over it. Restart the host session after selecting an updated connection.

To select a retained revision, apply that revision with the current settings hash. To inspect an interrupted apply, use `calf host recover --root STORE`, then add `--acknowledge OPERATION_ID` only for a confirmed before/after state. Recovery does not rewrite settings or run work. Unrecognised changes remain UNKNOWN.

## Execution and evidence

The adapter forwards a denied call or a rewritten registered check input, never a native permissionDecision=allow. Claude's own approval flow stays in charge. A complete PostToolBatch can resolve a matching non-check call without claiming it executed. A registered check requires its real owned-process terminal and matching file versions. Never-started owned checks can be cancelled without launching their command; claimed or ambiguous executions remain UNKNOWN.

Synthetic protocol tests are separate from actual AI/app sessions. Read the release verification report for the tested OS and scenario. Earlier actual desktop sessions remain historical evidence; a new binary build does not prove that a running app reloaded it.

Repository context, its read-only Local MCP server and CPU GCN/MCL connection are built into the core. The only current optional extension is FFmpeg. Earlier connections, records, contracts, settings and task runtimes are retained.
