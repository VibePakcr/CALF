# CALF — Universal Work and Runtime Workbench

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

## Verification and limits / 검증과 한계

Completed release qualification used the exact packaged native cores and SDK on macOS ARM64, Windows x64 and Linux x64 (Debian 13). It covers real Python and Node processes, independent validation, a local HTTP service, MCP, cancellation, stale evidence, preserved files and retained-runtime resumption. See VERIFICATION.json for the completed results. Deterministic adapters are used; this release does not claim a new live Codex/Antigravity service benchmark or memory/long-duration benchmark.

The work protocol currently supervises **file artifacts**. It is not an OS sandbox, a monetary cost ledger, remote database transaction system or a guarantee of aesthetic quality. Only registered executables and declared adapter files are pinned; transitive dependencies need their own packaging. Cancellation of external jobs depends on the adapter/provider. Unconfirmed cleanup stays UNKNOWN and may require host-level investigation. List calls are bounded (128 adapters / 256 works); no automatic full-history index is added. Adoption selects the current verified candidate; selecting an older adoption is not exposed yet.

Existing records, contracts and settings need no migration. Keep the full records home, including retained runtimes and work-v1. Do not merge or overwrite active journal files. Extract an update into a separate folder. The same CALF_WORK_HOME connects Harness and Workbench; legacy 1.8.4 hook history remains separate from the task queue.

macOS packages have ad-hoc integrity signatures, **not Apple notarization**. Windows packages have no publisher signature and Workbench needs WebView2. Linux Workbench requires GTK 3, WebKitGTK 4.1 and a graphical session. Included targets: macOS ARM64, Windows x64, Linux glibc x64; no Intel Mac, Windows/Linux ARM64 or musl package.

최종 바이너리·SDK를 macOS ARM64·Windows x64·Linux x64(Debian 13)에서 시험했습니다. 실제 Python·Node 프로세스, 독립 검수, 로컬 HTTP, MCP, 취소, 오래된 근거 무효화, 파일 보존, 원래 런타임을 통한 재개가 대상이며 완료 결과는 VERIFICATION.json에 기록합니다. 결정적인 시험 어댑터를 사용하며 새로운 Codex·Antigravity 실서비스 또는 메모리·장시간 시험을 주장하지 않습니다.

현재 규약은 파일 산출물을 감독합니다. OS 샌드박스·금액 정산·원격 DB 트랜잭션·미적 품질 보장은 제공하지 않습니다. 종료를 확인할 수 없으면 UNKNOWN을 유지합니다. 기존 기록·계약·설정과 전체 runtimes·work-v1 폴더를 보존하고, 업데이트는 별도 폴더에 풉니다. macOS 공증·Windows 게시자 서명은 없으며 각 OS의 WebView·GUI 라이브러리는 별도 요건입니다.

Native regression: 40 PASS. SDK boundaries: 16 per OS. Universal work: 23 scenarios per core per OS, plus retained-runtime/crash recovery and existing code-job SDK integration. macOS window interaction is freshly verified. Windows/Linux final UI bridge and system monitor are verified; fresh native-window interaction is not claimed.

네이티브 회귀 40개, OS별 SDK 경계 검사 16개, 각 OS·코어별 범용 작업 23개와 재개·강제 종료·기존 코드 작업 통합을 통과했습니다. macOS 실제 창 조작과 Windows/Linux 최종 네이티브 UI 연결·시스템 모니터를 확인했습니다. Windows/Linux의 새로운 창 조작 시험을 주장하지 않습니다.
