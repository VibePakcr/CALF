# CALF host connections — 1.8.7–1.8.14 / Workbench 1.9.10

[한국어](README_KR.md)

Use CALF to supervise one agent working in Codex, Antigravity or Claude Code. Each host retains its own account, model, permissions and settings. Connect one agent to a work item at a time. No additional model, background service or local LLM is required.

## Choose the connection

| Host | Connection | Verified host sessions |
|---|---|---|
| Codex | Native CALF hooks; review them in `/hooks` | macOS, real new Codex session, 8 independent checks, `SATISFIED` |
| Antigravity | Native CALF hooks; existing compatibility bridge may remain | macOS, real new ACP session, 8 independent checks, `SATISFIED` |
| Claude CLI and desktop local Code | Python hook adapter to the selected 1.8.7–1.8.14 / Workbench 1.9.10 engine | macOS CLI and desktop Code, 8 independent checks, accepted Stop and saved session |

These host-session results are separate from the released native core's Windows/Linux qualification. The Claude adapter uses POSIX locking and is qualified here only on macOS. Ordinary Claude chat, Cowork and cloud sessions are separate products/modes.

## Codex and Antigravity

Use the existing native installer from the [CALF download](https://github.com/VibePakcr/CALF/blob/main/DOWNLOADS.md). It retains versioned binaries, backs up settings and preserves unrelated hooks. Follow the included installer guide. Keep the same installation root for updates. If an existing managed installation lives elsewhere, inspect it first; do not add a second CALF route over it.

Use explicit host homes when testing an installation. Codex requires the normal `/hooks` review for new commands. Antigravity retains its own execution approval and sandbox rules. Starting a new session loads the selected connection; an already running session is not proof that it reloaded.

## Claude on macOS

The local kit includes `hostkit.py` and `claude/adapter.py`. It adds only CALF's nine lifecycle hooks. It never adds an allow rule or edits the desktop UI configuration. Python 3.10+ is required for this adapter, in addition to the native core. [Adapter behavior and limits](claude/README.md).

Choose physical absolute paths for a native installation, a separate host-kit state folder, the Python executable and the existing Claude settings JSON. If the settings path is a symlink, select its actual target; the tool refuses to replace symlinks. Backups may contain private settings: keep the state folder private and out of shared repositories.

First install the native engine without changing hooks:

```sh
/path/to/calf install --root /path/to/native-calf --no-hooks
```

Use the versioned executable path returned by that command and its `config.json`:

```sh
python3 -B hostkit.py prepare --root /path/to/claude-calf --revision 1.8.14-hosts.1 --core /path/to/native-calf/versions/VERSION/calf --config /path/to/native-calf/config.json --python /physical/path/to/python3
python3 -B hostkit.py inspect --settings /physical/path/to/claude/settings.json
python3 -B hostkit.py apply --root /path/to/claude-calf --revision 1.8.14-hosts.1 --settings /physical/path/to/claude/settings.json --expected-sha256 HASH_FROM_INSPECT
```

The settings JSON must already exist. For a new Claude profile, create an empty `{}` file at the location Claude uses, or start Claude once before selecting it. `prepare` writes only a new version inside the chosen kit state folder. `apply` retains the original settings bytes and merges CALF hooks after checking the supplied hash. Existing permission/MCP settings and unrelated hooks remain in the JSON. Review the hooks in Claude and start a new local Code session.

Do not reset an existing CALF hook connection to use this kit. The kit refuses an unmanaged hook command containing `CALF` rather than adding another route. Existing installations can continue using their current routing; a migration needs an explicit review of that connection first.

## Update and recover

Prepare a new kit revision side by side, inspect the current settings hash, then apply the new revision with that hash. To select a retained revision again, use the same `apply` command with its old revision. New non-CALF settings and hooks are preserved. Changed or missing managed hooks stop the operation for reconciliation.

If an apply was interrupted, run:

```sh
python3 -B hostkit.py recover --root /path/to/claude-calf
python3 -B hostkit.py recover --root /path/to/claude-calf --acknowledge OPERATION_ID
```

Recovery compares the settings with the retained before/after hashes. It completes local installation bookkeeping only when one matches. It does not write settings, run work, restore records or choose another model. Unrecognized changes remain `UNKNOWN`. Failed attempts and original backups remain available.

## Confirm actual work

Register an explicit contract with the installed core:

```sh
/path/to/calf register /path/to/work /path/to/contract.json --config /path/to/native-calf/config.json
```

Run the returned registered check command from that work folder through the selected host's normal approval flow. A first local command may need approval, including in Claude Auto mode. Do not use a permanent allow rule unless you intend to save it. The actual native check receipt and matching file versions establish completion; a host's text or exit code does not. Inspect the work's `history.html` and the recorded `SATISFIED`, `VIOLATED` or `UNKNOWN` result.

Existing 1.8.7 macOS model-session evidence is reused for the host behavior above. The kit's separate installation tests cover isolated settings merge, update/rollback, interrupted apply and actual local hook execution. They do not make another model call or claim additional OS host support.

## Local extension packs

The separate Local Pack Tools and Repository inspect preview are qualified on macOS, Windows and Linux. They do not change host hook routing or upgrade the native engine. [Pack release and bilingual guide](https://github.com/VibePakcr/CALF-Extensions/releases/tag/packs-v0.1.0-preview.1). Claude host installation remains macOS-only.

## This connection update

A non-check command denied before execution could remain pending because Claude does not emit `PostToolUseFailure` for that denial. The adapter now uses `PostToolBatch` to match its resolved result by session, turn, tool ID and input. Resolution is not execution success and cannot create a passing CHECK. Registered checks still need their real execution receipt.

An actual macOS Claude desktop Code session used core 1.8.10, ran one registered check with eight passing tests, matched the checked file version and recorded `SATISFIED` at Stop. Auto initially denied that check; it ran after an individual Allow once approval, and the session returned to Auto. This does not establish unattended Auto approval for every command. Release cores 1.8.11 and 1.9.6 receive separate synthetic adapter/installer checks; the live AI session is not repeated.
