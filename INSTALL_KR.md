# CALF 설치하고 첫 작업 시작하기

[소개](https://calf.vibepackr.com/) · [다운로드](https://calf.vibepackr.com/#downloads) · [화면으로 따라가기](https://calf.vibepackr.com/manual/?lang=ko#install) · [English](INSTALL.md)

## 1. Workbench 받기

[다운로드 페이지](https://calf.vibepackr.com/#downloads)에서 내 컴퓨터에 맞는 파일을 고르세요. 화면으로 사용하려면 Workbench, 터미널에서 사용하려면 Harness를 선택합니다.

| 컴퓨터 | 필요한 환경 |
| --- | --- |
| Apple Silicon Mac | macOS 14 이상. Workbench 1.9.18은 서명과 Apple 공증을 적용했습니다. |
| Windows x64 | Microsoft Edge WebView2 Runtime. Windows 패키지에는 게시자 서명이 없습니다. |
| Linux x64 | Debian 13, GTK 3, WebKitGTK 4.1과 그래픽 데스크톱. 다른 배포판은 호환성을 따로 확인해야 합니다. |

받은 파일의 SHA-256을 같은 릴리즈 페이지의 `SHA256SUMS`와 비교하세요. 앱을 열 때는 운영체제의 정상적인 보안 확인 절차를 따릅니다.

## 2. 압축 풀고 열기

**압축 파일 전체를 새 폴더에 풀고** 구성 파일을 함께 보관하세요.

| 운영체제 | 열 파일 |
| --- | --- |
| macOS | `CALF Workbench.app` |
| Windows | `calf-terminal.exe` |
| Linux | 압축을 푼 폴더의 터미널에서 `./calf-terminal` 실행 |

Linux는 `tar -xzf FILE.tar.gz`로 압축을 풀면 실행 권한이 유지됩니다. `calf` 또는 `calf.exe`는 데스크톱 실행 파일 옆에 두세요. macOS에서는 둘 다 앱 안에 들어 있습니다.

## 3. 작은 작업 하나 시작하기

1. **Choose workspace**에서 작업할 프로젝트 폴더를 고릅니다.
2. **Connect AI**에서 평소 쓰던 AI를 선택합니다.
3. 원하는 결과, 그대로 둘 것, 확인 방법을 적습니다. **Use a request outline**을 누르면 초안을 잡는 데 도움이 됩니다.
4. 프로젝트의 검사 도구가 준비됐는지 확인하고, 요청을 검토한 뒤 **Submit**을 누릅니다.
5. **Diff**와 결과 요약을 열어 바뀐 파일과 검사 결과를 살펴봅니다.

CALF는 프로젝트에 준비된 unittest·설정된 pytest·지원되는 Cargo 통합 테스트·node:test 같은 검사를 사용합니다. 빠진 프로젝트 도구는 직접 설치하세요. 검사 항목을 고르는 것만으로 실행되지는 않으므로, 작업 뒤 결과를 확인해야 합니다.

지금 상태는 **Current**, 이전 결과는 **Recorded**에서 봅니다. 파일이나 검사 환경을 바꾸면 예전의 성공도 다시 확인해야 할 수 있습니다.

[첫 작업 안내](FIRST_TASK_KR.md) · [화면 매뉴얼 열기](https://calf.vibepackr.com/manual/?lang=ko#start)

## 이미 CALF를 사용 중이라면

`CALF_WORK_HOME` 전체와 계약·설정·이전 버전 폴더를 유지하세요. 새 프로그램도 같은 데이터 폴더를 사용합니다. 이전 작업은 시작할 때 쓰던 런타임이 필요할 수 있으므로 `runtimes` 폴더도 남겨두세요.

설치본을 바꾸기 전에 [업데이트·복구 안내](UPDATE.md)를 읽어보세요. Codex·Antigravity·Claude는 [호스트 연결 안내](HOST_CONNECTIONS_KR.md)를 따라 연결하고, 새 훅은 호스트의 정상적인 승인 단계에서 검토합니다.

CALF는 무료로 사용할 수 있습니다. AI 서비스의 계정·요금·승인 설정은 그대로 적용됩니다.
