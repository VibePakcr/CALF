# CALF update / 업데이트 안내

## What is new — Harness 1.8.7 / Workbench 1.9.2 / SDK 0.2.1

- **Universal Work v1:** freeze a work contract, input snapshots and registered adapter identities; produce per-attempt file candidates; bind required checks and adoption to their exact manifest digest.
- **Runtime Work in Workbench:** import a contract, run or reconcile a registered runtime, inspect timestamped stages, artifacts and checks, cancel, recheck and explicitly adopt a verified version. Harness, SDK, MCP and Workbench use the same local records home.
- **Python, Node and local HTTP adapters:** real file-producing execution through one protocol. Dependency-free Python/Node SDK clients and a foreground stdio work MCP endpoint; read-only by default, control tools opt-in. Existing source-reader MCP stays separate.
- **Recovery:** unknown asynchronous submissions reserve the single execution slot and are queried using the original request ID. An explicit new attempt consumes the original budget. Previous candidates and adoption events remain. A timeout or exit 0 is not PASS.
- **Setup and updates:** first-run diagnostics, staged archive verification and retained originating runtimes. JavaScript/TypeScript node:test Check Profiles join Python unittest/pytest and bounded Cargo integration checks. No dependency installation or npm script execution.

The core remains local, lightweight and focused on a single agent. No model, multi-agent orchestration, embedding index or new resident service is added. Workbench loads only the selected runtime work; settled work is not continuously rehashed in the background.

## 이번 업데이트 — Harness 1.8.7 / Workbench 1.9.2 / SDK 0.2.1

- **공통 작업 규약 v1:** 작업 계약·입력 사본·등록 어댑터를 고정하고, 시도별 파일 산출물과 필수 검수·채택을 같은 파일 명세 해시에 결속합니다.
- **Workbench Runtime Work:** 계약 가져오기, 등록 런타임 실행·조회 재개, 타임스탬프 흐름·산출물·검수 확인, 취소·재검수·검증 버전 채택을 제공합니다. Harness·SDK·MCP와 같은 로컬 기록을 읽습니다.
- **Python·Node·로컬 HTTP Adapter:** 서로 다른 런타임의 파일 생성 작업을 공통 규약으로 실행합니다. 의존성 없는 Python·Node SDK와 전경 stdio 작업 MCP를 제공합니다. MCP는 기본 조회 전용이며 제어 도구는 명시적으로 켭니다. 기존 자료 조회 MCP는 별도로 유지됩니다.
- **복구:** 응답이 불명확한 비동기 요청은 실행 슬롯을 유지하며 기존 요청 ID로 조회합니다. 새 시도는 원래 예산을 소비하고 이전 산출물·채택 이력을 보존합니다. 시간 초과나 종료 코드 0을 PASS로 판정하지 않습니다.
- **첫 실행·업데이트·검사:** 환경 진단, 배포 압축 검증 후 별도 준비, 작업 시작 버전 보존을 제공합니다. Python unittest·pytest·제한된 Cargo 검사에 JavaScript/TypeScript node:test Check Profile을 추가합니다. 의존성 설치나 npm 스크립트 실행은 하지 않습니다.

로컬·경량·싱글 에이전트 중심을 유지합니다. 모델·멀티 에이전트·임베딩 색인·새 상주 서비스를 추가하지 않습니다. Runtime Work는 선택한 작업만 불러오며 종결된 산출물을 계속 백그라운드 해싱하지 않습니다.

[Downloads / 다운로드](DOWNLOADS.md) · [Full release notes / 전체 변경 안내](RELEASE-NOTES.md)
