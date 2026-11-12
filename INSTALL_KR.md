# CALF Workbench 설치

[English](INSTALL.md) · [다운로드](DOWNLOADS.md) · [첫 작업](FIRST_TASK_KR.md) · [화면 매뉴얼](CALF_mannual.html#install)

1. [다운로드](DOWNLOADS.md)에서 운영체제에 맞는 **Workbench 1.9.7**을 받습니다. macOS ARM64·Windows x64·Linux x64를 제공합니다. 받은 파일의 SHA-256을 릴리즈의 SHA256SUMS와 비교합니다.
2. **새 폴더**에 전체 압축을 풀고 파일을 함께 보관합니다. macOS는 CALF Workbench.app, Windows는 calf-terminal.exe를 실행합니다. Linux는 WebKitGTK 4.1과 런타임 의존성이 준비된 그래픽 데스크톱에서 ./calf-terminal을 실행합니다.
3. [첫 작업 안내](FIRST_TASK_KR.md)대로 폴더·기존 AI 연결·원하는 결과와 유지할 것·확인 방법을 정합니다.

기존 설치를 갱신할 때는 CALF_WORK_HOME 전체, 계약, 설정, 이전 버전 폴더를 보관하고 새 실행 파일에서도 같은 기록 위치를 사용합니다. 기존 작업은 이전 런타임에 고정될 수 있습니다. 관리형 실행기를 바꾸기 전에 [업데이트·복구](UPDATE.md)를 확인하세요. 공간 확보를 위해 이전 런타임을 삭제하지 마세요.

AI 계정·호스트와 프로젝트 검사 도구는 별도 준비가 필요합니다. 함께 들어 있는 hosts/ 키트는 Workbench 1.9.7을 지원하며 기존 SDK 0.2.4 압축본은 변경하지 않습니다. 1.9.7에는 이번 릴리즈의 연결 키트를 사용하세요. Claude 호스트 설치 검증은 macOS에 한정됩니다.

macOS 워크벤치는 Developer ID 서명과 Apple 공증을 적용했습니다. 하네스는 무결성 확인용 임시 서명본입니다. Windows에는 배포자 서명이 없습니다. 운영체제 경고는 평소의 보안 기준으로 검토하세요. 보호 기능을 끄도록 안내하지 않습니다. 플랫폼 요구 사항과 지원 실행 경로는 매뉴얼을 확인하세요.
