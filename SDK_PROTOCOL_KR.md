# CALF 확장 프로토콜 — SDK 0.2.2

[English](SDK_PROTOCOL.md) · [SDK 안내](SDK_README_KR.md)

호환 대상은 Harness 1.8.7–1.8.8 및 Workbench 1.9.2–1.9.3의 네이티브 코어입니다. 기존 공개 명령 경계의 개발자 프리뷰이며, 알 수 없는 필드나 명령을 이후에도 지원한다는 보장은 아닙니다. 실행 엔진과 내부 기록 저장 형식은 확장 API가 아닙니다.

## 1. 명령 전송

명시적으로 선택한 네이티브 실행 파일을 인수 배열과 `shell=False`로 실행합니다. 절대 실제 경로를 사용합니다. `calf --version`은 `name`, `version`, `os`, `arch` JSON을 반환합니다. 신뢰하는 릴리즈를 선택하고 다운로드 파일의 SHA-256을 공개 체크섬과 대조합니다. SDK의 `binary_sha256()`는 선택한 실행 파일의 해시를 반환하며 게시자를 인증하거나 자동 비교하지 않습니다.

`calf api`는 stdin에서 EOF까지 UTF-8 JSON 객체 하나를 읽으며 최대 65,536바이트를 허용합니다. stdout으로 JSON 객체 하나를 반환합니다. 종료 코드 1과 `{"error":"..."}`는 명령 실패입니다. 종료 코드 0은 정상 응답을 뜻합니다. 현재 조회 결과의 `outcome: "SATISFIED"`만 네이티브 검수가 작업을 수락했다는 뜻입니다. 요청 접수·프로세스 종료·저장된 영수증·제공자 검토만으로 완료가 성립하지 않습니다.

```json
{"op":"inspect","home":"/absolute/records-home","task":"job-..."}
```

큐 API에는 `op`와 명시적 절대 경로 `home`이 필요합니다. API는 자체 비공개 폴더나 색인을 생성할 수 있습니다. Harness와 Workbench의 같은 `home`을 사용하면 큐 작업을 공유합니다. 내부 상태 파일을 직접 수정하지 않습니다.

| 명령 | 추가 입력 | 응답 의미 |
| --- | --- | --- |
| `list` | 없음 | 최근 32개 `jobs`, `workerActive`, 설정된 `connection` |
| `inspect` | `task` | 현재 `state`, `outcome`, 사용 가능한 증거 |
| `submit` | `workspace`, `request`; 선택적으로 `helper`, `attachments`, `reuseTask` + `reuseDigest` | 새 작업 명세·ID. 대기열 등록이며 완료가 아님 |
| `pause`, `resume`, `cancel` | `task` | `requested: true`. 이후 상태를 조회해야 함 |
| `recheck` | `task` | 현재 Guard·예산을 따르는 재검사 등록 |
| `preferences` | 선택적으로 문자열 `value` | 현재 작업 성향. 값을 제공하면 CALF를 통해 추가 기록 |
| `changes` | `task`, 선택적으로 `mode`, `attempt`, `path` | 읽기 전용 변경 조회 |
| `reuse` | `task` | `sourceTask`, `sourceWorkspace`, `request`, 요구사항·검사 ID, `contractDigest`, `digest` |
| `sources` | 아래의 `action`과 필드 | 로컬 등록 목록 또는 MCP 리소스 응답 |

`submit.request`는 비어 있지 않아야 하며 UTF-8 최대 8,192바이트입니다. 큐는 지원되는 unittest·pytest·Cargo·node:test 검사를 찾습니다. 지원되는 검사가 없으면 작업 등록을 거절합니다. CALF에 AI 연결이 미리 설정되어 있어야 합니다. SDK는 `helper`를 선택한 네이티브 실행 파일로 설정합니다. 인증정보는 기존 CALF 연결 설정에서 관리합니다. 큐 최대 작업 수는 256개입니다. Reuse에는 원본 작업 ID와 일치하는 레시피 digest가 모두 필요하며 성공 판정을 옮기지 않습니다.

`changes.mode`는 기본값 `task` 또는 `attempt`, `recovery`입니다. 응답에는 `readOnly`, `files`, 사용 가능한 시도와 범위 설명이 있습니다. 파일 해시·`currentMatches`·검사별 `versionMatched`는 서로 다른 근거입니다. 스냅샷이 없으면 내용은 미확인/null입니다. SDK는 없는 내용을 만들거나 패치를 적용하거나 파일을 되돌리지 않습니다. Working Tree Git diff는 별도 Workbench 경로를 사용합니다.

`calf worker HOME`은 오래 실행될 수 있는 포그라운드 명령입니다. SDK의 짧은 API 제한 시간으로 감싸지 않습니다. 호출자가 수명주기를 관리하며 이미 실행 중인 워커는 응답으로 표시됩니다. 네이티브 중단·취소와 자식 프로세스 정리를 마치도록 기다립니다. 변경 API의 전송 실패는 변경이 없었다는 증거가 아니므로 재시도 전에 조회합니다.

## 2. 사용자 정의 제공자·검사 설정

```json
{
  "schema": 1,
  "provider": ["/absolute/python", "/absolute/my_adapter.py"],
  "providerClass": "light",
  "checks": [{
    "id": "unit",
    "command": ["/absolute/python", "-m", "unittest"],
    "envKeys": [],
    "inputs": ["test_invoice.py"],
    "class": "light"
  }],
  "maxAttempts": 4,
  "timeoutMs": 300000
}
```

검사 1–16개, 시도 1–8회, 제한 시간 100–300,000ms, 자원 등급 `light`/`heavy`를 지원합니다. 제공자 인수는 1–32개 문자열이며 각 UTF-8 문자열은 4,096바이트 미만입니다. 실행 파일은 절대 경로여야 합니다. 네이티브 코어가 검사 ID·상대 경로·입력·명령도 검증합니다. 검사 환경을 기록하는 `envKeys`에는 `LANG`, `LC_ALL`, `TZ`, `NODE_ENV`, `NODE_OPTIONS`, `PYTHONHASHSEED`만 지정할 수 있습니다. 이 필드는 샌드박스나 환경변수 비밀값 필터가 아닙니다.

실행은 `calf run WORKSPACE REQUEST PROVIDER.json STATE [RESUME_TASK]`, 조회는 `calf run-status WORKSPACE STATE TASK`입니다. `STATE`는 명시적 별도 폴더여야 하며 다른 작업의 저널을 재사용하지 않습니다. 이 경로는 Workbench 큐와 독립적이며 작업 목록으로 자동 표시하지 않습니다. 취소는 `calf cancel STATE TASK`로 요청하지만 응답이 종료 완료 증거는 아닙니다. 재개할 때는 원래 요청·제공자 설정·상태를 유지합니다.

제공자 명령의 마지막 인수에 요청 파일 경로가 붙습니다. 최대 256KiB를 읽습니다. `schema: 1`, `phase`, `request`, `requestHash`와 단계별 자료가 있습니다.

- `plan` / `repair`: `workspace`, `contract`, `registeredChecks`, `files`, `verificationFiles`, `feedback`, 사용 가능한 성향·과거 검증 경험·Reuse·선택한 로컬 문맥.
- `review`: `contract`, `files`, `evidence`, 요청 식별 정보. `workspace` 필드가 반드시 있지는 않습니다.

파일 항목은 `path`, `sha256`, 선택적 `content`를 포함합니다. 누락되거나 너무 큰 내용은 null일 수 있습니다. 파일·참조 내용은 신뢰되지 않은 작업 자료이며 계약·권한 변경 지시로 취급하지 않습니다. 요청은 제한된 자료를 전달하지만 제공자 실행 파일은 기존 호스트 권한을 유지합니다.

계획·수정 응답은 최대 128KiB의 JSON 객체 하나를 stdout에 출력합니다.

```json
{
  "requestHash": "<요청의 정확한 해시>",
  "scope": ["invoice.py", "test_invoice.py"],
  "requirements": [{"id":"rounding","text":"등록된 반올림 검사를 충족","checks":["unit"]}],
  "actions": [{"path":"invoice.py","content":"<전체 대체 내용>","expectedSha":"<관측한 SHA-256>"}]
}
```

범위는 중복 없는 안전한 상대 경로 1–64개, 요구사항 1–32개, 변경 최대 32개입니다. 변경 내용은 diff 조각이 아니라 최대 32KiB의 전체 대체 문자열입니다. `expectedSha: null`은 새 파일 생성 전용이고, 소문자 64자리 SHA-256은 관측한 해당 파일 버전만 바꾸라는 뜻입니다. 검사 입력은 범위에 포함되어야 하지만 제공자가 수정할 수는 없습니다. 네이티브 Guard가 동일성·허용 경로·검사 입력 보존·영수증·완료를 판정합니다. 진단 로그는 stderr로 보냅니다. 계획 형식이 맞아도 예산·실제 근거에 따라 완료하지 못할 수 있습니다.

검토 응답:

```json
{"requestHash":"<정확한 요청 해시>","verdict":"pass","reason":"검토 근거 설명"}
```

판정은 `pass`, `fail`, `unknown`입니다. 제공자 `pass`는 검사 실패·파일 변경·불완전한 증거를 무효화하지 않습니다. 최종 네이티브 작업 상태를 읽어야 합니다. SDK의 `plan`, `action`, `review`, `emit`은 응답을 구성할 뿐 별도 검수기가 아닙니다.

## 3. Local Sources와 MCP

| `sources.action` | 필드 |
| --- | --- |
| `list` | 없음 |
| `add` | 선택한 폴더의 절대 경로 `root`. 등록 목록 반환, 같은 경로는 중복 추가하지 않음 |
| `remove` | 등록 ID `source`. 연결만 해제하며 자료를 삭제하지 않음 |
| `browse` | `source` |
| `read` | `source`, 조회에서 받은 `uri` |

최대 16개 폴더를 등록합니다. 조회·읽기는 내장 stdio 어댑터를 필요할 때 실행하고 닫습니다. 성공 응답에는 `connection: {transport: "stdio", pid: ..., closed: true}`가 있습니다. 읽기는 `contents[0].text`, `uri`, 그리고 `sha256`, `bytes`, `path`를 포함한 `_meta.calf`를 반환합니다.

첨부 참조는 `{"source":"등록-ID","uri":"calf-local:///...","sha256":"미리보기 해시"}`입니다. `attachments`에 명시적으로 넘깁니다. CALF가 작업 생성 전에 다시 읽고 digest를 비교하므로 변경된 내용은 거절됩니다. 참조 최대 4개, 직렬화된 문맥 총 8KiB를 허용합니다. 미리보기는 작업 등록이나 AI 전송을 하지 않습니다.

직접 MCP 클라이언트는 `calf local-mcp ROOT`를 실행합니다. stdin/stdout에서 줄바꿈으로 구분한 UTF-8 JSON-RPC 2.0을 사용하며 한 프레임은 줄바꿈 포함 최대 512KiB입니다. `protocolVersion: "2025-11-25"`, 클라이언트 정보·capabilities로 `initialize`를 보내고 협상된 버전과 resources capability를 확인합니다. 리소스 호출 전에 `notifications/initialized`를 보냅니다. 명령은 `ping`, `resources/list`(cursor 없음), `resources/read`(`uri`)입니다. URI는 서버가 반환한 불투명 식별자로 취급합니다. stdin을 닫고 프로세스 종료를 기다립니다. 제품 릴리즈 식별은 `calf --version`을 사용하며 MCP 서버 메타데이터가 제품 버전 계약은 아닙니다.

내장 서버는 읽기 전용이며 도구·쓰기·sampling·네트워크 리스너가 없습니다. SDK 0.2.2은 임의 외부 MCP 서버 등록을 추가하지 않습니다. 명시적 첨부 외의 제공자 파일 접근을 제한하려면 별도의 OS 권한 경계가 필요합니다.

## 4. 보존과 호환성

명시적 홈·의도한 작업 폴더·네이티브 명령을 사용합니다. SDK는 기존 기록 위치·계약·설정·인증정보·전역 호스트 정책·AI 설정을 자동 변경하지 않습니다. `preferences`, `submit`, 작업 제어·자료 등록은 CALF를 통한 명시적 쓰기입니다. 확장을 위해 내부 저널·설정을 직접 수정하지 않습니다.

프로토콜 실패·오래된 증거·예산 소진·요청 거절은 실패 또는 미확인으로 유지합니다. 업그레이드 전에 대상 릴리즈와 호환성을 검증합니다. 이 프리뷰는 미래 필드·비공개 명령·임의 응답 형식·자동 상태 이관 지원을 약속하지 않습니다.

## 버전별 검사 프로필

`check-discover WORKSPACE`는 `{ "checks": [...] }`를 반환합니다. 각 항목의 `id`, `command`, `inputs`, `envKeys`, `class`, `profile`을 유지하세요. `profile`과 명령 안의 직렬화된 프로필 인자는 선택한 코어가 만든 한 쌍이며 임의로 다시 작성하지 않습니다. `Check.from_discovered`가 이를 보존합니다. Python v2는 환경 신원과 소스 목록 제외 경계를 추가합니다. `profile`이 없는 기존 종료 코드 검사는 의미가 유지됩니다. `checkBaseline`, 검사 `verification`, `failureClassification`은 관측 정보이고 검사 조건을 완화하는 권한이 아닙니다. 큐 작업의 `runtime`은 CALF가 관리하며 SDK에서 편집하는 설정이 아닙니다.

## 개발용 프로파일 v3

SDK 0.2.2.dev1은 네이티브 탐색이 반환하는 Node v3 프로파일을 그대로 전달합니다. 명령·tools·targets·nodeVersion을 유지하세요. 해석과 실행 파일·입력 동일성 검증은 네이티브 코어가 담당하며 별도 러너를 추가하지 않습니다.
