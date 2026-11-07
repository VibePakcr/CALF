# CALF Harness 1.8.8 · Workbench 1.9.3 · SDK 0.2.2

[Downloads](DOWNLOADS.md) · [English](README.md) · [한국어](README_KR.md)

## English

### Antigravity long-output fix

Antigravity adds a preview header when a command’s output is too long to display. CALF could miss the command’s exit code after that header and leave the observation pending. Both editions now recognize this specific host envelope after matching its session, step and transcript location. Text printed by the command cannot serve as its terminal result. Missing, mismatched or contradictory evidence still stays UNKNOWN.

The native SessionStart and PreInvocation responses already used typed injection messages. Their behavior is retained. The separate, older compatibility bridge used in one local installation is not included in this distribution.

### Guides and companion downloads

The English and Korean README files, download page, SDK protocols, host guides, screenshot captions and offline manual have been revised. The manual keeps its EN/KR switch, top navigation and embedded screenshots. Those screenshots were captured in Workbench 1.9.2 and remain labeled with that version.

SDK 0.2.2 updates documentation and release-verification version checks. Its task and runtime APIs are unchanged. The new Host Connections kit accepts Harness 1.8.7 and 1.8.8, pins the selected binary and records its actual version in Claude adapter receipts. Claude integration remains qualified on macOS; Codex and Antigravity use the native installer.

### Verification

The packaged macOS ARM64, Windows x64 and Linux x64 cores are checked with real local Python/Node processes, independent artifact validation, loopback HTTP and MCP, stale-evidence rejection, cancellation and retained-runtime recovery. Both editions are also exercised through native Antigravity hooks with a real long-output command and a registered check. Workbench’s native bridge is checked on each OS. Exact results and binary hashes are in VERIFICATION.json.

The native Rust suite passed 49 tests. macOS host-kit tests cover actual 1.8.8 hook invocation, settings merge, stale-hash refusal, update, rollback and interrupted apply recovery. Prior live Codex, Antigravity and Claude sessions are retained evidence from earlier versions. No paid model calls were made for this patch. Windows/Linux desktop-window interaction and memory or long-running behavior were not tested.

### Update without losing work

Extract into a new folder and keep your complete records home, including `runtimes` and `work-v1`. Existing queued tasks continue through their retained starting runtime. To update native hooks, use the existing installation root and normal host review flow. Keep older binaries referenced by registered checks. The updater does not reset contracts, settings or history. [Step-by-step update guide](UPDATE.md).

macOS packages have ad-hoc integrity signatures, not Apple notarization. Windows packages have no publisher signature; Workbench needs WebView2. Linux Workbench needs GTK 3, WebKitGTK 4.1 and a graphical session; Debian 13 is the tested Linux host. No Intel Mac, ARM64 Windows/Linux or musl build is included.

## 한국어

### Antigravity의 긴 출력 처리 수정

Antigravity는 명령 출력이 길면 앞부분에 미리보기 안내를 붙입니다. CALF가 그 뒤의 종료 코드를 놓쳐 실행 기록을 대기 상태로 남기는 경우를 고쳤습니다. 두 에디션 모두 세션·단계·대화 기록 위치를 대조한 뒤 이 안내 형식에 있는 종료 정보를 읽습니다. 명령이 출력한 성공 문구는 종료 근거로 사용하지 않습니다. 근거가 없거나 경로가 다르거나 결과가 충돌하면 UNKNOWN을 유지합니다.

네이티브 SessionStart·PreInvocation 응답은 이미 올바른 주입 메시지 형식을 사용하고 있었으며 그대로 유지합니다. 개인 환경에서 쓰던 이전 호환 브리지는 이번 배포에 포함하지 않습니다.

### 문서와 연결 키트

영·한 README, 다운로드 안내, SDK 규약, 호스트 연결 안내, 화면 설명과 오프라인 매뉴얼을 다듬었습니다. 매뉴얼의 EN/KR 전환, 상단 메뉴와 내장 스크린샷은 유지합니다. 화면은 Workbench 1.9.2에서 촬영한 자료이므로 실제 촬영 버전을 그대로 표시했습니다.

SDK 0.2.2는 문서와 배포 검수기의 대상 버전을 갱신한 패치입니다. 작업·런타임 API는 바뀌지 않았습니다. 새 Host Connections 키트는 Harness 1.8.7·1.8.8을 지원하며, 선택한 실행 파일을 해시로 확인하고 Claude 기록에도 실제 버전을 남깁니다. Claude 연결은 macOS에서 검증했습니다. Codex·Antigravity는 네이티브 설치기를 사용합니다.

### 확인한 내용

최종 macOS ARM64·Windows x64·Linux x64 코어로 실제 Python·Node 프로세스, 독립 산출물 검사, 로컬 HTTP·MCP, 변경된 파일의 근거 무효화, 취소와 원래 런타임을 통한 재개를 확인했습니다. 두 에디션의 네이티브 Antigravity 훅에는 실제 긴 출력 명령과 등록 검사를 연결했습니다. 각 OS의 Workbench 네이티브 연결도 확인했으며, 완료된 결과와 바이너리 해시는 VERIFICATION.json에 남깁니다.

Rust 단위 검사 49개를 통과했습니다. macOS 연결 키트 시험에서는 1.8.8 실제 훅 호출, 설정 병합, 오래된 해시 거절, 업데이트·이전 버전 선택과 적용 중단 복구를 확인했습니다. 과거 Codex·Antigravity·Claude 실서비스 세션은 이전 버전의 근거로 보존합니다. 이번 패치는 유료 모델을 새로 호출하지 않으며, Windows·Linux 새 창 조작이나 메모리·장시간 시험 결과를 추가하지 않습니다.

### 기존 작업을 보존하는 업데이트

새 폴더에 압축을 풀고 `runtimes`·`work-v1`을 포함한 기존 기록 폴더 전체를 유지하세요. 대기 중인 작업은 시작할 때 보관한 런타임으로 이어집니다. 네이티브 훅은 같은 설치 위치에서 갱신하고 호스트가 요청하는 검토 절차를 따릅니다. 등록 검사에서 참조하는 이전 실행 파일은 보관하세요. 계약·설정·이력은 초기화하지 않습니다. [업데이트 순서](UPDATE.md).

macOS는 공증되지 않은 ad-hoc 무결성 서명을 사용합니다. Windows 게시자 서명은 없으며 Workbench에는 WebView2가 필요합니다. Linux Workbench에는 GTK 3·WebKitGTK 4.1·그래픽 세션이 필요하고 Debian 13에서 검증했습니다. Intel Mac, Windows·Linux ARM64, musl 패키지는 포함하지 않습니다.
