# 작업 파일의 소유권·격리·복원

[English](ARTIFACT_LIFECYCLE.md) · [설계 점검](ARTIFACT_LIFECYCLE_DESIGN.md)

하네스 1.8.16 · 워크벤치 1.9.12 · SDK 0.2.9 기준입니다.

기존 기록에 연결된 파일을 모아 어느 작업에서 필요로 하고 왜 보존해야 하는지 보여줍니다. CALF가 새로 만드는 작은 임시 파일에는 생성 근거·참조·보존 기한도 붙일 수 있습니다. 기존 Rust 코어와 저널을 활용하며, 별도 DB·상주 감시기·AI 호출·프로세스 샘플러를 추가하지 않습니다.

## 조회 방법

새로 빌드한 코어의 `artifacts` 명령에 아래 JSON을 표준 입력으로 전달합니다. 경로와 작업 ID는 실제 값으로 바꾸세요. Windows에서는 절대 Windows 경로를 사용합니다.

```json
{"operation":"inventory","source":"native","workspace":"/absolute/project","task":"registered-task","limit":128,"hashBudgetBytes":8388608}
```

`native`는 기존 TASK·CHECK 계약 범위와 호스트 실행 기록을 읽습니다. 외부 에이전트가 어느 파일을 처음 만들었는지까지 확정하지는 않습니다. 전체 범위의 CHECK 해시를 개별 파일 해시로 바꿔 표시하지 않습니다.

독립 실행·범용 런타임 기록은 다음 요청으로 읽습니다.

```json
{"operation":"plan","source":"journal","workspace":"/absolute/project","state":"/absolute/records","task":"recorded-task"}
```

저장된 저널의 작업 폴더 식별자가 일치해야 합니다. 범용 런타임의 경우 `workspace`는 해당 작업의 폴더, `state`는 그 안의 `records` 폴더입니다. 기록된 파일 변경, 변경 전후·복구 스냅샷, 프로바이더 입력 참조와 시도별 후보 파일을 확인합니다. 이전 후보도 보존 대상으로 유지합니다.

기존 코어의 desktop/SDK API로도 같은 요청을 전달할 수 있습니다.

```json
{"op":"artifacts","request":{"operation":"inventory","source":"native","workspace":"/absolute/project"}}
```

이 코어 요청은 전송 문맥에 `home`이 있어도 폴더를 만들지 않습니다. Workbench의 Artifacts 화면에서 필요할 때만 조회할 수 있습니다. 새 MCP 도구는 설치하지 않습니다.

## 결과를 읽는 기준

- `owners`와 `references`는 연결된 작업과 원본 기록을 보여줍니다. 작업 하나로 필터해도 같은 경로를 참조하는 다른 작업의 연결은 유지합니다. 참조 전체 개수와 최근 8개 근거를 제공합니다.
- `RECORDED_CREATE`는 이전 파일이 없었고 코어의 쓰기가 완료됐다는 근거가 있을 때만 표시합니다. `lineage`로 시작·완료 기록을 연결합니다. 삭제 권한을 뜻하지는 않습니다. 후보 목록에서는 작업·시도·관측 시점을 연결하며, 기록에 없는 실제 파일 생성 시각을 만들어 표시하지 않습니다.
- `retentionReasons`에는 계약·검사 입력·소스·원본 기록·복구 스냅샷·후보를 남겨야 하는 이유가 표시됩니다.
- 파일 상태는 일치·변경·존재·없음·미확인·해시 예산 초과를 구분합니다. 원본 기록과 재생성 가능한 인덱스는 메타데이터만 조회하며 기록 체인은 별도로 검증합니다. `RECORD_SET`은 보존된 저널 조각의 묶음입니다.
- `exactContentGroups`는 이번 응답에서 실제 해시를 확인한 동일 내용의 경로입니다. 같은 파일을 workspace와 state에서 두 번 가리키는 경우는 중복 용량에서 제외합니다. 하드링크·압축·파일시스템 자체 중복 제거는 측정하지 않아 실제 확보 공간은 미확인으로 둡니다.
- `pendingOperations`는 시작·종료 기록이 맞지 않거나 정리가 미확인인 실행입니다. 실제 OS 생존 여부와는 다릅니다. PID가 보이지 않는다는 이유로 종료를 확정하거나 프로세스를 종료하지 않습니다. 다른 작업의 미종결 실행도 전체 개수에 반영합니다.
- `KEEP`, `REVIEW`, `REBUILDABLE_INDEX_REVIEW`, `MANAGED_QUARANTINE_REVIEW`는 보존·검토 제안입니다. `inventory`와 `plan` 모두 읽기 전용이며, 실행 권한과 실제 확보 공간은 각각 false와 0입니다.

## 생성할 때부터 소유권을 기록하는 관리 파일

CALF가 직접 만드는 새 임시 메모·로그·캐시 텍스트에만 적용하는 선택 기능입니다. 기존 파일을 가져와 정리 대상으로 재분류하지 않습니다. 소스·검사 입력·후보·계약·복구 근거는 계속 보호합니다.

```json
{"operation":"create","source":"journal","workspace":"/absolute/project","state":"/absolute/records","task":"registered-task","requestId":"build-note-1","role":"temporary","label":"빌드 메모","content":"작은 임시 메모\n","retentionSeconds":86400,"confirm":true}
```

해당 저널에 이미 등록된 작업만 사용할 수 있습니다. 코어가 `state/managed-artifacts/ID/payload`에 새 경로를 정하고, 쓰기 전에 의도를 기록한 뒤 실제 내용과 해시를 대조해 생성 근거를 남깁니다. UTF-8 텍스트는 파일당 16KiB, 저널당 128개로 제한합니다. 기본 보존 기간은 24시간, 최대 30일이며 저장된 생성 의도 시각부터 계산합니다. 기한이 지나도 자동 삭제하지 않습니다.

같은 작업의 `requestId`는 역할·이름·내용·보존 기간이 같은 요청에만 재사용합니다. 재요청은 현재 상태만 조회하며 쓰기를 반복하지 않습니다. 생성 중 중단돼 근거가 완성되지 않았다면 미확인으로 남기고, 재요청으로 완료 근거를 만들어 붙이지 않습니다.

다른 등록 작업에서 필요하면 `pin`으로 참조를 추가합니다. 작업이 종료된 기록을 확인한 뒤 해당 작업의 참조만 명시적으로 해제할 수 있습니다.

```json
{"operation":"release","source":"journal","workspace":"/absolute/project","state":"/absolute/records","task":"registered-task","artifactId":"RETURNED_ARTIFACT_ID","confirm":true}
```

`pin`도 같은 형식입니다. 모든 활성 참조가 해제되고 보존 기한까지 지나야 격리를 검토할 수 있습니다. 작업 재개·미종결 실행·불완전한 조회·파일 변경·미완성 생성 근거가 있으면 차단합니다. 참조 해제만으로 파일을 옮기거나 작업 완료를 판정하지 않습니다.

Workbench에서 종료된 작업을 선택하고 **Review reference release**를 누르면 그 작업의 참조만 확인 후 해제합니다. 다른 작업의 참조와 보존 기한은 화면에 계속 표시합니다.

Python은 `client.artifacts(workspace, operation="plan", state=state)`, Node는 `client.artifacts(workspace, {operation: "plan", state})`로 조회합니다. SDK에 관리 파일 예제를 포함했습니다. SDK는 같은 코어에 요청을 전달하며 저널을 직접 수정하지 않습니다.

## 경량화와 적용 범위

알려진 경로는 최대 512개, 기본 출력은 128개이며 최대 256개까지 표시합니다. 추가 파일 해시는 기본 8MiB, 최대 64MiB의 합산 예산 안에서 기존 32KiB 버퍼로 계산합니다. 0이면 산출물 내용을 읽지 않습니다. 실패한 읽기도 예약 예산에 포함하며 `hashBytesUpperBound`로 표시합니다. 기록 체인을 읽는 기존 한도는 별도로 적용됩니다.

한도를 넘으면 `TRUNCATED`를 표시합니다. 내부 경로 한도에 도달했는지는 `knownPathsLowerBound`로 구분합니다. 기록 밖에서 생성된 파일은 탐색하거나 분류하지 않으며, 목록에 없다는 사실이 삭제 가능하다는 뜻은 아닙니다. 오래된 파일·미추적 파일·중복 파일이라는 이유만으로 사용자 소스나 DB를 정리 대상으로 확정하지 않습니다.

경로 이탈·링크·특수 파일·바뀐 기록과 해시는 거부하거나 미확인으로 남깁니다. 일반적인 동시 변경은 재확인하지만 악의적인 변경 후 원상복구까지 차단하는 OS 격리 장치는 아닙니다. 현재 작업의 완료 판정과 기존 승인 정책은 그대로 유지합니다.

## 인덱스 격리와 복원

Workbench에서 **Artifacts**를 열고 작업 공간 기록 또는 해당 공간의 작업 기록을 선택한 뒤 새로고침합니다. **Preview index quarantine**은 이동할 파일과 지문만 보여줍니다. 내용을 확인하고 **Confirm quarantine**을 눌러야 이동합니다. 보관된 항목은 **Review restore**로 살펴본 뒤 별도로 복원을 확인합니다.

CLI·API에서도 같은 순서로 사용할 수 있습니다.

```json
{"operation":"prepare","source":"native","workspace":"/absolute/project"}
```

응답의 `plan.operationId`와 `digest`를 다음 요청에 넣습니다.

```json
{"operation":"quarantine","source":"native","workspace":"/absolute/project","operationId":"RETURNED_ID","digest":"RETURNED_DIGEST","confirm":true}
```

보관 현황은 확인 필드 없이 `operation: "retained"`로 조회합니다. 같은 작업 식별자·지문과 확인 필드로 `restore`를 요청하면 해당 사본을 복원합니다. 런타임 기록은 매 요청에 `source: "journal"`과 원래 `state` 경로를 사용합니다.

지문과 확인 필드는 요청한 동작을 특정하는 값입니다. 호스트 실행 권한을 부여하거나 사람의 승인을 증명하지는 않으며, 호출자의 기존 실행 권한이 그대로 적용됩니다.

인덱스는 `.calf/ontology.sqlite` 또는 저널의 `index.sqlite`만 대상으로 하며, DB 구조와 내용이 현재 기록으로 재생성 가능한지 대조합니다. 관리 파일은 코어의 생성 근거가 완성됐고 모든 참조가 해제됐으며 보존 기한이 지난 경우에만 대상이 됩니다. 해당 파일의 prepare·quarantine·restore 요청에는 매번 `"domain":"state","path":"managed-artifacts/ID/payload"`를 함께 넣습니다. 실행 중인 작업·보존 참조·하드링크·알 수 없는 DB 내용·SQLite 임시 트랜잭션 파일이 있으면 차단합니다. 기존 로그·소스·테스트·설정·계약·복구 스냅샷·후보 파일과 미분류 DB는 옮기지 않습니다.

인덱스 옆의 비공개 폴더에 파일 전체를 보관하므로 **격리만으로 디스크 여유 공간이 늘어나지는 않습니다.** 이동 전에 의도를 기록하고, 마지막 영수증이 남기 전에 중단됐더라도 실제 두 위치와 해시를 대조해 상태를 확인합니다. 영구 삭제 기능은 제공하지 않습니다.

원래 위치에 새 파일이 있으면 덮어쓰지 않습니다. 인덱스는 원본 기록이 바뀐 경우에도 복원을 차단합니다. 관리 파일은 이후 참조가 추가됐더라도 원래 생성 근거와 파일 내용이 일치하고 미종결 실행이 없으면 복원할 수 있습니다. 충돌을 확인하기 전 자동 재시도하거나 기록·설정을 되돌리지 않습니다. 일반적인 동시 변경과 실행 중단을 다루는 기능이며, 악의적인 파일시스템 변경을 격리하거나 모든 저장장치의 전원 장애 복구를 보장하는 장치는 아닙니다.

## 검증

최종 실행 파일 해시·운영체제별 결과·실제 창 조작 여부는 릴리즈의 `VERIFICATION.json`을 확인하세요. 합성 작업으로 실제 실행과 독립 검사를 확인하며, 새로운 유료 AI 시험을 수행했다는 뜻은 아닙니다. 아래는 인덱스만 다루던 이전 개발 단계의 기록으로, 이후 관리 파일 기능의 검증 근거와 구분합니다.

### 이전 인덱스 전용 개발 검증

macOS에서 수명 관리 검사 20개를 포함해 코어 검사 130개를 통과했습니다. 같은 수명 관리 검사를 Windows에서 18개(Unix 전용 2개 제외), Linux에서 20개 실행해 통과했습니다. 세 운영체제 모두 실제 CLI·Workbench API로 합성 인덱스를 격리·복원하고, 새 파일이 생긴 위치로의 복원을 차단했습니다. 보호 파일의 내용과 수정 시각도 유지했습니다. 새 UI 동작 검사 6개는 세 환경에서, 전체 UI 검사 43개는 Mac과 Linux에서 통과했습니다. 세 환경의 네이티브 UI 빌드도 확인했습니다.

Mac Workbench 실제 창에서도 미리보기·확인·격리·복원을 조작해 결과를 확인했습니다. Windows·Linux는 네이티브 실행·API 연결·UI 동작 검사까지 검증했으며, 실제 창의 클릭은 관측하지 않았습니다. 추가 AI 호출이나 전역 설정 변경은 없었습니다. 공개 패키지·설치된 호스트 훅·기존 사용자 앱은 아직 변경하지 않았습니다.
