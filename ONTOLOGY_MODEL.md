# Object, property, relationship and constraint specification

Current guide: Harness 1.8.25 · Workbench 1.9.23 · SDK 0.2.11.

Original release context: Harness 1.8.24 · Workbench 1.9.21 · Under Patch 2026-11-16 · stored record format 1 retained. Existing files are not rewritten or migrated.

CALF models tasks and their evidence. Four stored record types, common and variant properties, four relationship types and validation constraints are defined in the native Rust core. The graph is a read-only projection of that model.

This is a task-evidence model. It does not claim arbitrary business-domain modeling or causal inference. Origin is a provenance field, not a cryptographic actor identity. Structural validity alone does not prove execution, success or permission.

## Stored object types

| Type | Meaning | Data variants |
| --- | --- | --- |
| TASK | A registered work contract or an observation-only task | task.registered, task.observed |
| ACTION | An action note or a bound host/artifact observation | action.note, action.hostStart, action.hostEnd, action.hostConflict, action.mcpArtifact |
| CHECK | A retained receipt bound to a registered criterion; validity alone is not a passing verdict | check.native, check.host |
| DECISION | An operator review or a historical completion declaration | decision.review, decision.completion |

## Common properties

| Property | Type | Presence |
| --- | --- | --- |
| id | identifier | Required |
| kind | recordKind | Required |
| task | identifier | Required |
| body | text | Required |
| origin | origin | Required |
| state | initialState | Required |
| data | recordData | Required |
| relations | relation[] | Required |

## Relationship domain and range

| Relation | Allowed source → target | Task scope | Family |
| --- | --- | --- | --- |
| based_on | TASK → TASK, TASK → ACTION, TASK → CHECK, TASK → DECISION, ACTION → TASK, ACTION → ACTION, ACTION → CHECK, ACTION → DECISION, CHECK → TASK, CHECK → ACTION, CHECK → CHECK, CHECK → DECISION, DECISION → TASK, DECISION → ACTION, DECISION → CHECK, DECISION → DECISION | May cross tasks | REFERENCE |
| checks | CHECK → TASK, CHECK → ACTION | Same task required | REFERENCE |
| supersedes | TASK → TASK, ACTION → ACTION, CHECK → CHECK, DECISION → DECISION | Same task except TASK replacement | VERSION |
| conflicts_with | TASK → TASK, TASK → ACTION, TASK → CHECK, TASK → DECISION, ACTION → TASK, ACTION → ACTION, ACTION → CHECK, ACTION → DECISION, CHECK → TASK, CHECK → ACTION, CHECK → CHECK, CHECK → DECISION, DECISION → TASK, DECISION → ACTION, DECISION → CHECK, DECISION → DECISION | Same task required | CONFLICT |

Every stored relation has exactly type, to and state. Its source is the owning record and its target is the previous record named by to. based_on and checks are reference dependencies; supersedes is replacement; conflicts_with records conflict. A stored conflict edge is directed, while active-state evaluation considers both involved records.

## Variant properties

### task.registered

| Property | Type | Presence |
| --- | --- | --- |
| scope | relativePath[] | Required |
| criteria | criterion[] | Required |

### task.observed

| Property | Type | Presence |
| --- | --- | --- |
| mode | observedMode | Required |
| scope | emptyArray | Required |
| criteria | emptyArray | Required |

### criterion

| Property | Type | Presence |
| --- | --- | --- |
| id | identifier | Required |
| command | argument[] | Required |
| envKeys | environmentKey[] | Required |

### snapshot

| Property | Type | Presence |
| --- | --- | --- |
| complete | boolean | Required |
| reason | string\|null | Required |
| digest | sha256\|null | Required |

### action.note

| Property | Type | Presence |
| --- | --- | --- |
| details | text | Required |

### action.hostStart

| Property | Type | Presence |
| --- | --- | --- |
| details | text | Required |
| hostStart | hostStart | Required |

### action.hostEnd

| Property | Type | Presence |
| --- | --- | --- |
| details | text | Required |
| hostEnd | hostEnd | Required |

### action.hostConflict

| Property | Type | Presence |
| --- | --- | --- |
| details | text | Required |
| hostConflict | hostConflict | Required |

### action.mcpArtifact

| Property | Type | Presence |
| --- | --- | --- |
| details | text | Required |
| mcpArtifact | mcpArtifact | Required |

### hostStart

| Property | Type | Presence |
| --- | --- | --- |
| attempt | identifier | Required |
| step | unsignedInteger | Required |
| criterion | criterionId\|null | Required |
| taskHash | sha256 | Required |
| before | snapshot | Required |
| context | sha256\|null | Required |
| commandHash | sha256 | Required |
| cwd | string | Required |
| started | finiteNumber | Required |

### hostEnd

| Property | Type | Presence |
| --- | --- | --- |
| start | recordId | Required |
| step | matchingStartStep | Required |
| attempt | matchingStartAttempt | Required |
| exitCode | integer\|null | Required |
| error | boolean | Required |
| resultHash | sha256 | Required |

### hostConflict

| Property | Type | Presence |
| --- | --- | --- |
| attempt | identifier | Required |

### mcpArtifact

| Property | Type | Presence |
| --- | --- | --- |
| attempt | identifier | Required |
| taskHash | sha256 | Required |
| policyHash | sha256 | Required |
| scope | snapshot | Required |
| source | artifactSource | Required |

### check.native

| Property | Type | Presence |
| --- | --- | --- |
| criterion | identifier | Required |
| before | snapshot | Required |
| after | snapshot | Required |
| context | sha256\|null | Required |
| receipt | receipt | Required |

### check.host

| Property | Type | Presence |
| --- | --- | --- |
| criterion | identifier | Required |
| before | snapshot | Required |
| after | snapshot | Required |
| context | sha256\|null | Required |
| receipt | receipt | Required |
| source | checkSource | Required |

### checkSource

| Property | Type | Presence |
| --- | --- | --- |
| start | recordId | Required |
| step | matchingStartStep | Required |
| attempt | matchingStartAttempt | Required |
| resultHash | sha256 | Required |

### receipt

| Property | Type | Presence |
| --- | --- | --- |
| argv | matchingCriterionCommand | Required |
| cwd | string | Required |
| started | finiteNumber | Required |
| finished | finiteNumber | Required |
| exitCode | integer\|null | Required |
| signal | string\|null | Required |
| error | string\|null | Required |
| stdoutSha | sha256\|nullForHostSource | Required |
| stderrSha | sha256\|nullForHostSource | Required |

### decision.review

| Property | Type | Presence |
| --- | --- | --- |
| purpose | reviewPurpose | Required |
| target | recordId | Required |
| relation | relationIndex\|null | Required |
| state | reviewState | Required |
| reason | nonemptyText | Required |

### decision.completion

| Property | Type | Presence |
| --- | --- | --- |
| purpose | completionPurpose | Required |
| outcome | outcome | Required |
| reasons | string[] | Required |
| head | sha256 | Required |

## Constraints and enforcement points

- `record-fields`: Required fields are exact; unknown properties are rejected for each selected variant. [APPEND, LOAD]
- `record-identity`: Record IDs are unique. TASK has id=task. Other records bind a previously stored TASK. [APPEND, LOAD]
- `previous-target`: Stored relationship targets must already exist and be distinct. Forward and self references are rejected; stored relationship edges follow record order backwards. [APPEND, LOAD]
- `relation-domain-range`: The native allowed-pair predicate and task restrictions define each relation's source and target domains. Duplicate type/target pairs are rejected. [APPEND, LOAD]
- `proposal-state`: Agent-origin records are proposed. A proposed record cannot contain accepted relationships. [APPEND, LOAD]
- `contract`: Registered scope and criteria are nonempty, bounded and unique. Paths are relative; criterion commands and environment keys are constrained. [APPEND, LOAD]
- `observed-task`: Observation-only TASK has empty scope and criteria; observing host activity does not create a work contract. [APPEND, LOAD]
- `check-binding`: CHECK names an existing criterion, matches its exact command and includes checks to its own TASK. Accepted CHECK requires collector origin. [APPEND, LOAD]
- `snapshot-and-receipt`: A complete snapshot has a SHA-256 digest and null reason; an incomplete snapshot has null digest and a string reason. Receipt numbers are finite, finish >= start, and nullable results are retained as unknown. [APPEND, LOAD]
- `host-bindings`: Host start/end/check/artifact variants bind their declared task revision, start, step, attempt and collected scope as applicable. Start, end and artifact variants require accepted collector origin. [APPEND, LOAD]
- `operator-review`: Review is an accepted operator-origin DECISION, targets a same-task non-DECISION record or its existing relation index, and requires a nonempty reason. It cannot promote a non-collector CHECK. [APPEND, LOAD]
- `review-transition`: Every writer, including direct append and the review command, rejects accepting a record already projected as retracted. Legacy histories retain their original structural read format; no stored reviews are rewritten. [APPEND]
- `canonical-history`: Canonical markup, metadata binding, sequence and the full SHA-256 chain are checked. Append additionally requires the expected current head and rejects concurrent changes. [APPEND, LOAD]
- `active-graph`: Active dependencies require accepted records/relations. Retracted, superseded or conflicting evidence and unavailable/deep dependencies are not cleared as active. [ACTIVE_GRAPH_QUERY]
- `completion-boundary`: A well-formed record or stored completion declaration is not a current verdict. Current completion separately checks registered criteria, retained evidence, file scope and execution context. [COMPLETION_QUERY]

Identifiers: 1–128 ASCII bytes, starting alphanumeric. body/details: at most 8,192 UTF-16 code units; empty strings are structurally allowed. Registered scope/criteria: 1–64 each. Command arguments: 1–128; each shorter than 8,192 UTF-16 code units. Relations: 0–64 per record. History: at most 4,096 records. Active dependency depth limit: 64. The JSON specification lists primitive definitions and conditional fields.

## Storage model and view projection

Workbench journals use a separate storage format. Views may contain virtual TASK and EVENT/CONTRACT nodes. task_record is membership, not a dependency. Similarly named journal CHECK and stored ontology CHECK records do not acquire the same contract. Impact follows accepted active based_on/checks dependencies within the selected task only.

[JSON](ONTOLOGY_MODEL.json) · [한국어](ONTOLOGY_MODEL_KR.md) · [Usage guide](ONTOLOGY_GUIDE.md)
