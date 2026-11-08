# GCN/MCL in the CALF core

[한국어](GCN_CORE_KR.md)

GCN (Group Coordination Node) and MCL (Merge and Coordination Layer) now run in the shared Rust core: **Harness 1.8.9 / Workbench 1.9.4**. This is a preview. Existing stable downloads and earlier runtime paths remain available.

An extension describes cells, their dependencies, file ownership and required checks. CALF orders the selected cells and checks their current native evidence. **One agent remains the executor.** Coordination runs locally on the CPU, on demand.

## What belongs where

| Component | Responsibility |
|---|---|
| CALF native core | Validate the plan, order prerequisites, detect conflicting write owners and evaluate current native check evidence against the cell's file scope |
| Repository pack | Discover a registered project, select module references and retrieve exact original records |
| Host | Apply its existing tool permissions and run the work |

The native gate currently uses **native v1 TASK/criterion records**. Its record workspace must be the same physical project as the declared files. A passing check for another scope cannot make the cell ready. Changed files, missing checks and unresolved prerequisites leave it in `WAIT`. `READY` describes the declared checks; completion and adoption still follow the work contract.

Other domains can supply cell plans and native check bindings through this interface. Media providers and additional record formats need their own integration and qualification.

## Try the preview

1. Extract the new native package into a new folder. Keep your existing records home, contracts, settings, previous binaries and task runtimes.
2. Download the [Repository context pack](https://github.com/VibePakcr/CALF-Extensions/releases/tag/repository-v0.1.2-preview.5) separately. Follow its [project registration guide](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/REPOSITORY_CONTEXT.md), selecting the new native executable.
3. Register each project's history, module map and lane plan once. The context CLI then discovers that registration from the working directory. Use the complete installed CLI prefix, or a local wrapper created during setup, in the host's startup instruction.
4. Use `resume` to retrieve the selected lane, exact declared references, recent metadata and current gate in one call. Unregistered projects return `UNBOUND`.

Installed supervision hooks keep their existing pinned runtime. The local qualification retained the 1.8.8 hooks and added a versioned 1.8.9 GCN context runtime. Changing a host's hook definitions or trust remains a separate host operation. The existing Host Connections 1.8.8 companion remains version-specific.

Download and open the [illustrated manual](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF_GCN_manual.html) locally. It covers the native packages with an EN/KR switch. Existing screenshots retain their original capture labels.

## Common interfaces

```text
calf gcn < request.json
calf api < envelope.json
```

An API envelope is `{"op":"gcn","request":REQUEST}`. Workbench and the SDK may also attach their standard absolute `home` field. GCN validates that field without creating or changing that records home.

Python SDK **0.2.2** works through its existing generic call:

```python
result = client.call("gcn", request=request)
```

The Workbench native bridge exposes `gcn` with a `request` argument. All paths use the same native policy. The request operations are `validate`, `project`, `guard` and `gate`; callers supply a plan and module IDs, plus the lane and project identities needed by the operation. A caller-supplied verdict or executable command is rejected.

Limits: 64 cells, 16 lanes, 16 cells in an expanded lane, 64 KiB input and 256 KiB native output. Repository `resume` limits its response to 64 KiB, with at most eight 2 KiB reference excerpts and five recent metadata entries per selected module. Pending or truncated references are explicit. Native integrity checks may still read the complete journal.

## Verification and limits

macOS ARM64, Windows x64 and Debian x64 passed real native `WAIT → READY → WAIT` checks, wrong-file-scope refusal, both API envelope forms and the Workbench native bridge. Existing SDK generic calls were checked on macOS. The bridge qualification is a native self-check; it does not claim a new window-interaction test.

Fresh Codex and Antigravity sessions found the actual registered project without query paths in the user prompt. Claude also recovered the exact original references in one `resume` call; its final report used two equivalent labels that failed the temporary driver's strict string format. That failure and the separate functional review are retained.

The 938 existing history prefixes were preserved. Existing model, hook and approval values were retained. Codex native `thread/start` persisted a new project trust entry. A model-free, hook-free isolated replay reproduced that write. It is recorded separately from display preferences. Antigravity app metadata also changed; complete task-start bytes were unavailable for that file, so whole-app-state preservation is not claimed. No original settings were restored and no preservation baseline was advanced.

See [release notes and exact scope](GCN_RELEASE.md) and `GCN-VERIFICATION.json`. The core remains free to use and closed-source. SDK, adapter and MCP extensions use the supported interfaces under their existing licenses.
