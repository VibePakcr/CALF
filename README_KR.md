# CALF

**Controlled Agent Lifecycle Framework**

AI 에이전트 하나의 작업을 요청부터 실행·검수·복구까지 연결하는 경량 하네스·워크벤치입니다. Codex·Antigravity·Claude Code와 함께 사용하며, Headless 하네스와 Rust + Tauri 워크벤치가 하나의 Rust 코어를 공유합니다.

**무료 사용 · 비공개 바이너리 코어 · macOS / Windows / Linux**

[다운로드](DOWNLOADS.md) · [영·한 매뉴얼](CALF_mannual.html) · [English](README.md) · [최신 안내](CURRENT_RELEASE_KR.md)

## 최신 배포

하네스 **1.8.19** · 워크벤치 **1.9.16** · SDK **0.2.11**

첫 작업에서는 작업 폴더·AI 연결·요청·검사 준비·결과 확인을 한 흐름으로 안내합니다. 일반 안내는 읽기 쉬운 시스템 글꼴을, 경로·코드·실행 기록은 고정폭 글꼴을 사용합니다. **Current / Recorded / Next**를 구분해 지금의 판정과 보존된 결과, 필요한 다음 행동을 읽을 수 있습니다. 앱 아이콘의 흰색 바탕에도 둥근 모서리를 적용했습니다.

[새 화면 안내](UI_GUIDE_KR.md) · [변경 내용](RELEASE-NOTES.md) · [이전 배포 — Legacy](LEGACY.md)

## CALF로 할 수 있는 일

- **범위를 정해 위임합니다.** 싱글 에이전트 흐름과 기존 호스트의 계정·승인 규칙을 유지합니다.
- **실제 작업을 봅니다.** Task Flow·Git Graph·Diff·실행 출력·결과 요약으로 요청, 변경 파일과 검사 영수증을 연결합니다.
- **근거로 완료를 판단합니다.** 등록 검사는 현재 파일과 실행 문맥에 맞아야 합니다. 정상 종료나 AI의 주장만으로 완료 처리하지 않습니다.
- **기록을 남기고 이어갑니다.** 시도 기록, 명시적인 재개, 보호 파일, 복원 가능한 산출물 격리로 이전 작업을 버리지 않고 계속할 수 있습니다.
- **필요한 로컬 문맥만 읽습니다.** 내장 Repository Intelligence와 공학 지식 조회는 CPU에서 제한된 범위로 실행합니다. 추가 에이전트·로컬 모델·상주 인덱싱 서비스는 필요하지 않습니다.
- **선택한 도구를 연결합니다.** Local MCP·Adapter·SDK로 통제되는 실행 경로를 확장합니다. VibePackr는 선택 사항이며 CALF만으로도 사용할 수 있습니다.

로컬 모델 연결은 미리보기 기능입니다. 모델 목록 연결과 작업 완료는 구분하며, [Ollama·MLX의 실제 검증 범위](LOCAL_MODELS_KR.md)를 확인해야 합니다.

## 하네스와 워크벤치

**하네스 1.8.x**는 CLI·호스트 훅·MCP 연동을 위한 Headless 제품입니다. 같은 CALF 데이터 폴더로 **워크벤치 1.9.x**를 열면 하네스에서 남긴 기록도 볼 수 있습니다. 워크벤치가 별도의 완료 판정 엔진을 만들지는 않습니다. 업데이트할 때 기존 작업 런타임과 기록을 유지하세요.

## 첫 화면

![Workbench 1.9.16의 실제 첫 작업 안내](ui-macos-first-task.png)

동일 배포 실행 파일을 별도 예제 기록으로 연 실제 화면입니다. [Windows·Linux와 결과 읽는 법](UI_GUIDE_KR.md)을 확인하세요. 화면의 시스템 전체 사용량은 CALF의 성능 측정이 아닙니다.

## 사용 안내와 확장

[시작하기](INSTALL_KR.md) · [호스트 연결](HOST_CONNECTIONS_KR.md) · [첫 작업](FIRST_TASK_KR.md) · [내장 Repository Intelligence](REPOSITORY_BUILTIN_KR.md) · [산출물 관리](ARTIFACT_LIFECYCLE_KR.md) · [MCP 도구 평가](MCP_TOOL_EVALUATION_KR.md) · [SDK](sdk/README_KR.md) · [검증 범위](VERIFICATION.json)

Repository Intelligence는 코어에 내장돼 있습니다. 별도 [CALF Extensions](https://github.com/VibePakcr/CALF-Extensions) 저장소에는 선택형 FFmpeg 확장을 제공합니다.

## 배포 조건

CALF는 무료로 사용할 수 있습니다. 코어 소스는 공개하지 않으며 오픈소스 사용권을 부여하는 제품이 아닙니다. 무단 개변조·리버스 엔지니어링·재배포는 적용되는 약관과 법률에 따라 법적 제재를 받을 수 있습니다. 확장에는 별도로 제공하는 SDK·Adapter·MCP 인터페이스를 사용하며, 각 확장 자료의 라이선스를 따릅니다. 자세한 조건은 패키지에 포함된 라이선스 문서를 확인하세요. 연결한 AI 서비스의 요금과 이용 조건은 별도입니다.

## 구조 한눈에 보기

![CALF 구조 — 한국어](calf-overview-kr-20261111.png)

![CALF architecture — English](calf-overview-en-20261111.png)


## IDE connection / IDE 연결

[CALF Connect installation](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/INSTALL.md) · [한국어 설치](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/INSTALL_KR.md) · [Actual-screen manual / 화면 매뉴얼](https://github.com/VibePakcr/CALF-Extensions/blob/main/ide-connect/MANUAL_KR.md). Optional local-install files for VS Code, Cursor, PyCharm and Antigravity IDE; actual flows observed on three operating systems. No task is automatically submitted.
