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
