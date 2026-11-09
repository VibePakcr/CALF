# CALF Harness 1.8.10 · Workbench 1.9.5 · SDK 0.2.3

Saved execution results and the current observer verdict now appear separately in status JSON and Workbench **Task status**. You can inspect recorded CHECK results, file-version binding and differences such as `LC_ALL: Not set → C.UTF-8`. Managed task cards also offer an expandable status summary.

The current top-level outcome remains authoritative. Context differences keep `UNKNOWN`; failed checks keep `VIOLATED`. No environment normalization, weaker check, new agent, model, daemon or GPU compute is introduced. Details load on demand.

New checks save redacted diagnostic context in backward-readable records. Older receipts without field details are labelled unavailable. An optional later observation is accepted only when its full context digest matches the original CHECK, and is labelled as a later observation. Original CHECKs, prior versions, contracts and settings are retained.

SDK 0.2.3 adds `registered_tasks` and `registered_status`, plus a runnable status example. Extensions and adapters cannot promote historical success into current completion. Python, Node, MCP and generic adapter interfaces remain compatible.

See [downloads](DOWNLOADS.md), [English guide](STATUS_CONTEXT.md), [한국어 안내](STATUS_CONTEXT_KR.md) and [verification](VERIFICATION.json). Verification records distinguish fresh platform checks from reused earlier host/UI evidence. No new paid AI session or memory benchmark is included.

## 한국어

상태 조회 JSON과 Workbench의 **Task status**에서 저장된 실행 결과와 현재 조회 판정을 나눠 보여줍니다. 당시 CHECK 결과, 파일 버전 일치 여부와 `LC_ALL: Not set → C.UTF-8` 같은 문맥 차이를 확인할 수 있습니다. 관리형 작업 카드에도 펼쳐 볼 수 있는 상태 요약을 넣었습니다.

완료 여부는 기존 최상위 판정으로 판단합니다. 문맥이 다르면 `UNKNOWN`, 검사가 실패하면 `VIOLATED`를 유지합니다. 환경 변수를 맞추거나 검사 조건을 낮추지 않습니다. 에이전트·모델·상시 프로세스·GPU 연산도 추가하지 않았습니다. 상세 정보는 열었을 때만 불러옵니다.

새 검사는 민감한 값을 가린 진단 정보를 기존 CALF에서도 읽을 수 있는 기록에 추가합니다. 과거 영수증에 항목별 정보가 없으면 확인할 수 없다고 표시합니다. 나중에 문맥을 관측할 때는 전체 해시가 기존 CHECK와 정확히 같아야 하며, 사후 관측이라는 표시를 남깁니다. 원래 CHECK·이전 버전·계약·설정은 보존합니다.

SDK 0.2.3에는 `registered_tasks`, `registered_status`와 실행 예제를 추가했습니다. 기존 Python·Node·MCP·범용 어댑터 인터페이스는 유지합니다. 과거 통과 결과만으로 현재 작업을 완료 처리하지 않습니다.

새 플랫폼 검사와 이전 호스트·화면 검증을 재사용한 범위는 검증 문서에 구분했습니다. 새 유료 AI 세션이나 메모리 시험은 실행하지 않았습니다.
