# CALF Harness 1.8.6 · Workbench 1.9.1 · SDK 0.2.0

[English](README.md) · [한국어](README_KR.md) · [Downloads](DOWNLOADS.md)

## English

The shared native runtime now discovers bounded **unittest, pytest and Cargo Check Profiles**, records the pre-change failure baseline, distinguishes test failures from environment/evidence failures, and stops retries with no measured progress. Baseline failures are never waived. Completion still requires the registered checks, current file-version evidence and a separate review invocation.

Python selection prefers `.venv`, `venv`, the active environment and then a bounded PATH probe. Interpreter identity, virtual-environment configuration and installed package metadata are bound to new profile evidence. Missing dependencies are reported, not installed. A broken explicit environment is not silently replaced. Cargo support currently covers one package's integration tests in locked/offline mode; workspaces, unit tests and doctests are outside that automatic profile.

New queued tasks retain a hash-verified originating runtime. A newer launcher can inspect and resume the same task through that retained runtime without rewriting its check definition, consumed budget or past receipts. Keep the entire records home, including `runtimes`. Legacy tasks without a provable runtime remain unresolved. Advanced direct `calf run` state paths still need their original compatible runtime. Existing 1.8.4 hook histories remain separate from the Workbench queue.

SDK 0.2.0 adds `discover_checks()` and `Check.from_discovered()` plus a runnable discovery example. Profiles and their matching command are carried together; the native core remains the authority. This is a standard-library Python client with bounded per-call output and no new daemon, model runtime or index.

### Qualification

- Final native binaries: macOS ARM64, Windows x64 and Linux x64 (Debian 13). Both editions passed task control, shared records, Unicode preferences, stale-evidence/recheck and failure-exit/cancel checks in isolated folders.
- SDK: nine boundary tests on each OS plus real failing Python tests, repair, native profile round-trip, evidence invalidation, queue operations and Local MCP. SDK provider fixtures are deterministic, not AI-service tests.
- Actual Codex: a fresh macOS Harness 1.8.6 job repaired a six-test invoice example, passed owned checks and a separate AI review, matched Workbench 1.9.1's task record, and passed a separate six-test rerun. Existing tests, example history, contract and settings remained byte-identical.
- The preceding implementation qualification exercised Python environment selection, pytest/Cargo failures, no-progress termination and different-runtime update/resume on all three OSes; it also completed a 14-test actual Codex invoice job on each OS. These are retained implementation evidence, not fresh service runs on every final package. Antigravity's existing integration is retained; no new Antigravity service run is claimed for this patch release.
- macOS Workbench's final native screen and the bilingual manual were inspected. Windows/Linux desktop binaries were rebuilt; their prior native UI qualification is retained. Fresh final-package runtime/SDK checks ran on both hosts. No new memory or long-duration soak test was performed.

### Distribution and upgrade

Six binary archives and one portable SDK archive are provided. Each runtime archive includes the illustrated offline EN/KR manual, release notes, dependency notices, a file manifest and SHA-256 sums. Some manual screenshots are explicitly labelled historical 1.9.0 UI references; they do not stand in for new binary test evidence. The proprietary core source, personal records, contracts, settings and credentials are not shipped. SDK integration source has its separate extension license.

Extract into a new folder, keep the old installation and the complete records home, then connect the new program to the same home. Do not replace live journals or global host settings. macOS ARM64 14+ packages have ad-hoc integrity signatures, **not Apple notarization**. Windows packages have **no publisher signature** and Workbench requires WebView2. Linux Workbench needs GTK 3 / WebKitGTK 4.1 and a graphical session. No Intel Mac, ARM64 Windows/Linux or musl package is included. Direct OpenAI API service qualification and absolute correctness of arbitrary tasks are not claimed.

## 한국어

공통 네이티브 런타임에 **unittest·pytest·Cargo Check Profile**, 변경 전 실패 기준선, 실패 원인 분류, 진전 없는 반복 종료가 적용됩니다. 기존 실패를 면제하지 않으며, 등록 검사·현재 파일 버전 근거·별도 검수 호출이 충족되어야 완료로 판정합니다.

Python은 `.venv` → `venv` → 활성 환경 → 제한된 PATH 탐색 순서로 선택합니다. 인터프리터·가상환경 설정·설치 패키지 메타데이터를 새 검사 근거에 결속합니다. 의존성을 자동 설치하거나 손상된 명시 환경을 조용히 바꾸지 않습니다. Cargo 자동 검사는 단일 패키지의 통합 테스트를 locked·offline으로 실행하는 범위이며 workspace 전체·unit test·doctest는 포함하지 않습니다.

새 대기열 작업은 생성 당시 런타임을 해시로 보존합니다. 업데이트 후 새 실행기가 해당 런타임으로 기존 작업을 조회·재개하며 검사 정의·소진 예산·과거 영수증을 다시 쓰지 않습니다. `runtimes`를 포함한 전체 기록 폴더를 유지하세요. 런타임을 입증할 수 없는 이전 작업은 미해결로 남고, 고급 `calf run` 직접 상태 경로는 원래 호환 런타임이 필요합니다. 기존 1.8.4 훅 기록은 Workbench 대기열과 별도로 보존됩니다.

SDK 0.2.0에는 `discover_checks()`·`Check.from_discovered()`와 조회 예제가 추가됩니다. 검사 명세와 연결 명령을 함께 보존하며 판정 권한은 코어에 있습니다. Python 표준 라이브러리만 사용하고 상주 서비스·모델 런타임·색인을 추가하지 않습니다.

### 실제 확인 범위

- 최종 macOS ARM64·Windows x64·Linux x64(Debian 13) 코어에서 작업 제어·공유 기록·유니코드 선호·근거 무효화와 재검수·실패 종료·취소를 확인했습니다.
- SDK는 OS별 경계 검사 9개와 실제 Python 실패→복구→검사, 프로파일 왕복, 근거 무효화, 대기열, Local MCP를 검증했습니다. SDK 공급자는 결정적인 시험 도구이며 AI 서비스는 아닙니다.
- 새 macOS Harness 1.8.6에서 실제 Codex가 invoice 예제를 수정하고 검사 6개와 별도 AI 검수를 통과했습니다. Workbench 1.9.1에서 같은 작업을 조회하고 독립적으로 다시 실행한 검사 6개도 통과했습니다. 예제의 기존 테스트·기록·계약·설정은 원본 그대로 유지됐습니다.
- 직전 구현 검증에서 세 OS의 Python 환경 선택·pytest/Cargo·무효 재시도·다른 실행 버전으로 업데이트 후 재개를 확인했고, 각 OS의 실제 Codex 업무 검사 14개도 통과했습니다. 이는 보존된 구현 근거이며 모든 최종 패키지에서 새로 수행한 서비스 시험을 뜻하지 않습니다. 기존 Antigravity 연결은 유지하지만 이번 패치에서 새 Antigravity 서비스 시험은 수행하지 않았습니다.
- 최종 macOS 화면과 영·한 매뉴얼을 확인했습니다. Windows/Linux UI는 재빌드했으며 기존 네이티브 UI 확인 근거를 유지합니다. 최종 코어·SDK는 두 호스트에서 새로 시험했습니다. 메모리·장시간 시험은 추가하지 않았습니다.

### 배포와 보존

바이너리 압축 6개와 공용 SDK 압축 1개입니다. 실행 패키지마다 스크린샷이 포함된 영·한 오프라인 매뉴얼, 릴리즈 노트, 의존성 고지, 파일 명세와 SHA-256이 들어 있습니다. 매뉴얼의 이전 1.9.0 참고 화면은 캡션으로 구분하며 새 실행 검증 근거로 대신하지 않습니다. 코어 소스·개인 기록·계약·설정·인증정보는 배포하지 않습니다. SDK 확장 소스에는 별도 라이선스가 적용됩니다.

새 폴더에 압축을 풀고 기존 설치와 전체 기록 폴더를 유지한 채 같은 기록 위치로 연결하세요. 실행 중인 저널이나 전역 호스트 설정을 덮어쓰지 않습니다. macOS는 ad-hoc 무결성 서명이며 Apple 공증이 아닙니다. Windows 게시자 서명은 없으며 Workbench에는 WebView2가 필요합니다. Linux Workbench는 GTK 3·WebKitGTK 4.1·그래픽 세션이 필요합니다. Intel Mac·ARM64 Windows/Linux·musl 패키지는 포함하지 않습니다. 직접 OpenAI API 실서비스 검증이나 임의 작업의 절대적 정확성을 주장하지 않습니다.
