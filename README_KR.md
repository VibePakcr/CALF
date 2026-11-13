# CALF

**Controlled Agent Lifecycle Framework**

AI에게 맡긴 작업이 어디까지 됐는지 확인하세요. CALF에서 요청 내용과 바뀐 파일, 검사 결과를 함께 보고 멈춘 작업을 이어갈 수 있습니다.

Codex·Antigravity·Claude Code와 함께 사용하는 가벼운 워크벤치입니다. Rust와 Tauri로 만들었으며 macOS·Windows·Linux에서 무료로 사용할 수 있습니다.

[소개](https://calf.vibepackr.com/) · [다운로드](https://calf.vibepackr.com/#downloads) · [설치](INSTALL_KR.md) · [매뉴얼](https://calf.vibepackr.com/manual/?lang=ko) · [English](README.md)

## 처음이라면 Workbench로 시작하세요

1. [내 운영체제에 맞는 Workbench](https://calf.vibepackr.com/#downloads)를 받아 새 폴더에 압축을 풉니다.
2. 앱을 열고 작업 폴더와 평소 쓰던 AI를 선택합니다.
3. 원하는 결과와 그대로 둘 것을 적습니다. 안내에 따라 프로젝트의 검사 도구가 준비됐는지 확인하고 작업을 제출합니다.

[설치 안내](INSTALL_KR.md)와 [화면 매뉴얼](https://calf.vibepackr.com/manual/?lang=ko#start)에서 순서대로 따라갈 수 있습니다.

![Workbench 1.9.16 첫 작업 안내](ui-macos-first-task.png)

Workbench 1.9.16의 첫 작업 화면입니다. [Windows·Linux 화면](UI_GUIDE_KR.md)도 볼 수 있습니다.

## 이런 일을 할 수 있습니다

- **바뀐 파일 살펴보기.** Diff에서 변경 내용과 해당 파일의 검사 결과를 함께 봅니다.
- **확인이 필요한 작업 찾기.** 현재 상태와 이전 결과, 다음에 할 일을 확인합니다.
- **멈춘 작업 이어가기.** 이전 시도를 남겨두고 준비가 되면 Resume으로 재개합니다.
- **필요한 자료 찾기.** Repository Intelligence에서 지난 결정을 찾고, Engineering knowledge에서 개발 자료를 참고합니다.

Repository Intelligence는 CALF에 기본으로 포함돼 있습니다. GCN/MCL로 작업 순서와 바꿀 파일, 검사 항목을 정리합니다. Computer Engineering Pack / Pattern / Method의 기본 참조 목록 367개에 보유한 자료를 더할 수도 있습니다.

## 사용하는 방식에 맞춰 고르세요

| 하고 싶은 일 | 선택 |
| --- | --- |
| 화면에서 작업을 따라가고 파일과 결과 확인하기 | **Workbench 1.9.16** |
| 터미널 명령·호스트 훅·MCP로 사용하기 | **Harness 1.8.19** |
| 직접 만든 도구 연결하기 | **SDK 0.2.11** |

Workbench와 Harness는 같은 코어를 사용합니다. CALF 데이터 폴더를 같게 지정하면 같은 작업을 볼 수 있습니다. 업데이트할 때는 이 폴더와 이전 작업의 런타임을 유지하세요.

[다운로드](DOWNLOADS.md) · [업데이트 내용](RELEASE-NOTES.md) · [이전 버전](LEGACY.md)

## 더 알아보기

[첫 작업](FIRST_TASK_KR.md) · [AI 연결](HOST_CONNECTIONS_KR.md) · [Repository Intelligence](REPOSITORY_BUILTIN_KR.md) · [개발 자료](ENGINEERING_KNOWLEDGE_KR.md) · [저장된 파일](ARTIFACT_LIFECYCLE_KR.md) · [로컬 MCP 도구](MCP_TOOL_EVALUATION_KR.md) · [SDK](SDK_README_KR.md)

로컬 모델 연결은 미리보기 기능입니다. 사용하려면 먼저 [Ollama·MLX 안내](LOCAL_MODELS_KR.md)를 확인하세요.

CALF만으로도 사용할 수 있습니다. 영상 작업을 관리할 때는 선택형 [FFmpeg 확장](https://github.com/VibePakcr/CALF-Extensions)을 추가할 수 있습니다. [CALF Connect](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/INSTALL_KR.md)는 VS Code·Cursor·PyCharm·Antigravity IDE에서 Workbench를 여는 개발 프리뷰입니다.

## 사용 조건

CALF는 무료로 사용할 수 있습니다. 코어 소스는 공개하지 않으며 오픈소스 사용권을 부여하는 제품이 아닙니다. 무단 개변조·리버스 엔지니어링·재배포는 적용되는 약관과 법률에 따라 법적 제재를 받을 수 있습니다. 확장에는 별도로 제공하는 SDK·Adapter·MCP 인터페이스를 사용하며, 각 확장 자료의 라이선스를 따릅니다. 자세한 조건은 패키지에 포함된 라이선스 문서를 확인하세요. 연결한 AI 서비스의 요금과 이용 조건은 별도입니다.

## CALF 구조

![CALF 구조 — 한국어](calf-overview-kr-20261111.png)

![CALF architecture — English](calf-overview-en-20261111.png)
