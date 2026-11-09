# 범용 작업 규약 v1

CALF **1.8.7–1.8.8 / 1.9.2–1.9.3**, SDK **0.2.2**가 필요합니다. [English](WORK_PROTOCOL.md).

Python 문서 정리, Node 데이터 집계, 로컬 HTTP 서비스가 같은 작업·산출물·검수·채택 규약을 사용합니다. AI 모델이나 상주 서비스가 필수는 아닙니다. 연결된 에이전트 하나 또는 앱이 호출할 수 있으며, 코어 실행 엔진은 SDK에 포함되지 않습니다.

## 작업에서 채택까지

`submit`은 요청 키, 목적, Adapter, 매개변수, 입력 해시, 출력 계약, 필수 검사, 시도 예산, 채택 정책을 고정합니다. 입력은 새 작업 폴더에 복사하고 원본은 보존합니다. 같은 키와 같은 계약은 같은 작업을 반환하고, 같은 키로 계약을 변경하면 거절합니다. 접수만으로 실행되지는 않습니다.

`step`은 최초 실행 또는 기존 요청의 상태 조회를 수행합니다. 시도마다 새 후보 폴더와 고유 요청 ID를 사용합니다. 프로세스 EXIT 0 또는 Adapter의 succeeded 응답은 산출물 검수 통과를 뜻하지 않습니다. CALF는 선언한 모든 파일을 확인하고 해시를 계산한 뒤 검사를 실행하며, 입력·도구·산출물 버전이 그대로인지 다시 확인합니다. 검수 영수증에는 검사한 산출물 목록의 해시가 함께 기록됩니다.

`adopt`는 검증된 버전의 참조를 선택합니다. 기존 파일 덮어쓰기·게시·배포는 수행하지 않습니다. manual은 현재 명세 해시를 정확히 지정해야 하고, automatic은 최초 계약에서 허용해야 합니다. 이전 시도와 채택 이력은 보존합니다. 이전 채택을 다시 선택하는 API는 아직 없습니다.

## 사용 방법

```python
from calf_sdk import CalfClient
client = CalfClient('/absolute/calf', '/absolute/records', timeout=35)
accepted = client.work('submit', spec=work_spec)
result = client.work('step', work=accepted['work'])
verified = client.work('inspect', work=accepted['work'])
assert verified['verified'] and verified['outcome'] == 'SATISFIED'
```

```js
import {CalfClient, isSatisfied} from './node/index.mjs';
const client = new CalfClient('/absolute/calf', '/absolute/records');
const accepted = await client.work('submit', {spec: workSpec});
await client.work('step', {work: accepted.work});
const result = await client.work('inspect', {work: accepted.work});
if (isSatisfied(result)) console.log(result.manifest.digest);
```

Windows에서는 calf.exe와 인터프리터·기록 폴더의 절대 경로를 사용합니다. 출력의 상대 경로 구분자는 `/`입니다. SDK 제한 시간은 작업의 실행 제한 시간과 종료 정리 시간보다 길게 설정합니다. 통신 실패가 나면 무조건 다시 실행하지 말고 inspect/step으로 기존 요청을 확인합니다. SDK는 호스트 설정이나 자격증명을 자동 변경하지 않습니다.

| 호출 | 동작 |
|---|---|
| register | 실행 파일·Adapter 파일·역할·기능을 해시로 고정합니다. 기존 ID 교체는 거절하므로 버전별 ID를 사용합니다. |
| adapters / list | 로컬 등록 정보와 작업 식별자를 제한된 크기로 조회합니다. |
| submit | 계약과 입력을 고정합니다. 실행은 별도입니다. |
| inspect | 기록과 현재 파일 버전, 채택 유효성을 확인합니다. 실행 중 임시 표시는 unverified/UNKNOWN입니다. |
| step | 실행 또는 기존 비동기 요청 조회·검수를 진행합니다. 한 번의 호출로 완료되지 않을 수 있습니다. |
| cancel | 취소 요청만 남깁니다. step/query로 실제 종료를 확인해야 합니다. |
| retry | 종료된 작업에 남은 예산이 있으면 새 시도를 준비합니다. 기존 후보와 채택은 보존합니다. |
| recheck | 산출물을 다시 만들지 않고 현재 후보만 검사합니다. |
| adopt | 현재 검수 통과 명세의 정확한 digest를 지정해 채택합니다. |

[JSON Schema](../schemas/work-v1.schema.json), [실행 예제](../examples/universal_work.py), [Python Adapter](../examples/runtime_text.py), [Node Adapter](../examples/runtime_data.mjs), [독립 Validator](../examples/validator_text.py), [HTTP Adapter](../examples/runtime_http.py)를 참고하세요.

## Adapter 규약

등록한 명령은 셸 문자열이 아닌 argv 배열입니다. CALF가 마지막 인수에 요청 JSON 파일의 경로를 붙입니다. 환경은 지운 뒤 소수의 시스템·임시 경로 변수만 전달하며 자격증명은 상속하지 않습니다. 실행할 때만 프로세스를 띄우고, 기존 프로세스 그룹 관리와 Windows Job Object 종료 처리를 사용합니다. 인터프리터와 선언한 파일은 실행 전후 확인합니다. 모든 전이 의존성·OS 파일까지 검증하는 것은 아니므로 Adapter 배포자가 의존성을 고정해야 합니다.

요청은 `calf.runtime.v1`이며 operation, requestId, work, attempt, providerJobId, parameters, inputs, outputs, outputDirectory, extra를 포함합니다. operation은 execute/query/cancel/validate입니다. 응답은 stdout에 JSON 하나, 진단은 stderr에 기록합니다.

```json
{"schema":"calf.runtime.v1","requestId":"work-...:1","state":"succeeded","providerJobId":null,"usage":null}
```

상태는 running/succeeded/failed/cancelled/unknown/not_found입니다. 동기 Adapter는 running/unknown을 반환할 수 없습니다. 비동기 Adapter는 응답 유실로 providerJobId를 받지 못했어도 requestId로 조회할 수 있어야 합니다. 알려진 providerJobId는 바꿀 수 없습니다. not_found는 접수된 작업이 없다는 확정 조회 결과여야 하며 타임아웃을 대신 표시하면 안 됩니다. 불확실한 작업은 실행 슬롯을 계속 점유하며 새 execute 호출로 대체하지 않습니다. HTTP 예제는 loopback 전용이고 프록시·리다이렉트·자동 재전송이 없습니다.

Validator는 별도 프로세스로 실행되며 checkId, manifestDigest, outcome(SATISFIED/VIOLATED/UNKNOWN), reason을 반환합니다. 내장 검사는 SHA-256 일치, JSON Pointer 값 일치, 텍스트 포함입니다. 모든 산출물은 적어도 하나의 검사가 필요합니다. 이 규칙이 작업의 의미적 품질까지 자동 보장하지는 않습니다. 품질과 업무 규칙을 확인하려면 작업에 맞는 검사를 마련해야 합니다.

## Local MCP

`calf work-mcp /absolute/records`는 MCP 2025-11-25 JSON-lines stdio 서버입니다. 기본 도구는 work_list, work_inspect, work_adapters입니다. `--control`로 submit/step/cancel/retry/recheck/adopt를 추가합니다. Adapter 등록은 MCP에 노출하지 않습니다. Python의 work_mcp_server(control=True), Node의 workMcpServer({control:true})는 실행 설정만 반환하고 호스트 설정을 쓰거나 서버를 띄우지 않습니다. 기존 Local Sources MCP는 그대로입니다.

MCP 도구 사용 권한은 호스트가 결정합니다. explicit-client는 허용된 클라이언트 호출 기록이지 사람이 직접 클릭했다는 증명은 아닙니다. 다중 에이전트 조정이나 sampling은 추가하지 않습니다. 서버는 순차 호출을 처리하므로, 긴 step 실행 중 취소는 별도의 API/SDK 프로세스에서 요청합니다. 별도의 inspect 호출은 실행 중이라는 표시와 함께 아직 검증되지 않은 임시 상태를 반환합니다.

## 경량화·보존·보장 범위

* 계약 <48KiB, 고정 계약·요청 ≤64KiB, 입력 16개·출력 16개·검사 32개·시도 8회 상한입니다. 입력 합계·출력 합계·개별 파일은 최대 512MiB이며 Adapter는 더 작은 제한을 둘 수 있습니다.
* 출력 목록은 112항목/6단계 디렉터리/파일 16개 이하입니다. 텍스트·JSON 검사는 1MiB 이하만 읽고 해시·복사는 32KiB씩 처리합니다. 기존 제한된 프로세스 출력을 사용하며 응답 JSON은 64KiB 이하입니다. 이력 전체 적재·벡터 DB·모델·새 상주 캐시는 없습니다.
* 기존 자원 Fader와 worker.lock을 재사용합니다. 같은 기록 폴더에서는 아직 끝나지 않은 범용 작업 하나만 실행하며, 기존 코드 워커와도 차례를 조정합니다. 다른 home은 별개의 실행 범위입니다.
* 새 기록은 work-v1 아래에만 추가됩니다. 기존 기록·설정·계약·자료 조회 MCP는 그대로 사용합니다. 작업 시작 시 코어 실행 파일을 보존해 업데이트 뒤에도 같은 런타임으로 이어갑니다. 보존 런타임이 없거나 변경되면 차단합니다.
* 프로세스 정리나 비동기 종료를 확인하지 못하면 UNKNOWN과 점유 상태를 유지합니다. 동기 프로세스 종료 영수증만 있고 응답이 유실된 경우에는 성공을 추정하지 않고 UNKNOWN으로 종결합니다. 종료 영수증 이전의 비정상 중단은 호스트 수준 확인이 필요할 수 있습니다.
* 파일 해시를 비교해 각 확인 시점의 파일을 기록된 해시와 대조합니다. OS 샌드박스나 악성 프로세스에 대한 완전한 격리가 아닙니다. 신뢰할 수 있는 등록 Adapter를 적절한 호스트 권한 안에서 실행해야 합니다. 출력 상한은 수집 시 검사하며 커널 디스크 할당량은 아닙니다. 현재 범용 규약은 파일로 저장되는 산출물을 다룹니다. DB 변경·결제·임의 앱 부작용은 별도 Adapter와 검증 계약이 필요합니다.
* usage는 제공자 보고 메타데이터로만 보존하며 검증된 비용 장부나 환불 보장은 아닙니다. 금액 예산 관리와 원격 서비스 인증은 별도로 구현해야 합니다. Workbench Runtime Work에서 같은 기록과 단계 흐름을 조회합니다. 최종 Windows/Linux 실검증 결과는 VERIFICATION.json에 기록합니다.

Workbench의 Runtime Work에서 같은 기록을 열고 실행·조회 재개·취소·재검수·채택할 수 있습니다. Windows·Linux를 포함한 배포 파일별 검증 범위는 배포판 VERIFICATION.json을 참고하세요.
