# Update CALF Workbench 1.9.26

## Workbench 1.9.26 — usable task space and interactive evidence graphs

Task observations and task records now have separate scrolling areas. **Start a task** and the execution records keep their own space when switching between Task Flow, Git Graph and Diff. Drag the divider to adjust the split, or focus it and use arrow keys; Enter restores the default.

In **Evidence graph**, drag a node to rearrange it, drag the background or scroll to move around, and use the zoom controls or Ctrl/⌘ + wheel. **Fit to view** fits the graph; **Reset layout** restores the original arrangement. Shift + arrow keys moves a focused node. These are temporary view changes: recorded evidence, relationships and completion decisions are unchanged.

Git Graph continues to show local commits and branches. It displays merges, local changes, conflicts, detached HEAD and tracking counts from local refs, with at most 20 recent commits. It does not fetch or modify the repository. A file dependency graph is a separate view and is not part of this update.

Update from 1.9.25 through Updates, or extract 1.9.26 into a new folder while keeping the existing records home. Earlier installations and rollback remain available. Harness 1.8.25 and SDK 0.2.11 are unchanged. [Update guide](UPDATE.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#workspace-graphs).

## Workbench 1.9.26 — 작업 공간 확보와 근거 그래프 조작

작업 관측 영역과 작업 기록 영역을 각각 스크롤합니다. Task Flow·Git Graph·Diff를 바꿔도 **Start a task**와 실행 기록에 필요한 공간을 유지합니다. 경계선을 끌어 비율을 조절하거나, 경계선에 초점을 두고 방향키를 사용하세요. Enter는 기본 비율로 되돌립니다.

**Evidence graph**에서 노드를 끌어 배치하고, 배경을 끌거나 스크롤하여 이동합니다. 확대·축소 버튼 또는 Ctrl/⌘ + 휠을 사용할 수 있습니다. **Fit to view**는 화면에 맞추고 **Reset layout**은 처음 배치로 복원합니다. 초점이 있는 노드는 Shift + 방향키로 이동할 수 있습니다. 화면을 위한 임시 조작이며 근거 기록·관계·완료 판정은 변경하지 않습니다.

Git Graph는 기존의 로컬 커밋·브랜치 보기입니다. 병합, 로컬 변경, 충돌, 분리된 HEAD, 로컬 추적 참조의 앞섬·뒤처짐을 표시하며 최근 커밋 최대 20개를 조회합니다. fetch나 저장소 변경은 수행하지 않습니다. 파일 의존 관계 그래프는 별도 보기이며 이번 변경에 포함하지 않습니다.

1.9.25의 Updates를 사용하거나 1.9.26을 새 폴더에 풀고 기존 기록 위치를 유지하세요. 이전 설치본과 롤백을 보존합니다. Harness 1.8.25와 SDK 0.2.11은 변경하지 않습니다. [업데이트 안내](UPDATE.md) · [온라인 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#workspace-graphs).


## Workbench 1.9.25 — a smaller Updates view

Updates shows the **running version**, at most one **verified newer prepared update**, and the **verified previous version** for rollback. A window still running an older version says so separately from the selected version. An update candidate must be newer than both.

Older installations move into collapsed **Retained versions**, grouped by version without repeated activation buttons. They are kept on disk. Failed candidate or rollback verification disables that action and explains the problem. Existing native activation and rollback verify the selected bytes again when used.

Nothing downloads or changes versions automatically. Records, contracts, settings, audit history and pinned task runtimes remain intact. The retained catalogue keeps its existing bound of 32 local entries. Harness 1.8.25 and SDK 0.2.11 are unchanged.

Update from 1.9.24 through Updates or extract 1.9.25 into a new folder with your existing records home. [Update guide](UPDATE.md) · [Online manual](https://calf.vibepackr.com/manual/?lang=en#update-view).

## Workbench 1.9.25 — 업데이트와 롤백을 간결하게

Updates에는 **실행 중인 버전**, **검증된 새 업데이트 후보 최대 하나**, **검증된 직전 롤백 버전**을 표시합니다. 이전 버전의 창이 계속 열려 있으면 선택된 버전과 구분해 알려줍니다. 업데이트 후보는 실행 중인 버전과 선택된 버전 모두보다 새로워야 합니다.

이전 설치본은 접힌 **Retained versions**에서 버전별로 묶어 조회합니다. 실행 버튼을 반복하지 않으며 파일은 그대로 보관합니다. 업데이트 후보나 직전 버전의 검증에 실패하면 해당 실행 기능을 비활성화하고 이유를 표시합니다. 실제 업데이트·롤백 때는 기존 네이티브 경로가 파일을 다시 검증합니다.

자동 다운로드나 자동 버전 전환은 없습니다. 기록·계약·설정·감사 이력·작업별 고정 런타임을 보존하며, 보관 목록 조회는 기존 로컬 항목 32개 한도를 유지합니다. Harness 1.8.25와 SDK 0.2.11은 변경하지 않습니다.

1.9.24의 Updates를 사용하거나 1.9.25를 새 폴더에 풀고 기존 기록 위치를 유지하세요. [업데이트 안내](UPDATE.md) · [온라인 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#update-view).


Current guide: Workbench **1.9.26** · Harness **1.8.25** · SDK **0.2.11**.

Use Updates or the [current downloads](DOWNLOADS.md). Keep the complete records home, contracts, preferences and pinned task runtimes. Extract into a new folder; linked host tasks continue in their original host. See the [current manual](https://calf.vibepackr.com/manual/?lang=en#update-view).

현재 안내는 Workbench 1.9.26 기준입니다. [다운로드](DOWNLOADS.md)와 [한국어 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#update-view)을 확인하세요. 기존 기록·계약·설정과 작업별 런타임을 보존합니다.

## Historical update notes / 과거 업데이트 기록

# Update CALF / CALF 업데이트

Harness **1.8.8** · Workbench **1.9.3** · SDK **0.2.2**

## English

1. Let active work finish, or request Pause and wait for its process to stop. Close the old Workbench window.
2. Back up your installation settings and the complete records home. Keep `history.html`, contracts, journal segments, indexes, `runtimes` and `work-v1` together.
3. Download the package for your OS and CPU from [Downloads](DOWNLOADS.md). Compare its hash with SHA256SUMS, then extract it into a new folder.
4. Use the same records home. `calf task home` shows the selected location. An explicit CALF_WORK_HOME or existing runtime configuration must still point there.
5. For native Codex/Antigravity hooks, run the new installer with the existing installation root and host homes. Review new commands through the host’s usual controls, then start a new session. For Claude, follow [the Host Connections guide](hosts/README.md).
6. Open a retained task, inspect its evidence and run a small registered check. Existing queued tasks resume through their saved starting runtime; newly created tasks use the new release.

Keep the previous package until you have checked the update. Do not overwrite live journals or restore old settings over later edits. A missing or modified retained runtime blocks resumption rather than silently selecting another binary.

Apps may save window size, sidebar state or other UI preferences while you use them. Keep those changes in your audit, but distinguish them from changes to models, permissions, hooks, credentials or contracts. If an unexplained change appears, retain both observations and investigate it before writing anything back.

## 한국어

1. 실행 중인 작업이 끝나기를 기다리거나 Pause를 요청하고 프로세스가 멈춘 뒤 이전 Workbench 창을 닫습니다.
2. 설치 설정과 기록 폴더 전체를 백업합니다. `history.html`, 계약, 저널 조각, 색인, `runtimes`, `work-v1`을 함께 보관하세요.
3. [다운로드](DOWNLOADS.md)에서 OS·CPU에 맞는 패키지를 받고 SHA256SUMS와 해시를 대조한 뒤 새 폴더에 압축을 풉니다.
4. 기존 기록 위치를 그대로 사용합니다. `calf task home`으로 선택된 위치를 확인할 수 있습니다. CALF_WORK_HOME이나 기존 런타임 설정을 사용한다면 같은 위치를 가리키도록 유지하세요.
5. Codex·Antigravity 네이티브 훅은 기존 설치 위치와 호스트 홈을 지정해 새 설치기로 갱신합니다. 호스트가 요청하는 명령 검토를 마친 뒤 새 세션을 시작하세요. Claude는 [연결 키트 안내](hosts/README_KR.md)를 따릅니다.
6. 이전 작업과 근거를 열어 보고 작은 등록 검사를 실행합니다. 기존 대기 작업은 보관한 시작 런타임으로 이어지고, 새로 만든 작업은 새 버전으로 시작합니다.

업데이트를 확인할 때까지 이전 패키지를 보관하세요. 실행 중인 저널이나 이후 변경한 설정 위에 오래된 백업을 덮어쓰지 마세요. 보관한 런타임이 없거나 바뀌었다면 다른 실행 파일로 바꾸지 않고 재개를 중단합니다.

앱 사용 중 창 크기·사이드바 같은 UI 설정이 자동 저장될 수 있습니다. 이런 변경도 감사 기록에 남기되, 모델·권한·훅·인증정보·계약 변경과 구분해 확인하세요. 설명되지 않는 변경이 있으면 전후 상태를 보존하고 원인을 확인한 뒤 처리합니다.

[Release notes / 변경 사항](RELEASE-NOTES.md) · [Offline EN/KR manual](MANUAL.md)
