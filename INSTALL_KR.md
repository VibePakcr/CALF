# CALF Workbench 설치

[English](INSTALL.md) · [다운로드](DOWNLOADS.md) · [첫 작업](FIRST_TASK_KR.md) · [화면 매뉴얼](CALF_mannual.html#install)

1. [다운로드](DOWNLOADS.md)에서 운영체제에 맞는 **최신 공개 Workbench**를 받습니다. 파일의 SHA-256을 해당 릴리즈의 SHA256SUMS와 비교합니다. 개발 후보와 공개 배포본은 구분합니다.
2. 압축 파일 전체를 **새 폴더**에 풀고 구성 파일을 함께 보관합니다. macOS는 CALF Workbench.app, Windows는 calf-terminal.exe를 엽니다. Linux는 그래픽 데스크톱에서 ./calf-terminal을 실행합니다.
3. [첫 작업](FIRST_TASK_KR.md)에 따라 프로젝트 폴더와 기존 AI 계정을 연결하고, 원하는 결과와 변경 한계를 적은 뒤 검사 항목을 찾습니다. 검사 항목을 찾았다는 표시가 실행·통과를 뜻하지는 않습니다.
4. 작업 뒤 Diff와 현재 결과 요약을 확인합니다. 파일이나 검사 환경이 달라지면 과거 성공도 현재는 UNKNOWN일 수 있습니다.

CALF는 독립적으로 무료로 사용할 수 있습니다. AI 서비스의 계정·요금·승인 규칙은 그대로 적용됩니다. Python·Cargo·Node 같은 도구는 해당 프로젝트를 검사할 때 필요합니다. 현재 네이티브 호스트 어댑터는 Rust로 실행하며, 선택적인 SDK 예제는 각 클라이언트 언어를 사용합니다.

## 운영체제 요구 사항

- macOS ARM64: macOS 14 이상. 해당 배포본의 Developer ID 서명·Apple 공증 상태를 확인합니다. 로컬 개발 후보는 별도 배포 검증이 필요합니다.
- Windows x64: Microsoft Edge WebView2 Runtime이 필요합니다. 현재 게시자 서명을 제공한다고 안내하지 않습니다. 운영체제의 보안 정책을 따르세요.
- Linux x64: GTK 3·WebKitGTK 4.1이 필요합니다. 검증 기준은 Debian 13이며 다른 배포판까지 자동으로 보증하지는 않습니다.

## 기존 설치본을 사용 중이라면

CALF_WORK_HOME 전체와 계약·설정·이전 버전 폴더를 유지합니다. 새 실행 파일도 같은 데이터 폴더를 사용합니다. 이전 작업은 기존 런타임에 고정돼 있을 수 있습니다. 관리형 실행 경로를 바꾸기 전에 [업데이트·복구](UPDATE.md)를 확인하고, 공간 확보를 위해 이전 런타임을 삭제하지 마세요.

Codex·Antigravity·Claude는 함께 제공되는 [호스트 키트](hosts/README_KR.md)와 [Claude 안내](hosts/claude/README_KR.md)를 사용합니다. 이미 설치돼 있다면 기존 연결부터 확인합니다. 새 Codex 훅 정의는 호스트의 정상적인 검토가 필요합니다. 패키지 공개만으로 실행 중인 세션이 바뀌거나 명령 권한이 부여되지는 않습니다.
