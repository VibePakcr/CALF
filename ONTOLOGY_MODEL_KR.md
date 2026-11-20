# 객체·속성·관계·제약 명세

현재 안내: Harness 1.8.25 · Workbench 1.9.23 · SDK 0.2.11.

최초 적용 버전과 이력: Harness 1.8.24 · Workbench 1.9.21 · Under Patch 2026-11-16 · 저장 기록 형식 1 유지. 기존 파일을 이 명세에 맞춰 다시 쓰거나 마이그레이션하지 않습니다.

CALF의 도메인은 작업과 검증 근거입니다. 네 가지 저장 기록 타입, 공통·타입별 속성, 네 가지 관계와 검증 제약을 Rust 네이티브 코어에서 정의합니다. 그래프는 이 모델의 읽기 전용 투영입니다.

임의의 업무 객체를 설계하는 범용 업무 온톨로지나 인과 추론 기능을 주장하지 않습니다. 기록의 origin은 출처 필드이며 암호학적으로 인증된 행위자 신원이 아닙니다. 구조적 유효성만으로 실행·통과·권한을 입증하지 않습니다.

## 저장 객체 타입

| 타입 | 의미 | data 변형 |
| --- | --- | --- |
| TASK | 범위·검사 기준이 있는 작업 계약 또는 관측 전용 작업 | task.registered, task.observed |
| ACTION | 행동 메모 또는 연결된 호스트·자료 관측 | action.note, action.hostStart, action.hostEnd, action.hostConflict, action.mcpArtifact |
| CHECK | 등록된 검사 기준과 연결된 실행 영수증. 형식이 유효하다는 사실만으로 통과를 뜻하지 않음 | check.native, check.host |
| DECISION | 운영자의 검토 또는 과거 완료 판단 기록 | decision.review, decision.completion |

## 공통 속성

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| id | identifier | 필수 |
| kind | recordKind | 필수 |
| task | identifier | 필수 |
| body | text | 필수 |
| origin | origin | 필수 |
| state | initialState | 필수 |
| data | recordData | 필수 |
| relations | relation[] | 필수 |

## 관계의 도메인·범위

| 관계 | 허용 출발 → 도착 | 작업 범위 | 분류 |
| --- | --- | --- | --- |
| based_on | TASK → TASK, TASK → ACTION, TASK → CHECK, TASK → DECISION, ACTION → TASK, ACTION → ACTION, ACTION → CHECK, ACTION → DECISION, CHECK → TASK, CHECK → ACTION, CHECK → CHECK, CHECK → DECISION, DECISION → TASK, DECISION → ACTION, DECISION → CHECK, DECISION → DECISION | 다른 작업 참조 허용 | REFERENCE |
| checks | CHECK → TASK, CHECK → ACTION | 동일 작업 필수 | REFERENCE |
| supersedes | TASK → TASK, ACTION → ACTION, CHECK → CHECK, DECISION → DECISION | TASK 대체 이외에는 동일 작업 필수 | VERSION |
| conflicts_with | TASK → TASK, TASK → ACTION, TASK → CHECK, TASK → DECISION, ACTION → TASK, ACTION → ACTION, ACTION → CHECK, ACTION → DECISION, CHECK → TASK, CHECK → ACTION, CHECK → CHECK, CHECK → DECISION, DECISION → TASK, DECISION → ACTION, DECISION → CHECK, DECISION → DECISION | 동일 작업 필수 | CONFLICT |

모든 저장 관계는 type·to·state 세 속성을 가집니다. 출발점은 관계를 가진 기록이고 도착점은 to가 가리키는 이전 기록입니다. based_on·checks는 참조 의존성, supersedes는 버전 대체, conflicts_with는 충돌입니다. 저장된 충돌 선은 방향이 있지만 유효성 계산은 해당 두 기록을 함께 고려합니다.

## 타입별 속성

### task.registered

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| scope | relativePath[] | 필수 |
| criteria | criterion[] | 필수 |

### task.observed

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| mode | observedMode | 필수 |
| scope | emptyArray | 필수 |
| criteria | emptyArray | 필수 |

### criterion

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| id | identifier | 필수 |
| command | argument[] | 필수 |
| envKeys | environmentKey[] | 필수 |

### snapshot

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| complete | boolean | 필수 |
| reason | string\|null | 필수 |
| digest | sha256\|null | 필수 |

### action.note

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| details | text | 필수 |

### action.hostStart

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| details | text | 필수 |
| hostStart | hostStart | 필수 |

### action.hostEnd

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| details | text | 필수 |
| hostEnd | hostEnd | 필수 |

### action.hostConflict

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| details | text | 필수 |
| hostConflict | hostConflict | 필수 |

### action.mcpArtifact

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| details | text | 필수 |
| mcpArtifact | mcpArtifact | 필수 |

### hostStart

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| attempt | identifier | 필수 |
| step | unsignedInteger | 필수 |
| criterion | criterionId\|null | 필수 |
| taskHash | sha256 | 필수 |
| before | snapshot | 필수 |
| context | sha256\|null | 필수 |
| commandHash | sha256 | 필수 |
| cwd | string | 필수 |
| started | finiteNumber | 필수 |

### hostEnd

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| start | recordId | 필수 |
| step | matchingStartStep | 필수 |
| attempt | matchingStartAttempt | 필수 |
| exitCode | integer\|null | 필수 |
| error | boolean | 필수 |
| resultHash | sha256 | 필수 |

### hostConflict

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| attempt | identifier | 필수 |

### mcpArtifact

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| attempt | identifier | 필수 |
| taskHash | sha256 | 필수 |
| policyHash | sha256 | 필수 |
| scope | snapshot | 필수 |
| source | artifactSource | 필수 |

### check.native

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| criterion | identifier | 필수 |
| before | snapshot | 필수 |
| after | snapshot | 필수 |
| context | sha256\|null | 필수 |
| receipt | receipt | 필수 |

### check.host

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| criterion | identifier | 필수 |
| before | snapshot | 필수 |
| after | snapshot | 필수 |
| context | sha256\|null | 필수 |
| receipt | receipt | 필수 |
| source | checkSource | 필수 |

### checkSource

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| start | recordId | 필수 |
| step | matchingStartStep | 필수 |
| attempt | matchingStartAttempt | 필수 |
| resultHash | sha256 | 필수 |

### receipt

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| argv | matchingCriterionCommand | 필수 |
| cwd | string | 필수 |
| started | finiteNumber | 필수 |
| finished | finiteNumber | 필수 |
| exitCode | integer\|null | 필수 |
| signal | string\|null | 필수 |
| error | string\|null | 필수 |
| stdoutSha | sha256\|nullForHostSource | 필수 |
| stderrSha | sha256\|nullForHostSource | 필수 |

### decision.review

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| purpose | reviewPurpose | 필수 |
| target | recordId | 필수 |
| relation | relationIndex\|null | 필수 |
| state | reviewState | 필수 |
| reason | nonemptyText | 필수 |

### decision.completion

| 속성 | 자료형 | 존재 조건 |
| --- | --- | --- |
| purpose | completionPurpose | 필수 |
| outcome | outcome | 필수 |
| reasons | string[] | 필수 |
| head | sha256 | 필수 |

## 검증 제약과 적용 시점

- `record-fields`: 선택한 변형마다 필수 속성을 정확히 검사하며 알 수 없는 속성을 거부합니다. [APPEND, LOAD]
- `record-identity`: 기록 ID는 고유합니다. TASK는 id=task이며 다른 기록은 앞서 저장된 TASK에 속합니다. [APPEND, LOAD]
- `previous-target`: 관계 대상은 이미 존재하는 별도 기록이어야 합니다. 자기 참조·미래 참조를 거부합니다. 저장된 참조는 기록 순서의 이전 방향을 가리킵니다. [APPEND, LOAD]
- `relation-domain-range`: 관계별 허용 출발·도착 타입과 작업 범위를 검사합니다. 같은 type/to 조합의 중복 관계를 거부합니다. [APPEND, LOAD]
- `proposal-state`: agent 출처 기록은 proposed 상태이며 제안 기록에 accepted 관계를 넣을 수 없습니다. [APPEND, LOAD]
- `contract`: 등록 작업의 범위·검사 기준은 비어 있지 않고 수와 중복을 제한합니다. 상대 경로·명령 인수·선택 환경 키도 검사합니다. [APPEND, LOAD]
- `observed-task`: 관측 전용 TASK의 scope와 criteria는 비어 있습니다. 호스트 활동 관측만으로 작업 계약이 생기지 않습니다. [APPEND, LOAD]
- `check-binding`: CHECK는 등록된 criterion과 정확한 명령을 가리키고 자신의 TASK에 checks 관계를 가져야 합니다. accepted CHECK에는 collector 출처가 필요합니다. [APPEND, LOAD]
- `snapshot-and-receipt`: 완전한 스냅샷은 해시와 null reason을, 불완전한 스냅샷은 null 해시와 문자열 reason을 가집니다. 실행 시각은 유한하고 종료가 시작보다 빠를 수 없습니다. 미확인 결과의 null은 그대로 유지합니다. [APPEND, LOAD]
- `host-bindings`: 호스트 시작·종료·검사·자료 변형은 해당 작업 개정, 시작 기록, 단계, 시도, 수집 범위를 서로 대조합니다. 시작·종료·자료 변형에는 accepted collector 출처가 필요합니다. [APPEND, LOAD]
- `operator-review`: 검토는 accepted operator DECISION입니다. 같은 작업의 DECISION 이외 기록 또는 그 기록의 유효한 관계 인덱스를 대상으로 하며 빈 사유를 거부합니다. collector가 아닌 CHECK를 승격할 수 없습니다. [APPEND, LOAD]
- `review-transition`: 모든 기록 추가 경로에서 이미 retracted로 투영된 기록의 accepted 재승격을 거부합니다. 기존 기록을 다시 쓰거나 과거 읽기 형식을 바꾸지 않습니다. [APPEND]
- `canonical-history`: 정규화된 기록 마크업·프로젝트/워크스페이스 연결·순서·전체 SHA-256 체인을 확인합니다. 새 추가에는 기대한 최신 head가 필요하며 동시 변경을 거부합니다. [APPEND, LOAD]
- `active-graph`: 유효한 의존성에는 accepted 기록과 관계가 필요합니다. 철회·대체·충돌 또는 확인할 수 없거나 너무 깊은 의존성을 유효하다고 처리하지 않습니다. [ACTIVE_GRAPH_QUERY]
- `completion-boundary`: 형식이 맞는 기록이나 과거 완료 선언은 현재 완료 판정이 아닙니다. 현재 판정은 등록 기준·보존 근거·파일 범위·실행 문맥을 따로 확인합니다. [COMPLETION_QUERY]

식별자: ASCII 1–128바이트, 첫 글자는 영숫자. body·details: 최대 8,192 UTF-16 단위이며 빈 문자열도 형식상 허용합니다. 등록 scope·criteria: 각 1–64개. 명령 인수: 1–128개, 각 인수는 8,192 UTF-16 단위 미만. 관계: 기록당 0–64개. 이력: 최대 4,096개. active 의존성 깊이 제한: 64. 전체 기본형과 조건부 속성은 JSON 명세에 있습니다.

## 저장 모델과 화면 투영의 구분

Workbench journal은 별도 저장 형식입니다. 화면에는 가상 TASK와 EVENT·CONTRACT 등이 표시될 수 있습니다. task_record는 소속 표시이며 의존성이 아닙니다. 타입 이름이 비슷해도 journal CHECK와 저장 온톨로지 CHECK를 같은 계약으로 합치지 않습니다. 영향 조회는 선택한 작업의 승인되고 유효한 based_on·checks 관계만 따릅니다.

[JSON](ONTOLOGY_MODEL.json) · [English](ONTOLOGY_MODEL.md) · [사용 안내](ONTOLOGY_GUIDE_KR.md)
