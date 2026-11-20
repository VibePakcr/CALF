# 과거 장애 평가 · 반증 검증 · 이벤트 기반 재개

현재 안내: Harness 1.8.25 · Workbench 1.9.23 · SDK 0.2.11.

CALF의 기존 Rust 코어·작업 계약·HTML 저널을 확장합니다. 기존 작업을 자동
등록하지 않으며 원래 계약·설정·보존 실행기를 유지합니다. 별도 에이전트 팩토리,
외부 ETS/GCI 연결, 웹훅 서버나 상주 데몬은 추가하지 않습니다.

## 과거 장애 평가

`calf evaluation < request.json`에 `schema: calf.evaluation.v1`,
`op: backtest_prepare`, `case`를 전달합니다.

```json
{
  "id": "incident-example", "provenance": "synthetic", "cutoffMs": 1000,
  "signal": "상태 조회가 실패했습니다.",
  "evidence": [
    {"id": "observed", "kind": "observation", "availableAtMs": 900, "text": "기록 작성기가 잠금을 보유하고 있습니다."},
    {"id": "answer", "kind": "resolution", "availableAtMs": 1100, "text": "보존된 사후 진단입니다."}
  ],
  "oracle": {"causes": ["writer-contention"], "onsetMs": 900,
    "onsetToleranceMs": 100, "affected": ["status-query"], "evidenceIds": ["observed"]}
}
```

위 `case`는 합성 예제입니다. 실제 사례는 `source_reported` 출처와 확인한 시각을
사용합니다. 기준 시각까지 이용 가능했던 `observation`·`code`만 조사 패킷에
포함됩니다. `resolution`·`memory`·`prior_run`과 미래 자료는 제외합니다. 증거는
최대 128개이며 정답에 필요한 근거가 허용된 자료에 없으면 거절합니다.

조사자에게는 응답의 `packet`만 제공합니다. 평가자는 `case`, 정답, 과거 실행
결과를 별도 보관하고 `packetDigest`와 `caseCommitment`를 고정합니다. 패킷 생성
자체가 호스트 전체의 파일·네트워크 격리를 보장하지는 않습니다. 실제 에이전트는
새 문맥과 제한된 자료·도구 접근 경로로 실행하고 접근 기록을 별도로 확보합니다.

`op: backtest_score`에는 다음 필드를 전달합니다.

- `case`, `caseCommitment`: 준비 단계에서 고정한 원본과 해시.
- `submission`: `caseId`, `packetDigest`, `investigatorId`, `cause`, `onsetMs`,
  `affected`, `evidenceIds`, `handoff`.
- `handoff`: `summary`, `impact`, `uncertainty`, `nextStep`, `evidenceIds`.
- `access`: `state`(`complete`·`partial`·`unobserved`)와 관측한 `evidenceIds`.
- `handoffReview`: 미검토이면 `null`. 검토 시 `reviewerId`, `handoffDigest`,
  각 0–4점의 `clarity`·`impact`·`evidence`·`nextStep`, 그리고 `reason`.

원인·시작 시점·영향 대상의 미관측 값은 `null`이며 0·빈 목록과 구분합니다.
원인 레이블, 시작 시점 오차, 영향 대상 집합, 필수 근거 인용을 각각 평가합니다.
정답을 추측해 맞힌 경우와 근거를 갖춘 정답을 구분합니다. 보고서 필드 충족과
보고서 유용성도 별도입니다. 같은 조사자 ID의 검토와 다른 보고서 해시의 검토는
거절하지만 검토자 신원 자체를 인증하지는 않습니다.

금지 자료 접근·인용 또는 금지 원문의 직접 복사가 확인되면 `EXCLUDED_LEAKAGE`,
접근 범위가 불완전하면 `EXCLUDED_ACCESS_UNKNOWN`으로 점수를 내지 않습니다.
접근 범위는 호출자 보고값이고 직접 복사 검사는 의미를 바꾼 누출까지 탐지하지
못합니다. 정상 결과도 `SCORED_LABEL_AGREEMENT`이며 모델 능력 인증이 아닙니다.

## 기존 CHECK에 결속하는 반증 검증

`op: diagnosis_prepare`는 `root`와 아래 `plan`을 받습니다.

```json
{
  "schema": "calf.diagnosis-plan.v1", "task": "REGISTERED_TASK_ID",
  "taskHash": "ACCEPTED_TASK_ENVELOPE_SHA256", "hypothesis": "검증할 가설",
  "checks": [
    {"criterion": "support", "role": "support", "question": "관측이 가설을 지지하는가?"},
    {"criterion": "control", "role": "counterexample", "question": "제시한 반례가 배제되는가?"},
    {"criterion": "alternative", "role": "alternative", "question": "명시한 대안 설명을 배제할 근거가 있는가?"}
  ]
}
```

모든 등록 검사 ID를 중복 없이 포함하고 세 역할을 모두 선언합니다. 반증 검사는
제시한 반례가 배제될 때, 대안 검사는 명시한 대안 설명이 배제될 때 통과하도록
작성합니다. 질문을 적는 것만으로 검사의 의미나 독립성이 입증되지는 않습니다.

준비 응답의 `planDigest`를 검사 전에 고정합니다. 기존 `calf check` 또는 승인된
호스트 검사 경로로 실제 검사를 실행한 뒤 `op: diagnosis`에 같은 `root`, `plan`,
`planDigest`를 전달합니다. 결과를 입력으로 제출해 네이티브 CHECK를 대체할 수
없습니다. 새 계획 해시의 평가는 원래 평가와 구분해야 합니다.

| 결과 | 의미 |
|---|---|
| `SUPPORTED_BY_CHECKS` | 현재 범위·환경에서 모든 등록 검사가 통과함 |
| `REJECTED_BY_CHECKS` | 유효한 검사에서 선언한 조건의 실패를 확인함 |
| `INCONCLUSIVE` | 검사 누락·낡은 근거·충돌·미완료 또는 도구 오류 |

검사 종료 코드는 0=조건 충족, 1=조건 불충족, 그 외=도구 오류입니다. 오류를
반증 성공으로 취급하지 않습니다. 파일·환경·기록이 바뀌면 이전 통과를 현재
근거로 사용하지 않습니다. 조회는 인덱스 재생성이나 기록 쓰기를 수행하지
않습니다. 결과는 선언한 검사 아래의 판단이며 보편적 인과 증명·완료 기록·
실행 승인이 아닙니다. 기존 완료 판정은 계속 기존 네이티브 엔진이 담당합니다.

## 이벤트 대기와 지정 작업 재개

`calf events < request.json` 또는 공통 API
`{"op":"events","request":REQUEST}`를 사용합니다. 모든 요청은
`schema: calf.event-resume.v1`, 명시적 `home`, 관리 작업의 `task`를 포함합니다.
읽기 전용으로 연결된 호스트 작업에는 적용하지 않습니다.

| op | 추가 필드와 동작 |
|---|---|
| `observe` | 현재 `viewDigest`, `head`, 대기 상태를 읽음. 기록 생성 없음 |
| `arm` | `expectedViewDigest`, `expectedHead`, `subscription`으로 대기 등록 |
| `deliver` | `waitDigest`, `event` 검증 후 지정 작업을 큐잉 |
| `dispatch` | 전달 검증 후 해당 작업만 기존 worker로 실행 |
| `revoke` | `waitDigest`에 결속한 대기를 철회하고 기존 pause 파일을 남김 |

`subscription`은 `id`, `source`, `subject`, `revision`, `kind`, `ttlMs`입니다.
`event`는 `id`, `source`, `subject`, `revision`, `kind`, `occurredAtMs`입니다.
종류는 `review_completed`, `checks_completed`, `deployment_completed`,
`dependency_ready`이며 명령·인수·승인 필드를 넣을 수 없습니다. TTL은 1ms–7일,
발생 시각은 등록 이후·만료 이전이며 미래 시각이 아니어야 합니다.

`arm`은 `queued` 작업만 허용합니다. 실행 중인 worker, 취소, 사람의 일시정지,
미결 실행이 있으면 거절합니다. 고정된 작업 실행기가 현재 코어와 같은 바이너리여야
하며 오래된 실행기를 교체하지 않습니다. `expectedHead`는 `observe` 값을 그대로
사용합니다. 아직 저널이 없는 새 작업에서는 `null`입니다.

대기 중 worker는 종료합니다. 승인된 로컬 Adapter가 이벤트 도착 시 `dispatch`를
호출하면 해당 작업만 실행합니다. `deliver`만 호출한 경우 기존 명시적 worker
호출이 실행을 담당합니다. 같은 이벤트는 대기를 다시 큐잉하지 않습니다.
이벤트는 권한·자격증명·Operation Authority Lease를 생성하거나 갱신하지 않습니다.
`source` 문자열은 인증 수단이 아니므로 인증 없는 공개 웹훅으로 노출하면 안 됩니다.
외부 이벤트 수집기는 자동 설치하지 않으며 공식 Adapter의 인증·검증 경계를 따릅니다.

전이는 기존 HTML 저널에 먼저 기록합니다. 전달 후 화면 갱신이 중단되면 준비
기록에서 이어갑니다. 실행 소비만 있고 정산 기록이 없으면 `DISPATCH_UNCERTAIN` /
`needs_reconciliation`으로 남기며 자동 재실행하지 않습니다. 만료는 `EXPIRED`로
남깁니다. 사람 개입 조회도 정상 대기·만료·미결 실행을 구분합니다. 철회 후 재개는
기존 명시적 절차를 따르며 미결 실행의 복구 검사를 우회하지 않습니다.

## 검증 범위와 업데이트

격리된 네이티브 프로세스·실제 CHECK·결정적 시험 공급자로 검증합니다. 보존된 장애 보고서의 관측을 정답과 분리하고 통제된 정답·오답·누출 입력을 평가합니다. 원래 텔레메트리 전체 재생이나 실제 AI 모델 정확도 측정은 아닙니다. 운영체제별 결과와 한계는 릴리즈의 `WORKFLOW-VERIFICATION.json`을 확인하세요.

이번 기능은 Rust 코어의 CLI·공통 API로 사용합니다. 별도 그래픽 워크플로 편집기를 추가하지 않습니다. 새 폴더에 설치하거나 Workbench Updates를 사용하고 기존 기록 폴더·계약·설정·고정 실행기를 유지하세요. 연결된 작업은 원래 호스트에서 계속됩니다.

[English](WORKFLOW_HARDENING.md) · [매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#workflow-hardening)
