# Workbench 1.9.7 · 2026-11-10

First-task guidance shows the selected folder, saved connection and next step. An optional three-line request outline only fills an empty draft. The guide folds after a new job appears and can be reopened; setup diagnosis opens on demand. No execution authorization, checks, record format, host policy or model settings change.

첫 작업 안내에 폴더·저장된 연결·다음 단계를 표시합니다. 빈 입력창에만 세 줄 초안을 넣을 수 있고, 새 작업이 나타나면 접히며 다시 열 수 있습니다. 진단은 필요할 때 엽니다. 실행 권한·검사·기록 형식·호스트 정책·모델 설정은 변경하지 않습니다.

[Actual screenshots / 실제 화면](FIRST_TASK_KR.md) · [Installation / 설치](install.md) · [Verification scope / 검증 범위](VERIFICATION.json)

Workbench 1.9.7 and Host Connections 1.8.11-hosts.2 are new artifacts. Harness 1.8.11 and SDK 0.2.4 releases remain unchanged. The latest kit recognizes the new Workbench identity without changing approval settings. Existing records, contracts, settings and older runtimes must be retained.

---

# CALF Harness 1.8.11 · Workbench 1.9.6 · SDK 0.2.4

## Claude connection update

- Added the official `PostToolBatch` observation to the Claude hook adapter. A denied non-check call is resolved only when session, turn, tool ID and input match. The complete batch is validated first, and only a result fingerprint is retained.
- Registered checks still require real native execution receipts and matching file versions. Missing results, conflicting identities and claimed checks stay `UNKNOWN`. Batch text cannot create a passing CHECK or infer exit zero.
- Included the nine-hook adapter and install/update/recovery kit in Harness, Workbench and SDK archives. The installer prepares revisions side by side, checks current settings hashes and preserves unrelated hooks, permissions and MCP settings. No persistent allow rule is added.
- Updated English/Korean connection guides, SDK docs and the offline language-switching manual. Workbench keeps saved completion separate from the current verdict and shows differences such as `LC_ALL`.

**Verification:** the actual macOS Claude desktop Code session used core 1.8.10 and ran one registered check with eight passing tests, file-version MATCH and native Stop `SATISFIED`. Auto initially blocked the check; the owner approved that one command, then restored Auto. This evidence is reused, not described as a new model call on 1.8.11. Fresh release-binary, SDK and hook-boundary checks are listed in [VERIFICATION.json](VERIFICATION.json). A separate CLI denial trial only qualified resolution; its intended work remained unfinished.

Claude host installation remains macOS-only. Windows/Linux core and SDK tests do not establish Claude host support there. Existing releases, records, contracts and settings are retained. No new model, daemon, GPU control, memory/soak test or approval-policy change is introduced.

[Downloads](DOWNLOADS.md) · [Claude guide](CLAUDE_CONNECTION.md) · [Host installation](HOST_CONNECTIONS.md) · [SDK guide](SDK_README.md)

The SDK verification example also handles the additive `statusView` response while still comparing every execution field and requiring the current observer to be `SATISFIED`.

## 한국어

- Claude 어댑터에 공식 `PostToolBatch` 관측을 추가했습니다. 거절된 일반 호출은 세션·턴·도구 ID·입력이 모두 일치할 때만 종료를 연결합니다. 묶음 전체를 먼저 검증하고 응답 원문 대신 해시를 남깁니다.
- 등록 검사는 실제 실행 영수증과 파일 버전이 일치해야 통과 근거가 됩니다. 결과 누락·신원 충돌·진행 중인 검사는 `UNKNOWN`을 유지합니다. 응답 문구로 통과 CHECK를 만들거나 종료 코드 0을 추정하지 않습니다.
- 하네스·워크벤치·SDK 압축 파일에 같은 9개 훅과 설치·업데이트·복구 도구를 넣었습니다. 새 리비전을 이전 버전 옆에 준비하고 현재 설정 해시를 대조합니다. 다른 훅·권한·MCP 설정은 보존하며 영구 허용 규칙을 추가하지 않습니다.
- 영·한 연결 안내와 SDK 문서, 언어 전환이 가능한 오프라인 매뉴얼을 갱신했습니다. Workbench는 저장된 완료와 현재 조회 판정을 구분하고 `LC_ALL` 등의 차이를 표시합니다.

**검증 범위:** 실제 macOS Claude 앱 Code 세션은 코어 1.8.10으로 등록 검사 1회·8개 테스트, 파일 버전 MATCH와 Stop의 `SATISFIED`를 확인했습니다. 최초 Auto 차단 후 검사 한 건을 개별 승인하고 Auto로 복원한 결과입니다. 이 근거를 재사용하며, 새 1.8.11에서 AI 세션을 다시 실행했다고 안내하지 않습니다. 새 배포 실행 파일·SDK·훅 경계 검사는 [VERIFICATION.json](VERIFICATION.json)에 구분합니다. 별도 CLI 거절 시험은 종료 연결만 확인했고 의도한 업무는 완료하지 못했습니다.

Claude 호스트 설치 검증은 macOS에 한정합니다. Windows·Linux의 코어·SDK 검사와는 별개입니다. 이전 버전·기록·계약·설정은 보존합니다. 모델·상주 프로세스·GPU 제어·메모리 시험이나 승인 정책 변경은 추가하지 않았습니다.

[다운로드](DOWNLOADS.md) · [Claude 안내](CLAUDE_CONNECTION_KR.md) · [호스트 설치](HOST_CONNECTIONS_KR.md) · [SDK 안내](SDK_README_KR.md)

SDK 검증 예제도 새 `statusView` 응답에 맞췄습니다. 기존 실행 결과의 모든 항목을 대조하고 현재 조회 판정이 `SATISFIED`인지 별도로 확인합니다.
