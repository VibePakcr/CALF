# CALF Harness 1.8.25 · Workbench 1.9.24
## Workbench 1.9.24 — follow work and review interruptions

Switch between **Flow** and **History** for the same recent verified steps. The task request, recorded state and available state explanation stay together. Select a step to inspect its record and operation details; use **Task evidence** for current validation.

**Review requests** opens Attention. **Needs review**, **Observation gaps** and **All observed** filter the same bounded native observation. Cards separate the historical outcome from current completion, show freshness, and expose the recorded evidence reference. Open a task to inspect it before taking an existing review action.

This is a view over existing records. It adds no execution engine, task database, automatic approval, remote approval or host-task control. Earlier records and pinned runtimes remain intact. Harness 1.8.25 and SDK 0.2.11 are unchanged.

Upgrade from Workbench 1.9.23 through Updates, or extract 1.9.24 into a new folder and keep your existing records home. [Screen guide](WORK_STATE_VIEW.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#work-state).

## Workbench 1.9.24 — 작업 흐름과 중단 이유 확인

**Flow**와 **History**에서 같은 최근 검증 기록을 흐름도와 시간순 목록으로 전환합니다. 작업 요청·기록된 상태·확인 가능한 상태 설명을 함께 보여줍니다. 단계를 선택하면 기록·작업 정보를 읽고, **Task evidence**에서 현재 검증 상태를 확인할 수 있습니다.

**Review requests**로 Attention을 열고 **Needs review**, **Observation gaps**, **All observed**로 같은 제한된 네이티브 조회 결과를 나눠 봅니다. 카드에는 과거 결과와 현재 완료 여부를 구분하고, 관측 시각과 근거 참조를 표시합니다. 작업을 열어 근거를 읽은 뒤 기존 검토 기능을 사용하세요.

기존 기록을 읽는 화면 개선입니다. 별도 실행 엔진·작업 DB·자동 승인·원격 승인·호스트 작업 제어를 추가하지 않습니다. 이전 기록과 작업별 고정 런타임을 보존하며 Harness 1.8.25와 SDK 0.2.11은 유지합니다.

Workbench 1.9.23의 Updates를 사용하거나 1.9.24를 새 폴더에 풀고 기존 기록 위치를 유지하세요. [화면 안내](WORK_STATE_VIEW_KR.md) · [온라인 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#work-state).


## 1.8.25 / 1.9.23 — incident evaluation, adversarial review and event resume

Historical incident packets exclude answers and future evidence; scores separate diagnosis from handoff usefulness. Adversarial review binds support, counterexamples and alternatives to actual current native CHECKs. Opt-in local events resume one bound managed task, reject duplicate/stale events and retain uncertain interrupted execution for review. Existing records, contracts, settings and pinned task runtimes remain intact.

Host audit logs now rotate before a new record would exceed 64 MiB. The previous bytes remain in cold segments with their size and SHA-256 receipts. Writers share an OS lock, and an audit write failure leaves the event unacknowledged for retry.

Use `calf evaluation` and `calf events` through the CLI or common API. [Usage and fields](WORKFLOW_HARDENING.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#workflow-hardening). SDK 0.2.11 is unchanged.

Upgrade from Workbench 1.9.22 through Updates or extract 1.9.23 into a new folder. Keep the original records home and pinned task runtimes. Linked host tasks continue in their original host.

## 1.8.25 / 1.9.23 — 과거 장애 평가·반증 검증·이벤트 재개

과거 장애의 정답·미래 자료를 분리하고 진단과 보고서를 별도 평가합니다. 가설·반례·대안을 실제 네이티브 CHECK에 결속하며, 명시적으로 등록한 이벤트로 지정 관리 작업만 재개합니다. 중복·만료 이벤트와 중단 후 불확실한 재실행을 차단합니다. 기존 기록·계약·설정과 작업별 고정 실행기를 보존합니다.

호스트 감사 로그가 새 기록으로 64MiB를 넘기 전에 자동 회전합니다. 이전 기록은 크기·SHA-256 영수증과 함께 콜드로그로 보관합니다. 작성자는 OS 잠금을 공유하며, 감사 저장에 실패한 이벤트는 처리 완료로 표시하지 않습니다.

CLI와 공통 API의 `calf evaluation`·`calf events`로 사용합니다. [사용법과 필드](WORKFLOW_HARDENING_KR.md) · [온라인 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#workflow-hardening). SDK 0.2.11은 유지합니다.

Workbench 1.9.22의 Updates를 사용하거나 1.9.23을 새 폴더에 푸세요. 기존 기록 폴더와 작업별 고정 실행기는 유지하며, 연결 작업은 원래 호스트에서 계속됩니다.

## Previous releases

# CALF Workbench 1.9.22

Fix connected-task status lookup while preserving existing records, contracts, settings and pinned runtimes. Harness 1.8.24 and SDK 0.2.11 remain unchanged.

- Retain the selected task ID when it is omitted from the task list. An unavailable task shows its own error instead of another task’s verdict.
- Read explicitly connected host tasks without requiring an unrelated workspace selection.
- Rechecked utility-panel switching, background control visibility, unsaved preference drafts, Esc and task search.

연결 작업의 상태 조회를 수정한 정식 패치 릴리즈입니다. 목록에서 빠진 작업도 선택한 ID를 유지하며, 해당 작업을 읽지 못할 때 다른 작업의 결과로 대체하지 않습니다. 폴더 선택 전에도 연결 작업을 조회할 수 있습니다.

The task-selection repair passed 79 targeted UI tests, including three reproduced regressions. Actual macOS UI checks read both existing host tasks without controlling them. Per-platform package checks and signing results are recorded in STATUS-LOOKUP-VERIFICATION.json. Windows binaries are unsigned; Linux requires GTK 3 and WebKitGTK 4.1.

Use Updates or extract the new package to a separate folder. Previous releases remain available. Read-only host observations do not establish task liveness or whole-task completion.

## Previous releases

## Under Patch 2026-11-19 — Harness 1.8.24 · Workbench 1.9.21

- Evaluate supplied model choices, required skills and forbidden skills with `calf evaluation`.
- Read lane process outcomes, durations, provider-reported usage and supplied-rate estimates from exact native checkpoints. Keep missing counters and unpriced cost unknown.
- Correct local planner nullable-hash validation while retaining the shared MCP schema rules. Preserve existing records, contracts, settings and pinned task runtimes.

동일 버전의 배포 파일을 교체하는 언더패치입니다. 모델·스킬 선택과 Lane 계측을 Rust에서 읽기 전용으로 평가하며, 기존 기록·계약·설정과 진행 작업의 고정 런타임을 보존합니다.

[English guide and real-model pilot](ROUTING_EVALUATION.md) · [한국어 안내](ROUTING_EVALUATION_KR.md) · [Qualification](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING-LANE-VERIFICATION.json)

# CALF Harness 1.8.24 · Workbench 1.9.21

Same underpatch includes the long-session status query repair; latest linked responses remain readable with old records and settings preserved.

## Under Patch — credential-isolated operation delegation

Opt-in Rust broker on macOS with a separately provisioned Linux SSH client, fixed read-only operation, exact ticket and local confirmation before credentials, one-use authority, acknowledged results and fail-closed uncertainty. No local untrusted process route, agent/port/filesystem forwarding or credential-writing CLI. Existing versions, records, contracts, settings and tasks retained.

## Under Patch — ontology model and append integrity

Under Patch 2026-11-16 · version numbers retained. The [model specification](ONTOLOGY_MODEL.md) and [JSON](ONTOLOGY_MODEL.json) define objects, common/variant properties, relationship domain/range and enforcement points. Native validation and public descriptions share field definitions. Every append path rejects reviving a retracted record. Stored format, contracts, settings and task runtimes are preserved.

Under Patch 2026-11-16 · 버전 번호 유지. 객체·공통/타입별 속성·관계의 도메인과 범위·제약 적용 시점을 [명세](ONTOLOGY_MODEL_KR.md)와 [JSON](ONTOLOGY_MODEL.json)으로 제공합니다. Rust 검증기와 필드 정의를 공유하며 모든 기록 추가 경로에서 철회 기록 재승격을 차단합니다. 기존 기록 형식·계약·설정·작업 런타임은 유지합니다.


## Harness 1.8.24 · Workbench 1.9.21 — evidence graphs and native ontology exploration

- Read-only evidence graph with themed relationship directions, zoom and fit.
- Search and page through older selected-task evidence; navigate neighborhoods, incoming references and bounded paths.
- Inspect direct/indirect impact candidates and their recorded dependency explanations.
- Reuse canonical reads within one request and index dependency traversal while retaining full source validation and snapshot-change rejection.
- Preserve original records, contracts, settings, task runtimes and previous releases. SDK 0.2.11 remains unchanged.

작업 하나의 근거 그래프, 오래된 기록 검색과 페이지 이동, 주변·역참조·기록 경로, 직접·간접 영향 근거를 읽기 전용으로 제공합니다. 기록 연결 검증을 유지하면서 반복 해석을 줄였습니다. 현재 작업 완료나 인과관계를 자동 판정하지 않습니다.

[English guide](ONTOLOGY_GUIDE.md) · [한국어 사용법](ONTOLOGY_GUIDE_KR.md)

## Harness 1.8.23 · Workbench 1.9.20 — connected host tasks and writer-safe status

- Connected tasks cards read explicitly linked Codex CALF records and follow the newest response in that same session.
- Background polling no longer opens retained runtimes' writer journals. A busy original writer leaves a readable committed observation and an unknown current verdict.
- Response endings, historical completion and current validation remain distinct. Original records, contracts, settings, required checks and pinned runtimes are retained.
- SDK 0.2.11 is unchanged. No private task bindings or user records are distributed.

연결된 Codex CALF 작업을 카드와 상세 상태에서 읽고 같은 채팅의 최신 응답 기록을 따라갑니다. 기록 쓰기와 조회가 겹쳐도 확정 기록을 읽으며 현재 검증을 임의로 성공 처리하지 않습니다. 작업 중단·재시작 없이 기존 기록·계약·설정·원래 런타임과 이전 배포본을 유지합니다.

[English guide](HOST_TASKS_PATCH.md) · [한국어 안내](HOST_TASKS_PATCH_KR.md)


## Harness 1.8.22 · Workbench 1.9.19 — clearer views and retained task status

- Utility views use the central work area. Underlying task controls no longer overlap; Close stays available while contents scroll.
- Navigation, keyboard focus, draft retention, update buttons, light-theme contrast and empty-folder states are polished.
- Task status finds Workbench records for the selected folder and uses each task’s retained runtime. Recorded results and current observations stay distinct. Missing or corrupt data remains explicit.
- Existing records, contracts, settings, pinned task runtimes and earlier releases are preserved. SDK 0.2.11 is unchanged.

보조 화면과 뒤쪽 버튼이 겹치지 않도록 배치를 정리하고, 닫기·키보드·초안 유지·업데이트·밝은 테마·빈 폴더 안내를 다듬었습니다. 작업 상태는 선택한 폴더의 보관 기록과 원래 런타임을 조회하며 과거 결과와 현재 관측을 구분합니다. 기존 기록·계약·설정·이전 런타임·배포본은 보존합니다.

[English details](UI_STATUS_PATCH.md) · [한국어 안내](UI_STATUS_PATCH_KR.md)


## Harness 1.8.21 · Workbench 1.9.18 — corrections for the next request

- Save an explicit correction from a task. Matching notes from two different tasks in the same folder become a suggestion for a new request.
- Append a suggestion to the editable form and undo it without replacing your original text. Existing contracts, permissions and required checks stay intact.
- The request helper has a fixed title and Close button with a separate scrolling body. English/Korean guides and the offline manual include actual new-release captures.

같은 폴더에서 반복해서 남긴 수정 사항을 다음 요청에서 골라 넣고 되돌릴 수 있습니다. 기존 기록·계약·설정과 검사 기준을 유지하며, 대화 자동 분석이나 전역 규칙 자동 적용은 하지 않습니다.

[English guide](REQUEST_GUIDANCE.md) · [한국어 사용법](REQUEST_GUIDANCE_KR.md)


## Harness 1.8.20 · Workbench 1.9.17 — automatic engineering material

Built-in references require no setup. Workbench adds one-folder import for UTF-8 Markdown/text and existing CALF knowledge exports. Rust validates files and Unicode chunks, retains original files and existing selections, and keeps import separate from read-only search/MCP. New tasks use the connected material automatically. SDK 0.2.11 is unchanged.

기본 지식은 설정 없이 사용합니다. 개인 자료는 폴더 선택 한 번으로 검사·색인·연결하며 기존 자료·기록·계약·설정을 보존합니다.


- Keep unresolved effects visible after cancel/pause requests; do not confuse a request with an actual stopped operation.
- Show missing runtime/evidence as unknown; bound attention observation and expose coverage instead of a false all-clear.
- Native authority, contracts, existing records and recovery remain unchanged. SDK 0.2.11 is unchanged.
- Optional CALF Connect 0.1.0-dev.1 is released separately with bilingual installation and actual-screen manuals. Four IDEs across three operating systems were observed in isolated profiles.
- Final package identity and lifecycle checks are separate from the reused implementation regression and 12 IDE GUI flows. No new live AI task or token saving is claimed.

## 한국어

- 취소·일시 정지 요청만으로 중단됐다고 표시하지 않고 미해결 효과를 계속 보여줍니다.
- 확인할 수 없는 런타임·근거는 상태 불명으로 남기고 주의 목록의 조회 범위·한도를 명시합니다.
- 기존 네이티브 권한·계약·기록·복구를 유지합니다. SDK 0.2.11은 변경하지 않습니다.
- CALF Connect 0.1.0-dev.1은 별도 배포하며 세 OS·네 IDE의 실제 화면과 영·한 설치·매뉴얼을 제공합니다.
- 최종 패키지 검사와 재사용 구현 회귀·12개 GUI 검증을 구분합니다. 새로운 실제 AI 작업이나 절감률을 주장하지 않습니다.

---

# CALF update — Harness 1.8.18 · Workbench 1.9.15 · SDK 0.2.11

- The shared Rust core retrieves Development Pack, Pattern and Method references on the CPU. The built-in starter contains 367 references, including entries explicitly marked as names rather than complete definitions.
- An explicit local import builds a bounded SQLite full-text index, preserving source hashes and candidate/historical status. The private qualification corpus is not included in downloads.
- New tasks freeze their selected references through plan, repair, review and resume. Knowledge remains reference data; registered, file-bound checks still decide completion.
- Workbench adds an on-demand Engineering knowledge panel. Repository Local MCP and Rust/Python/Node SDK examples use the same native reader.
- An optional loopback-only Ollama/MLX chat connection checks model metadata without inference. No model, daemon, cloud dependency or extra agent is required. Actual local-model task completion is not qualified: unchanged memory guards stopped the Qwen7B trials on the M5 16GB.
- Resource interruptions are distinguished from ordinary provider failure. Short native transport error codes are recorded without prompts or raw model responses.
- Windows and Debian passed actual synthetic import/resume/repair/check flows and SDK reads. A Mac Codex task passed registered checks, a separate review and three independently rerun tests. A lookup result or a source's past PASS is never a new completion receipt.
- Previous versions, retained task runtimes, records, contracts and settings remain in place. The proprietary core is distributed as free-to-use binaries; public SDK/adapter/MCP extension points remain separate.

## 한국어

- Development Pack·Pattern·Method 참조를 공유 Rust 코어에서 CPU로 조회합니다. 기본 참조 367개 중 이름만 있는 항목은 완전한 정의와 구분합니다.
- 사용자가 선택한 자료는 로컬 SQLite 전문 검색 인덱스로 가져옵니다. 출처 해시와 후보·과거 자료 상태를 보존하며 비공개 검증 자료는 배포하지 않습니다.
- 새 작업의 참조는 계획·수정·검토·재개 동안 그대로 유지합니다. 지식은 참고 자료이고 실제 파일에 결속된 등록 검사가 완료 여부를 판단합니다.
- Workbench의 Engineering knowledge 패널은 열었을 때만 조회합니다. Repository Local MCP와 Rust·Python·Node SDK 예제도 같은 네이티브 조회기를 사용합니다.
- 기존 Ollama·MLX 서버를 위한 루프백 연결을 미리보기로 제공합니다. 연결 확인은 모델 목록만 읽습니다. M5 16GB에서 Qwen7B 시험은 기존 메모리 가드가 중단했으므로 작업 완료까지 지원 검증이 끝났다고 안내하지 않습니다.
- 자원 부족에 따른 중단과 일반 연결 실패를 구분하고, 민감한 본문 없이 오류 코드를 기록합니다.
- Windows·Debian의 실제 합성 실행·재개·수정·검사와 SDK 조회를 통과했습니다. Mac의 실제 Codex 작업은 등록 검사·별도 검토와 독립 테스트 3개를 통과했습니다.
- 이전 버전·작업 런타임·기록·계약·설정과 완료 기준을 유지합니다. 코어 소스는 비공개이며 무료 사용 가능한 실행 파일과 별도 SDK·Adapter·MCP 확장점을 제공합니다.

---


## Workbench 1.9.14: monitor and sidebar update

Mint usage bars and values now sit on thin unused tracks. CPU shows its detected total and three busiest cores. The left panel scrolls independently to its bottom menus and version. Qualified on macOS, Windows and Debian; earlier packages and records are retained. Harness 1.8.17 and SDK 0.2.10 are unchanged. [English details](MONITOR_UI_FIX.md) · [한국어](MONITOR_UI_FIX_KR.md).


## Workbench 1.9.14: 모니터·좌측 패널 수정

민트색 사용량·숫자는 유지하고 남은 구간을 가는 트랙으로 정리했습니다. CPU의 전체 코어 수와 사용량 상위 3개를 구분하며, 좌측 패널은 맨 아래 메뉴와 버전 표시까지 따로 스크롤할 수 있습니다. 맥·윈도우·Debian에서 화면을 확인했습니다. 하네스 1.8.17·SDK 0.2.10과 기존 기록·계약·설정, 이전 배포본은 유지합니다. [자세히](MONITOR_UI_FIX_KR.md) · [English](MONITOR_UI_FIX.md).

---

## Packaging correction · 12 November 2026

In-app update archives now carry the required manifest and internal checksums, without extra Mac metadata. Executables, signatures and completion rules are unchanged. [English details](PACKAGE_UPDATE_FIX.md) · [한국어 안내](PACKAGE_UPDATE_FIX_KR.md).

---

# CALF update — Harness 1.8.17 · Workbench 1.9.13 · SDK 0.2.10

- Task Flow names the Work, Checks and Repair / retry lanes; labels remain visible while scrolling.
- A five-step first-task guide keeps check discovery separate from test execution.
- Up to eight personal request outlines are stored locally and applied to an empty helper form. New work requires fresh checks.
- Evidence-aware next steps distinguish an unavailable observation from a missing or changed runtime.
- Task summaries require preview and explicit local export. No automatic upload, permission transfer or current completion certificate is added.
- Build metadata and English/Korean release documents share version facts. Published release, installed version and current verdict remain distinct.
- macOS Workbench uses Developer ID signing and Apple notarization. Windows publisher signing is not claimed. Linux qualification covers Debian 13 x86_64.

The proprietary core stays private. CALF remains free to use, independent of VibePackr, local-first and centred on one agent. Connected AI services retain their own accounts, fees and approval rules. Existing versions, records, contracts and settings are preserved.

[English guide](CURRENT_RELEASE.md) · [한국어 안내](CURRENT_RELEASE_KR.md)

---

# CALF 업데이트 — 하네스 1.8.17 · 워크벤치 1.9.13 · SDK 0.2.10

- Task Flow에 Work·Checks·Repair / retry 레인 이름을 표시합니다. 가로로 스크롤해도 레인 이름은 보입니다.
- 다섯 단계 첫 작업 안내에서 검사 항목을 찾는 것과 실제 검사를 구분합니다.
- 로컬 요청 양식은 최대 8개까지 저장하고 비어 있는 도움말 입력란에 적용합니다. 새 작업은 새로 검수합니다.
- 근거에 따른 다음 행동을 안내하며, 일시적인 조회 실패를 런타임 손상으로 단정하지 않습니다.
- 작업 요약은 미리보기와 명시적 확인 후 로컬에 저장합니다. 자동 업로드·실행 권한 이전·현재 완료 인증은 제공하지 않습니다.
- 빌드와 영·한 문서의 버전 정보를 맞춥니다. 공개 배포·현재 설치·현재 검수 결과는 각각 구분합니다.
- Mac 워크벤치에 Developer ID 서명과 Apple 공증을 적용합니다. Windows 게시자 서명은 제공하지 않으며 Linux 검증 기준은 Debian 13 x86_64입니다.

비공개 코어는 공개하지 않습니다. CALF는 VibePackr 없이도 무료로 사용할 수 있으며 로컬·경량·싱글 에이전트 중심을 유지합니다. 연결한 AI 서비스의 계정·요금·승인 규칙은 그대로 적용됩니다. 이전 버전과 기존 기록·계약·설정은 보존합니다.
