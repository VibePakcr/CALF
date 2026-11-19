# CALF 사용 안내 · User guide

## Workbench 1.9.22 — connected task status

Open a card under Connected tasks to read that exact host task. You can do this before choosing a workspace. Refresh status reads the same selected task again.

If the task is missing from a bounded or recently changed task list, Workbench retains its identity and requests that task directly. If its link is no longer readable, the view shows an error instead of displaying another task’s result. Check the existing host connection, then refresh; no restart is needed for this read-only view.

“Response ended” describes a recorded host event. It does not establish process liveness or completion of the whole task. UNKNOWN stays unknown when current completion has not been evaluated.

Sidebar utility panels occupy the central work area. Close or Esc returns to the task view. Switching between panels retains an unsaved preferences draft; Save preferences is the explicit save action.

Upgrade from Workbench 1.9.21 through Updates, or download 1.9.22 and extract it to a new folder. Keep your existing records folder, contracts, preferences and pinned task runtimes. Preparing the update leaves the current window running. Existing linked tasks continue in their original host.

## Workbench 1.9.22 — 연결 작업 상태 조회

Connected tasks에서 카드를 누르면 해당 호스트 작업의 기록을 읽습니다. 작업 폴더를 선택하기 전에도 사용할 수 있습니다. Refresh status는 현재 선택한 같은 작업을 다시 조회합니다.

작업이 제한된 목록이나 갱신된 목록에서 빠져도 선택한 ID를 유지해 그 작업을 직접 조회합니다. 연결을 읽을 수 없으면 다른 작업의 결과를 대신 보여주지 않고 오류를 표시합니다. 기존 호스트 연결을 확인한 뒤 다시 조회하세요. 읽기 전용 조회를 위해 작업을 재시작할 필요는 없습니다.

Response ended는 호스트의 응답 종료 기록입니다. 프로세스의 실행 여부나 전체 작업의 완료를 입증하지 않습니다. 현재 완료 여부를 평가하지 않았으면 UNKNOWN을 유지합니다.

좌측 메뉴의 보조 패널은 중앙 작업 영역에 표시됩니다. Close 또는 Esc로 작업 화면에 돌아갑니다. 패널을 전환해도 저장하지 않은 환경설정 초안은 유지되며, Save preferences를 눌러야 저장됩니다.

Workbench 1.9.21의 Updates에서 확인하거나 1.9.22를 받아 새 폴더에 압축을 푸세요. 기존 기록 폴더·계약·환경설정과 작업별 고정 런타임을 유지합니다. 업데이트를 준비하는 동안 현재 창은 계속 실행되며 연결된 작업은 원래 호스트에서 계속됩니다.


## 웹에서 읽기 · Read online

[한국어 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko) · [English manual](https://calf.vibepackr.com/manual/?lang=en)

설치부터 첫 작업, 결과 확인과 작업 재개까지 화면을 보며 따라가세요. 위쪽 **KO / EN** 버튼으로 언어를 바꿀 수 있습니다.

Follow the pictures to install CALF, start a task, review the result and resume work. Use **KO / EN** at the top to switch languages.

| 찾는 내용 · Find what you need | 한국어 | English |
| --- | --- | --- |
| CALF 소개 · Overview | [소개](https://calf.vibepackr.com/) | [Overview](https://calf.vibepackr.com/en/) |
| 프로그램 받기 · Download | [다운로드](https://calf.vibepackr.com/#downloads) | [Downloads](https://calf.vibepackr.com/en/#downloads) |
| 설치하기 · Install | [설치](https://calf.vibepackr.com/manual/?lang=ko#install) | [Installation](https://calf.vibepackr.com/manual/?lang=en#install) |
| 첫 작업 · First task | [첫 작업](https://calf.vibepackr.com/manual/?lang=ko#start) | [First task](https://calf.vibepackr.com/manual/?lang=en#start) |

## 짧은 안내 · Quick guides

[한국어 설치](INSTALL_KR.md) · [English installation](INSTALL.md) · [한국어 화면 안내](UI_GUIDE_KR.md) · [English screen guide](UI_GUIDE.md)

## 오프라인에서 읽기 · Read offline

[영·한 HTML 매뉴얼 받기 · Download the EN/KR HTML manual](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/CALF_mannual.html)

`CALF_mannual.html`을 받아 Chrome·Edge·Safari에서 여세요. 그림이 모두 들어 있어 인터넷 없이도 볼 수 있습니다. 이 파일은 위쪽 **EN / KR** 버튼으로 언어를 바꿉니다.

Download `CALF_mannual.html` and open it in Chrome, Edge or Safari. All pictures are included, so you can read it without an internet connection. In this file, use **EN / KR** to switch languages.

GitHub에서 HTML 미리보기가 열리지 않으면 위 다운로드 링크를 이용하세요.

If GitHub cannot preview the HTML file, use the download link above.

[GitHub release](https://github.com/VibePakcr/CALF/releases/tag/v1.9.21) · [GitLab release](https://gitlab.com/vibepackr-group/CALF/-/releases/v1.9.21) · [Downloads / 다운로드](DOWNLOADS.md)

## 이번 업데이트 · This update

[수정 제안 추가·되돌리기](REQUEST_GUIDANCE_KR.md) · [Add and undo correction suggestions](REQUEST_GUIDANCE.md)

[화면·상태 조회 변경 안내](UI_STATUS_PATCH_KR.md) · [Views and task status](UI_STATUS_PATCH.md)

[연결 작업 안내](HOST_TASKS_PATCH_KR.md) · [Connected task guide](HOST_TASKS_PATCH.md)

[근거 그래프와 변경 영향](ONTOLOGY_GUIDE_KR.md) · [Evidence exploration](ONTOLOGY_GUIDE.md)

[객체·속성·관계·제약 명세](ONTOLOGY_MODEL_KR.md) · [Object model specification](ONTOLOGY_MODEL.md) · [JSON](ONTOLOGY_MODEL.json)

[Credential-isolated operation delegation / 자격증명 격리 작업 위임](CALF_mannual.html#operation-delegation)


## Routing and lane evaluation / 라우팅·Lane 평가

# Routing and lane evaluation

`calf evaluation` evaluates supplied model/skill selections and reads accounting from explicit native task journals. The Rust core reuses GCN planning, write-owner validation and canonical journal observation. Reports are read-only and keep `executionAuthority: false` and `currentCompletion: "NOT_EVALUATED"`.

## Evaluate selections

```sh
calf evaluation < routing.json
```

```json
{
  "schema": "calf.evaluation.v1",
  "op": "routing",
  "provenance": "synthetic",
  "cases": [{
    "id": "prose-negative-control",
    "category": "prose",
    "expectedModels": ["model-a"],
    "requiredSkills": [],
    "forbiddenSkills": ["release"],
    "selectedModel": "model-a",
    "selectedSkills": []
  }]
}
```

Use `synthetic` for fixtures or `source_reported` for supplied observations. This label does not authenticate the source. The report separates model agreement, missing required skills and forbidden skill selections. Contradictory labels, duplicate IDs and duplicate selections are rejected.

An empty skill list is an observed selection of no skills. `null` is an unavailable observation and is excluded from the accuracy denominator. An observed model with no expected labels is unlabelled. These scores measure agreement with the supplied labels; they do not prove actual host skill invocation or model quality.

## Read a checkpoint and account for lanes

Send this request with real, absolute paths:

```json
{
  "schema": "calf.evaluation.v1",
  "op": "checkpoint",
  "workspace": "/absolute/project",
  "journal": "/absolute/state"
}
```

For `op: "lanes"`, supply `moduleIds`, the existing `calf.gcn.lanes.v1` plan, `bindings`, and `rates` (an empty array is valid). Each binding contains `cell`, `workspace`, `journal`, `task` and the exact observed `head` with its `seq` and `hash`. See the Korean guide for a complete plan example. The native API accepts the same request through `{"op":"evaluation","request":…}`.

Bindings explicitly attribute a recorded task to a cell. They do not prove that the task contract's file scope equals the plan's write scope. The native planner validates dependencies and write conflicts. Shared prerequisite cells count once in the overall total; each lane subtotal includes its own prerequisites, so lane subtotals are not additive.

`UNBOUND_NOT_OBSERVED` means a cell has no supplied task binding. `NO_START_RECORDED` means the bound journal has no process start for that task. Neither proves that a task never ran elsewhere. Saved outcomes and check receipts remain historical. Required, observed and missing recorded checks are reported separately; the query runs no checks and grants no current completion verdict.

A changed checkpoint, an in-progress journal extension or a bounded observation limit rejects the query. The reader neither takes over the writer nor repairs the source. Inputs are limited to 512KiB and reports to 256KiB, within the existing journal record/byte budgets. Lanes retain the native logical single-executor meaning.

## Usage, time and estimates

New native provider attempts record monotonic elapsed time for success and failure. `sumProviderElapsedMs` is a sum of call durations, including transport overhead. It is not total task makespan or pure inference time.

Built-in adapters collect numeric counters when a supported response supplies them: OpenAI Responses usage, a single Codex `turn.completed` usage event, local OpenAI-compatible Chat usage, or Ollama prompt/evaluation counts. Ollama cached-input counts and Antigravity usage remain unavailable. The configured/requested `model` is not independent attestation of the provider's resolved backend model.

Counters travel through an optional receipt bound to the operation and input hash. Provider reply formats and task checks are retained. Missing, malformed, unsupported and legacy counters stay `null`. A partial total stays `null`; `known…` fields and observed-call counts expose only the known portion. Known zero with incomplete coverage does not mean a free call.

Each optional rate entry has `provider`, `model`, `sourceSha256`, `inputMicrosPerMillion`, `outputMicrosPerMillion` and `cachedInputMicrosPerMillion`. Units are micro-USD per million tokens. Uncached input and cached input are priced separately, with each call rounded down to micro-USD. The exact provider/model rate and all required counters must be present. The source hash binds supplied data but does not verify a current tariff. `billedCost` remains `null`.

## Real-model pilot

On 2026-11-19, the official Codex CLI ran three isolated tasks per model at requested medium reasoning, one attempt each: decimal CSV totals, half-open interval merging and a skill-selection fixture. CALF recorded 12 planner/reviewer calls. Both models passed all three native checks, current status reads and separate check reruns.

| Requested model | Tasks passed | Median task time | Input/output tokens, all three tasks | Standard API equivalent, all three tasks |
| --- | --- | --- | --- | --- |
| GPT-6.2-Sol | 3/3 | 40.112s | 145,156 / 3,459 | $0.324902 |
| GPT-6.2-Astra | 3/3 | 38.319s | 151,341 / 2,780 | $1.321928 |

The token counts are provider-reported. The price column applies the published short-context Standard API rates, excluding unreported cache writes, tier multipliers and subscription credit accounting; it is not an invoice. Each model has only three single-attempt samples. Backend load, service tier and cache state were not controlled, so this pilot does not establish a general model ranking or repeatable speedup. The generated selector passed four observed required/forbidden selection cases; it did not invoke host skills.

[OpenAI Sol rates](https://developers.openai.com/api/docs/models/gpt-6.2-sol) · [Astra rates](https://developers.openai.com/api/docs/models/gpt-6.2-astra) · [한국어 안내](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING_EVALUATION_KR.md) · [Qualification](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING-LANE-VERIFICATION.json)


# 라우팅·스킬 선택·Lane 실행 계측

CALF의 Rust 코어는 `calf evaluation`으로 선택 결과와 보관된 실행 기록을 평가합니다. 기존 GCN 계획 검사, 작업 저널, 작업공간 쓰기 잠금을 재사용합니다. 이 명령은 CPU에서 읽기 전용으로 실행되며 모델 선택, 자동 대체, 작업 실행, 승인 또는 현재 완료 판정을 수행하지 않습니다.

## 모델·스킬 선택 평가

```sh
calf evaluation < routing.json
```

```json
{
  "schema": "calf.evaluation.v1",
  "op": "routing",
  "provenance": "synthetic",
  "cases": [{
    "id": "prose-negative-control",
    "category": "prose",
    "expectedModels": ["model-a"],
    "requiredSkills": [],
    "forbiddenSkills": ["release"],
    "selectedModel": "model-a",
    "selectedSkills": []
  }]
}
```

`provenance`는 합성 시험의 `synthetic`, 외부 관측 자료의 `source_reported` 중 하나입니다. 사용자 제공 출처 구분이며 자료의 진위를 인증하지 않습니다. 모델의 기대 목록과 선택 결과가 일치하는지, 필수 스킬이 누락됐는지, 금지 스킬이 선택됐는지를 각각 집계합니다. 모순된 필수·금지 목록, 중복 식별자와 중복 선택은 거부합니다.

`selectedSkills: []`는 아무 스킬도 선택하지 않았다는 관측입니다. `null`은 관측이 없어 평가할 수 없다는 뜻입니다. 누락 관측은 정확도 분모에서 제외하고 별도로 표시합니다. 기대 모델 목록이 없으면 모델 선택 결과를 정답으로 채점하지 않습니다.

보고서는 제공한 정답 레이블과의 일치도입니다. 실제 호스트의 스킬 호출, 모델의 작업 품질 또는 성능 우위를 증명하지 않습니다. 실제 평가 자료를 모아 동일한 작업·검사·환경 조건에서 비교해야 라우팅 정책의 효용을 판단할 수 있습니다.

## 체크포인트와 Lane 계측

먼저 명시한 원본 저널의 체크포인트를 읽습니다.

```json
{
  "schema": "calf.evaluation.v1",
  "op": "checkpoint",
  "workspace": "/absolute/project",
  "journal": "/absolute/state"
}
```

반환된 `head`의 `seq`와 `hash`를 Lane 평가 요청에 그대로 넣습니다.

```json
{
  "schema": "calf.evaluation.v1",
  "op": "lanes",
  "moduleIds": ["core"],
  "plan": {
    "schema": "calf.gcn.lanes.v1",
    "cells": [{
      "id": "implementation",
      "modules": ["core"],
      "dependsOn": [],
      "writes": ["src/value.rs"],
      "checks": []
    }],
    "lanes": [{"id": "main", "cells": ["implementation"]}]
  },
  "bindings": [{
    "cell": "implementation",
    "workspace": "/absolute/project",
    "journal": "/absolute/state",
    "task": "TASK_ID_FROM_NATIVE_RUN",
    "head": {"seq": 1, "hash": "REPLACE_WITH_OBSERVED_64_HEX_HASH"}
  }],
  "rates": []
}
```

위 경로·작업 ID·체크포인트는 설명용 자리표시자입니다. 실제 실행 결과와 체크포인트로 대체해야 합니다. CALF는 기존 GCN 코어로 의존 순서와 쓰기 충돌을 검증합니다. 같은 저널·작업을 여러 셀에 중복 결속하면 거부하며, 여러 Lane이 공유하는 선행 셀은 전체 합계에서 한 번만 계산합니다. 각 Lane의 `accounting` 소계에는 해당 Lane의 공유 선행 셀이 포함되므로 Lane 소계를 서로 더하면 안 됩니다. `recordedCheckCoverage`는 결속 셀·미결속 셀·알려진 누락 검사 수를 구분합니다. Lane은 논리적인 단일 실행자 계획입니다. 이 보고서로 병렬 실행이나 속도 향상을 추론하지 않습니다.

셀과 작업의 결속은 호출자가 명시한 귀속 관계입니다. 계획의 쓰기 목록과 실제 작업 계약의 범위가 같다는 증명은 아닙니다. 결속이 없는 셀의 `UNBOUND_NOT_OBSERVED`는 실행 여부를 모른다는 뜻입니다. 결속한 저널에 시작 기록이 없으면 `NO_START_RECORDED`로 표시합니다.

계측은 원본의 `process_started`에 결속한 공급자·검토 호출을 셉니다. 실패, 성공, 종료 결과가 확인되지 않은 호출을 구분합니다. 저장된 상태와 결과는 과거 실행 결과로만 표시하며, 등록 검사·보관된 검사 결과·누락 검사 수도 함께 제공합니다. 파일 결속 진단은 표시할 수 있지만 검사를 다시 실행하지 않습니다. 최상위 `currentCompletion`과 검사별 `currentVerification`은 항상 `NOT_EVALUATED`입니다.

체크포인트가 달라졌거나 읽는 중 원본이 바뀌면 결과를 반환하지 않습니다. 현재 쓰기 작업을 중단하거나 원본을 복구하지 않습니다. 쿼리는 저널 관측의 기존 건수·바이트 제한을 따르며, 입력은 최대 512KiB, 출력은 최대 256KiB입니다.

## 시간·사용량·비용

새 네이티브 공급자 호출에는 성공·실패에 관계없이 단조 시계로 측정한 경과 시간이 기록됩니다. `sumProviderElapsedMs`는 호출 시간의 합이며 전체 작업의 벽시계 시간이나 순수 모델 추론 시간이 아닙니다.

내장 어댑터는 공급자가 반환한 숫자 카운터만 선택적으로 수집합니다.

| 공급자 경로 | 입력·출력 토큰 | 캐시 입력 |
| --- | --- | --- |
| OpenAI Responses | 응답의 usage | 응답의 상세 usage |
| Codex CLI | 단일 turn.completed의 usage | 해당 usage |
| 로컬 OpenAI 호환 Chat | 응답의 usage | 응답의 상세 usage |
| Ollama | prompt_eval_count / eval_count | 미제공 |
| Antigravity | 미제공 | 미제공 |

카운터는 공급자 보고값이며 독립 측정값이 아닙니다. `model`은 요청 설정의 모델 식별자입니다. 공급자가 실제로 해석한 모델이나 청구 모델의 동일성을 인증하지 않습니다. 모델을 명시하지 않은 기존 설정은 기본값을 추측하지 않습니다. `providerGroups`는 설정 해시·공급자·요청 모델별 집계입니다.

사용량은 작업·입력 해시에 결속한 일회성 부가 영수증으로 전달하며 기존 공급자 응답 형식은 유지합니다. 누락·오류·과거 실행·명세가 없는 카운터는 `null`로 남습니다. 일부만 알려졌다면 전체 합계는 `null`, `known…`과 관측 호출 수에는 확인된 부분만 나타납니다. `known…: 0`만으로 전체가 0이라고 해석하면 안 됩니다.

비용 추정에는 `rates`에 명시적 단가를 넣습니다. 각 항목은 `provider`, `model`, `sourceSha256`, `inputMicrosPerMillion`, `outputMicrosPerMillion`, `cachedInputMicrosPerMillion`을 사용합니다. 단위는 백만 토큰당 마이크로 USD입니다. 전체 입력에서 캐시 입력을 제외한 토큰에 일반 입력 단가를 적용하고 캐시 입력은 별도 단가로 계산합니다. 호출마다 마이크로 USD 미만을 버립니다.

모든 필요한 토큰 수와 정확히 일치하는 단가가 있을 때만 해당 호출을 가격화합니다. 미관측이나 단가 누락을 무료로 처리하지 않습니다. 단가의 출처 해시는 입력 결속용이며 최신 가격이나 올바른 과금 조건을 검증하지 않습니다. `billedCost`는 항상 `null`이고 추정치는 청구 금액이 아닙니다.

## API와 검증 범위

동일한 요청은 네이티브 API의 `{"op":"evaluation","request":…}`로도 전달할 수 있습니다. UI나 외부 어댑터가 별도의 평가 규칙을 소유하지 않습니다.

검증 범위는 정답·오답·누락 관측, 금지·필수 스킬, 명시적 0과 미관측 사용량, 부분 가격화, 원본 체크포인트 불일치, 성공·실패하는 격리 프로세스의 실제 저널 조회입니다. 합성 공급자의 시험 카운터로 모델의 실제 비용·품질·속도 개선을 주장하지 않습니다. 기존 기록·계약·설정과 실행 중인 작업의 제어는 이 기능의 범위에 포함되지 않습니다.

## 실제 모델 비교 — 2026-11-19

공식 Codex CLI로 GPT-6.2-Sol·Astra에 같은 중간 추론 수준과 단일 시도를 적용했습니다. 금액 계산·반열린 구간 병합·스킬 선택의 격리 과제 3개씩을 실행했고 계획·검토 호출은 합계 12회였습니다. 두 모델 모두 네이티브 검사, 현재 상태 재조회, 별도 검사 재실행에서 3개 과제를 통과했습니다.

| 요청 모델 | 통과 | 과제당 중앙 시간 | 입력/출력 토큰 합계 | Standard API 단가 환산 합계 |
| --- | --- | --- | --- | --- |
| GPT-6.2-Sol | 3/3 | 40.112초 | 145,156 / 3,459 | $0.324902 |
| GPT-6.2-Astra | 3/3 | 38.319초 | 151,341 / 2,780 | $1.321928 |

토큰은 공급자 보고값이며 금액은 3개 과제의 공개 Standard API 단가 환산치입니다. 미보고 캐시 쓰기·서비스 등급 배수·구독 크레딧 과금은 포함하지 않으며 실제 청구액은 미확인입니다. 서버 부하·서비스 등급·캐시 상태를 통제하지 않은 모델당 3개 단일 시도이므로 일반 성능 순위나 반복 가능한 절감률을 뜻하지 않습니다. 생성된 선택 함수를 실행한 필수·금지 선택 4건도 통과했으며 실제 호스트 스킬 호출의 증명은 아닙니다.

[English and official rate sources](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING_EVALUATION.md#real-model-pilot) · [검증 범위](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING-LANE-VERIFICATION.json)
