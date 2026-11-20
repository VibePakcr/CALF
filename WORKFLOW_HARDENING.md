# Incident evaluation, adversarial review and event resume

Current guide: Harness 1.8.25 · Workbench 1.9.23 · SDK 0.2.11.

These capabilities use the existing Rust core through the CLI and common API.
Existing tasks are not automatically enrolled. Records, contracts, settings and
pinned runtimes remain intact. The Workbench core exposes the same API; these
operations do not add a new graphical workflow editor.

## Evaluate a historical incident

Send `schema: calf.evaluation.v1`, `op: backtest_prepare` and `case` to
`calf evaluation < request.json`. A case contains:

- `id`, `provenance` (`synthetic` or `source_reported`), `cutoffMs`, `signal`.
- Up to 128 `evidence` entries: `id`, `kind`, `availableAtMs`, `text`.
- `oracle`: `causes`, nullable `onsetMs`, `onsetToleranceMs`, `affected`, `evidenceIds`.

Only `observation` and `code` available by the cutoff enter the investigation
packet. `resolution`, `memory`, `prior_run` and future evidence are excluded.
Give the investigator only the returned `packet`. Keep the case and oracle with
the evaluator and retain `packetDigest` and `caseCommitment`.

For `backtest_score`, supply `case`, `caseCommitment`, `submission`, `access` and
`handoffReview`. A submission has `caseId`, `packetDigest`, `investigatorId`,
nullable `cause`, `onsetMs` and `affected`, `evidenceIds`, and `handoff`.
The handoff has `summary`, `impact`, `uncertainty`, `nextStep` and `evidenceIds`.
Access has `state` (`complete`, `partial`, `unobserved`) and `evidenceIds`.

Cause agreement, onset tolerance, affected-set agreement and required citations
are separate measurements. Missing observations remain null. A correct guess
without required evidence is not a grounded answer. Handoff field completeness
is distinct from usefulness: `handoffReview` is null until reviewed, or contains
`reviewerId`, `handoffDigest`, four 0–4 scores (`clarity`, `impact`, `evidence`,
`nextStep`) and `reason`. The investigator cannot use the same ID to self-grade.

Forbidden access, citations or direct copying of excluded text produce
`EXCLUDED_LEAKAGE`; incomplete access coverage produces `EXCLUDED_ACCESS_UNKNOWN`.
Neither is scored. Access and identity are caller-reported, not authenticated.
Packet construction does not sandbox the host, and direct-copy detection cannot
detect every paraphrased leak. Isolate a real investigator's context and tools
and obtain access evidence separately. A normal score is label agreement, not
certification of model ability.

## Review a diagnosis against real checks

Use `diagnosis_prepare` with `root` and a `plan`. The plan has
`schema: calf.diagnosis-plan.v1`, `task`, the accepted `taskHash`, `hypothesis`,
and `checks` entries containing `criterion`, `role` and `question`.
Every registered criterion must appear exactly once, and all three roles are
required: `support`, `counterexample`, `alternative`.

Freeze the returned `planDigest` before testing. A counterexample check passes
when its proposed counterexample is ruled out; an alternative check tests an
explicit competing explanation. Naming a role does not prove independence or
the meaning of a test. Run the actual checks using the existing `calf check`
or authorized host path. Then send `diagnosis` with the same `root`, `plan` and
`planDigest`. Submitted verdicts cannot replace native CHECK evidence.

| Result | Meaning |
| --- | --- |
| `SUPPORTED_BY_CHECKS` | All registered checks currently support the declared conditions |
| `REJECTED_BY_CHECKS` | A valid check observed a declared condition fail |
| `INCONCLUSIVE` | Evidence is missing, stale, conflicting, incomplete or a tool failed |

Exit 0 means the condition holds; 1 means it does not; other exits are tool
errors. Changed files, context or records invalidate prior support. Review is
read-only and does not rebuild an index. It grants neither completion nor
execution authority and is not a universal causal proof.

## Resume a specific managed job on an event

Use `calf events < request.json` or the common API envelope
`{"op":"events","request":REQUEST}`. Each request has
`schema: calf.event-resume.v1`, `op`, explicit `home` and `task`.

| Operation | Additional input / behavior |
| --- | --- |
| `observe` | Read `viewDigest`, `head`, wait state and digest without writing |
| `arm` | Bind `expectedViewDigest`, `expectedHead`, `subscription` |
| `deliver` | Validate `waitDigest`, `event`; queue only the selected task |
| `dispatch` | Validate delivery and invoke the existing worker for that task only |
| `revoke` | Bind `waitDigest`; revoke the wait and leave the normal pause marker |

A subscription contains `id`, `source`, `subject`, `revision`, `kind`, `ttlMs`.
An event contains `id`, `source`, `subject`, `revision`, `kind`, `occurredAtMs`.
Kinds are `review_completed`, `checks_completed`, `deployment_completed`,
`dependency_ready`. TTL is 1ms–7 days. Events must occur during the registered
wait and not in the future. Commands, arguments and approval fields are rejected.

Arm only a queued, quiescent managed job whose pinned core equals the running
core. Use the exact observation hashes; an absent initial journal has a null
head. Active workers, cancellation, manual pause and unresolved operations block
arming. Read-only linked host tasks are not eligible. Old pinned runtimes are
never silently upgraded.

Waiting workers exit. An authorized local adapter calls `dispatch` when an event
arrives; `deliver` alone needs an explicit worker invocation. Duplicate events
do not requeue or replay execution. Journal transitions precede view changes.
A consumed dispatch without settlement becomes `DISPATCH_UNCERTAIN` /
`needs_reconciliation`, never an automatic retry. Expiry remains `EXPIRED`.
Attention distinguishes normal waiting from expiry and uncertain execution.
Revocation keeps the existing explicit resume and recovery requirements.

Events create no credentials, approvals or authority leases. `source` is a
label, not authentication. This release installs no public webhook listener or
daemon; an external collector must enforce its own authenticated adapter boundary.

## Verification and updating

Release qualification uses isolated native processes, actual checks and a
deterministic test provider. Curated observations from a retained incident are
tested with controlled correct, wrong and leaked inputs. This is not replay of
all original telemetry or a live-model accuracy benchmark. Check the release's
`WORKFLOW-VERIFICATION.json` for platform-specific results and limits.

Extract into a new folder or use Workbench Updates. Keep the complete records
home and existing task runtimes. Linked work continues in its original host.

[한국어](WORKFLOW_HARDENING_KR.md) · [Manual](https://calf.vibepackr.com/manual/?lang=en#workflow-hardening)
