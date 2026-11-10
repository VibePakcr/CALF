# CALF MCP contract and tool evaluation: implementation audit

Program: `CALF_MCP_ADAPTER_CONTRACT_AND_TOOL_EVALUATION_PROGRAM`

Audit date: 2026-11-10

Source: the existing mutable `CALF-tauri` working tree, native development version **1.9.7**. This is not the public 1.9.6 release or a new production deployment.

## What the source actually provides

| Existing contract | Evidence in this working tree | Decision |
| --- | --- | --- |
| MCP framing and source access | `native/src/local_mcp.rs`: bounded JSON-lines framing; owned read-only folder resources | Reuse the frame bytes and sender. Keep existing resource behavior. Add duplicate-key rejection only to the new contract/mediation path. |
| Universal Work MCP | `native/src/work_mcp.rs`: read-only by default; explicit control; frozen WorkSpec execution through `work::api` | Preserve without rerouting its existing calls. This endpoint does not discover arbitrary third-party MCP tools. |
| Runtime pins, paths, identities | `native/src/work_contract.rs`: `pin_adapter`, `verify_adapter`, `child`, `file_identity` | Reuse. Do not create another executable allowlist or package manager. |
| Native task and completion contract | `native/src/history.rs`, `schema.rs`, `engine.rs`: accepted TASK, hash-chain ACTION/CHECK/DECISION, `begin`/`finish`, current completion | Bind each invocation to the exact accepted TASK envelope. MCP results cannot create CHECK records. Unresolved starts retain the existing completion blocker. |
| Segmented execution journal | `native/src/journal.rs`: append-only HTML, rebuildable SQLite projection, per-run ownership | Preserve. The selected registered-task path already uses `history.html`, so tool events join that existing chain rather than adding another Journal or database. |
| CPU GCN/MCL | `native/src/context_control.rs`: explicit module/cell/lane sets, prerequisites, write owners, native gate evidence | Reuse `guard` for a selected module in a supplied lane. It is a scope check, not execution permission or whole-project PASS. Do not redefine MCL or create workers. |
| Repository Intelligence | `native/src/repository.rs` and `repository_ast.py`: bounded related-file projection; Repository pack supplies separate selective history context | Preserve. No verified mapping currently turns arbitrary MCP capabilities into Repository modules. Automatic mapping remains unimplemented, rather than being inferred from tool descriptions. |
| GCI | No named GCI contract or runtime entry point found in this working tree | Do not invent one. A future binding needs its actual canonical interface. |
| ETS | No named ETS API, event schema or runtime dependency found in this working tree | Reuse native TASK/ACTION history now. Calling that a completed external ETS integration would be inaccurate. A future ETS binding must be checked against its actual contract. |
| Independent existing source repository | This mutable source folder had no Git metadata | Keep all prior files in place. A private local source commit is prepared; no public remote, push, package replacement or installed-host update is part of this program. |

The context launcher returned `UNBOUND` for this workspace. No unrelated project records were searched or treated as instructions. Source and current tests, rather than historical completion text, establish the audit above.

## Added, reused and deferred

**Added:** `tool_contract.rs` for bounded normalization, schema validation, selection and result evaluation; `tool_mcp.rs` for the explicit policy-bound local stdio path; `tool_host.rs` for exact execution intents dispatched by the existing `hosts::execute_owned` entry point. The CLI exposes `tool-contract`, `tool-call`, `tool-prepare` and an optional foreground `tool-mcp`. Test fixture/verification helpers remain under the existing `native/ops` directory.

**Reused:** accepted tasks, task hashes, history writer/CAS and chain validation, native outstanding-execution checks, independent registered checks, pinned runtime identities, physical path helpers, owned process groups, the existing GCN scope guard and MCP framing. No external source, new library, model, service or duplicate ETS is introduced. Existing Work and Local Sources MCP contracts stay in place.

**Connected through existing contracts:** native ticket validation, single consumption and terminal receipts now cover exact host-admitted candidate creation. Preparation grants no authority. The native execution path alone can construct the internal admission value; no JSON approval bit or reserved inner CLI grants writing. Successful writes run all registered independent checks automatically. A typed `mcpArtifact` ACTION binds the validated scope to completion; older cores reject this required extension rather than ignoring it. Existing records remain unchanged.

**Scoped recovery:** a write policy may opt in to `local-artifact-and-native-checks` before execution. A separate host-admitted intent can reconcile the original stopped native invocation from its exact receipt, expected candidate hash, unchanged protected scope and fresh native checks. It never resubmits the tool call or rewrites the original error, receipt or history. Missing/changed receipts, changed candidates, unconfirmed cleanup or explicit cancellation cannot be settled this way. A timeout alone establishes nothing.

**Still unverified:** an independently signed human-consent receipt; general overwrite/delete/external operations; authoritative remote-job reconciliation; GCI/external ETS bindings; automatic Repository module/capability mapping; and qualification of this new path on Windows/Linux or another transport. The owner explicitly selected the currently verified GCN/MCL and native record boundaries after the missing named GCI/ETS interfaces were reported. No replacement interfaces are invented.

**Deferred until P0/P1 is complete:** evaluation caches, automatic contract-impact analysis and broader context-budget optimization. Current processing is CPU-only, bounded, on demand, and uses one executor. No daemon or local model is needed.

## Initial completion classification

The overall program remains **FOUNDATION_READY**. The narrower macOS local stdio profile can be reported as **INTEGRATION_VERIFIED** only with its attached final execution evidence. This is not an all-provider, all-transport or all-OS PASS.

The profile includes MCP-to-mediator-to-MCP reads, preparation without dispatch, actual host execution of a new candidate, independent checks, exact-version completion binding, duplicate/expired/tampered-intent rejection, contract drift, GCN write ownership, missing/foreign/tampered receipt rejection, actual interruption, timeout/disconnection and post-execution journal-failure recovery without resubmission. The verification summary distinguishes fresh final-core tests from earlier trials. A first deadline failure is retained: a sender could start after the connection budget expired. The corrected transport checks the budget before creating the writer and again before sending; an expired-pipe test proves zero bytes were sent. A separate retained reproduction found that the native cancellation marker reached the outer terminal receipt but not the new inner execution. The corrected path passes that existing cancellation condition into response waiting and independent checks, without an additional service. Actual response-phase and check-phase cancellation cases must both remain UNKNOWN.

A tool declaration is untrusted data. A local policy or native ticket is not proof that a human clicked an approval button: the caller must already have authority under its host/OS rules. The host may allow or deny the prepared command through its existing flow. CALF adds no permission, persistent allow rule or approval engine. Even the read path starts a locally reviewed pinned process with that host's permissions. This code does not install an OS filesystem/network isolation boundary or control an independently launched process. Post-call snapshots can detect lasting changes within selected scope; they cannot establish that no transient or out-of-scope side effect occurred.

## Required evidence before raising the classification

1. If independent human-consent attestation is required, bind a real host-provided approval contract. Native execution admission must not be relabelled as such an attestation.
2. For broader side effects or remote jobs, define the domain's authoritative query/cancellation and reconciliation contract before enabling retries. Keep the first error, candidate and consumed attempt.
3. Bind canonical GCI/ETS interfaces only if they actually exist and become available. Keep native event identity and completion authority; the current owner decision does not establish those missing interfaces.
4. Qualify each additional OS, transport and effect profile with real execution, interruption, reconciliation and regression evidence.

Overall completion must state the supported profile and unresolved items explicitly. Local candidate recovery is not evidence of remote-job recovery or general destructive-operation support.

## Cross-platform release qualification — 2026-11-10

The initial implementation audit above remains provenance for the 1.9.7 development source. Harness 1.8.12 and Workbench 1.9.8 now qualify the same local stdio profile on macOS ARM64, Windows x64 and Linux x64 (Debian 13). Each edition/OS combination passed 11 read groups and 14 execution/recovery groups. SDK 0.2.5 passed 17 boundary tests per OS and actual native policy preparation with Python/Node descriptor agreement. Preparation dispatched zero requested tool calls.

The release verification JSON supersedes the initial macOS-only qualification status. This adds no canonical GCI/ETS contract, remote provider settlement, destructive tool authority, human-consent signature or general OS sandbox. Overall program classification remains FOUNDATION_READY; INTEGRATION_VERIFIED applies to the explicitly tested local profile. The existing native runtime source matches the prior 66-test suite; edition/version metadata changed separately.
