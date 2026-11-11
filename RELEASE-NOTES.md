# Repository Intelligence in the Rust core · 2026-11-11

Harness 1.8.15 · Workbench 1.9.11 · SDK 0.2.8 · optional native FFmpeg 0.2.0-preview.1.

- Repository context, module history, exact-record queries and the existing CPU lane/gate now run in one native core.
- Local Git captures retain raw HEAD/index/working versions, source hashes and lexical relationship candidates. No Git status, worktree conversions, hooks or fetch are used by this reader.
- Workbench adds a lazy Repository context panel and saved-source selection. Reading records is separate from sending context to an AI or establishing completion.
- Native pack management and Claude lifecycle/setup/update/recovery no longer require Python. SDKs remain thin language bindings. Existing owner-managed T9 protection bridges and project-language test runtimes remain intact.
- FFmpeg is the only current optional extension. Navigator, hosted browsing, video management and motion experiments are excluded from current packages; their historical source and releases are retained.
- Existing original journals, hash chains, contracts, settings, old task runtimes and approved media are preserved. Completion standards are unchanged.

하네스 1.8.15 · 워크벤치 1.9.11 · SDK 0.2.8 · 선택 확장 FFmpeg 0.2.0-preview.1입니다. Repository 문맥·모듈 기록·원문 조회·CPU 레인과 검사를 공통 Rust 코어로 통합했습니다. 로컬 Git의 원본 버전과 관계 후보를 저장하고 워크벤치에서 필요한 기록·파일만 조회할 수 있습니다. 팩 관리와 Claude 연결도 Rust로 처리하며, 현재 별도 확장은 FFmpeg만 남깁니다. 기존 기록·계약·설정·과거 실행 파일·승인 영상은 보존하고 완료 기준은 유지합니다.

See VERIFICATION.json for exact binary identities and tested platforms. Native synthetic tests are not new paid AI/app-session benchmarks. Rust lexical candidates do not replace a full Python parser or application tests. The optional media profile remains bounded; it does not verify aesthetic quality. macOS packages use ad-hoc integrity signing, not Apple notarization; Windows publisher signing is not claimed.

---

# Maintenance distribution · 2026-11-11

Harness 1.8.14 · Workbench 1.9.10 · SDK 0.2.7. Existing records, contracts, settings and older task runtimes are retained. No new setup step is required.

하네스 1.8.14 · Workbench 1.9.10 · SDK 0.2.7 유지보수 배포본입니다. 기존 기록·계약·설정과 과거 작업의 실행 파일을 유지합니다.

---

# CALF Harness 1.8.13 · Workbench 1.9.9 · SDK 0.2.6

## Decisions and results, with less clutter

- Read-only Attention gathers stopped work and candidates awaiting adoption. The Harness and Workbench share the native query; opening it does not execute or approve work.
- Result summaries connect changed files, check receipts, saved reviews and the current verdict. A historical pass stays distinct from current verification.
- Shape request helps describe the outcome, preserved inputs and checks while retaining the user's draft. It does not submit the task or weaken its contract.
- Day/Night changes only the central workspace. Appearance preferences are stored separately from contracts and other settings.
- Find task supports CJK text, Cmd/Ctrl+K, arrow keys, Enter and Esc using only the loaded recent queue. It does not scan all history or call a model.
- Narrow windows fold the system/worker monitors. Hidden monitors stop sampling; Task Flow and execution continue.
- Fixed Windows update preparation to validate original ZIP member names before platform separator normalization. Traversal, links and backslash member names remain blocked.
- SDK documents, examples and the three-host compatibility list match this release. No new product library, daemon, model or agent pool is added.

Fresh release binaries and archives are checked separately from the earlier live Codex task and GUI observations. [VERIFICATION.json](VERIFICATION.json) distinguishes that evidence, owner-assisted Windows actions and the remaining Linux remote-input limitation. This is not a new AI-service or memory benchmark.

## 한국어

- Attention에서 중단된 작업과 채택 대기 후보를 모아 볼 수 있습니다. 하네스와 Workbench가 같은 읽기 전용 조회를 사용하며, 조회만으로 실행하거나 승인하지 않습니다.
- 결과 요약에서 변경 파일·검사 영수증·저장된 검토·현재 판정을 함께 확인합니다. 과거 통과와 현재 검증은 구분합니다.
- 요청 도움 기능으로 원하는 결과·보존 대상·확인 방법을 정리합니다. 기존 초안을 유지하며 작업을 제출하거나 계약 기준을 낮추지 않습니다.
- 중앙 작업 영역만 Day/Night로 전환합니다. 테마는 계약과 다른 설정에서 분리해 저장합니다.
- CJK 작업 검색과 Cmd/Ctrl+K·방향키·Enter·Esc를 지원합니다. 이미 읽은 최근 목록만 검색하고 전체 기록 조회나 AI 호출을 추가하지 않습니다.
- 좁은 창에서는 시스템·워커 모니터를 접습니다. 접힌 동안 자원 조회를 멈추고, Task Flow와 작업 실행은 계속 유지합니다.
- Windows 업데이트에서 ZIP의 원래 경로 이름을 검사하도록 고쳤습니다. 정상 경로의 구분자 변환으로 생기던 거부를 해결하며, 경로 이탈·링크·백슬래시 이름은 계속 차단합니다.
- SDK 문서·예제와 세 호스트의 호환 목록을 맞췄습니다. 새 라이브러리·상주 서비스·모델·에이전트 풀을 추가하지 않았습니다.

새 배포 실행 파일·압축 파일의 검증과 이전 실제 Codex 작업·화면 검증은 [VERIFICATION.json](VERIFICATION.json)에 구분합니다. Windows의 사용자 직접 조작과 Linux 원격 입력의 미확인 범위도 명시합니다. 새 AI 실서비스 시험이나 메모리 시험은 하지 않았습니다.

기존 기록 위치·계약·설정·과거 버전을 보관해 업데이트하세요. 조회 기능은 실행 권한을 부여하지 않으며 기존 완료 기준을 그대로 적용합니다.

[Downloads / 다운로드](DOWNLOADS.md) · [English guide](WORKBENCH_CLARITY.md) · [한국어 안내](WORKBENCH_CLARITY_KR.md)
