# CALF — Controlled Agent Lifecycle Framework

## 기록된 파일 조회와 되돌릴 수 있는 정리

하네스 1.8.16 · 워크벤치 1.9.12 · SDK 0.2.9입니다. **Artifacts**에서 어느 작업이 파일을 참조하고 왜 보존해야 하는지 확인합니다. 새로 만드는 작은 임시 텍스트에는 생성 근거와 보존 기한을 붙일 수 있습니다. 재생성 가능한 인덱스, 또는 참조가 모두 해제되고 기한이 지난 관리 파일만 미리보기와 명시적 확인을 거쳐 격리합니다. 복원은 새 파일을 덮어쓰지 않으며, 기존 소스·테스트·후보·기록·계약·설정은 계속 보호합니다. 상주 탐색과 영구 삭제는 없습니다. 격리는 파일을 보관하므로 디스크 여유 공간을 늘리지 않습니다.

[한국어 안내](ARTIFACT_LIFECYCLE_KR.md) · [English guide](ARTIFACT_LIFECYCLE.md)


## Repository Intelligence를 기본 기능으로 통합했습니다

하네스 **1.8.15**, 워크벤치 **1.9.11**, SDK **0.2.8**에서 필요한 모듈 기록·정확한 원문 조회·로컬 Git 캡처·저장된 HEAD/인덱스/작업 파일 버전·파일 관계 후보를 공통 Rust 코어로 제공합니다. [사용법과 범위](REPOSITORY_BUILTIN_KR.md)를 확인하세요.

선택 팩의 설치·검수와 Claude 이벤트 어댑터도 코어가 처리합니다. 이 경로에는 Python·Node가 필요하지 않습니다. 언어별 SDK는 얇은 연결층으로 유지하며, 프로젝트 검사·FFmpeg/ffprobe·기존 사용자 보호 연결은 각각의 의존성을 유지합니다. 현재 별도 확장은 FFmpeg만 제공합니다. 이전 패키지와 기록도 보존합니다.

참고 기록·Git 캡처·과거 PASS만으로 완료를 판정하지 않습니다. 현재 네이티브 검사와 정확한 파일 버전이 기준입니다. Rust 소스 분석은 관계 후보를 제공하며 Python 문법 전체나 의미적 정확성을 증명하지 않습니다.


새 Codex 세션에서 필요한 모듈 조회부터 실제 영·한 보고서 작성, 독립 검사, Workbench 기록 확인까지 마쳤습니다. [실제 결과와 확인 범위](REPOSITORY_SESSION_VERIFICATION_KR.md)를 함께 공개합니다.

[English](README.md) · [다운로드](DOWNLOADS.md) · [영·한 사용 매뉴얼](CALF_mannual.html)

CALF는 AI 에이전트 하나에게 맡긴 작업을 실행부터 검사·복구까지 감독하는 경량 로컬 도구입니다. 요청과 실제 변경, 검사 근거를 연결하고 실패하거나 미완료인 시도도 기록에 남깁니다. Codex·Antigravity는 네이티브 훅으로, Claude CLI와 앱의 로컬 Code 모드는 macOS 어댑터로 연결합니다. 각 호스트의 계정·모델·승인 정책은 유지합니다.

## 첫 작업에서 덜 신경 쓸 일

**폴더·AI 연결·원하는 결과를 정하면, CALF에서 변경 내용과 검사 근거, 끝나지 않은 시도를 함께 확인할 수 있습니다.**

처음에는 세 가지만 준비하세요. 작업할 폴더를 선택하고, 기존 AI 계정을 연결하고, 결과·유지할 것·확인 방법을 적습니다. 첫 작업 안내가 현재 선택 상태와 다음 단계를 보여줍니다. **Use a request outline**은 빈 입력창에 세 줄의 초안만 넣습니다. 내용을 채운 뒤 Submit을 누르세요.

![Workbench 1.9.7의 실제 첫 작업 안내](workbench-first-task.jpg)

[설치부터 시작](INSTALL_KR.md) · [첫 작업 단계별 안내](FIRST_TASK_KR.md) · [영·한 화면 매뉴얼](CALF_mannual.html)

## 최신 배포 · 2026-11-12

**Harness 1.8.16 · Workbench 1.9.12 · SDK 0.2.9**

macOS ARM64·Windows x64·Linux x64용 패키지가 공개됐습니다. 배포 공개가 기존 설치 앱이나 호스트 훅을 자동으로 바꾸지는 않으므로 설치·업데이트 안내에 따라 적용하세요. 기존 기록 위치·계약·설정과 과거 작업의 실행 파일을 보관하세요. 실제 검사와 적용 범위는 [VERIFICATION.json](VERIFICATION.json)에서 확인할 수 있습니다.

| 제품 | 용도 |
|---|---|
| 하네스 1.8.x | 창 없이 실행하는 코어와 기존 에이전트 훅 |
| Workbench 1.9.x | 같은 실행·기록 체계에 Rust + Tauri 작업 화면 추가 |
| SDK | Python·Node, Local MCP와 범용 어댑터를 통한 확장 |

## CALF 한눈에 보기

공통 코어, 필요한 맥락 조회, 실행·검수·복구와 확장 경계를 한 장에 정리했습니다. 2026년 11월 11일 배포 기준이며, Workbench 그림은 기능을 설명하기 위한 구성도입니다.

<p align="center">
  <a href="calf-overview-kr-20261111.png">
    <img src="calf-overview-kr-20261111.png" alt="CALF 공개 제품 개요: 하네스·Workbench·맥락·검수·복구·확장" width="760">
  </a>
</p>

[한글 원본 보기](calf-overview-kr-20261111.png) · [English infographic](calf-overview-en-20261111.png)

## MCP 도구도 계약과 검수에 연결

검토한 로컬 MCP 정책에서 읽기와 새 후보 생성을 실행하고, 실제 파일 버전과 등록 검사를 대조합니다. 실행안 준비와 승인을 구분하며, 응답이 끊겨도 같은 도구를 자동으로 다시 보내지 않습니다. 원래 정책에 설정된 로컬 복구는 종료 영수증과 후보 해시를 확인하고 새 검사를 실행합니다. macOS·Windows·Linux에서 두 제품의 같은 경로를 검증했습니다.

기존 첫 작업 안내는 그대로 유지합니다. MCP 확장은 필요한 경우에만 연결하며, 상주 서비스·추가 모델·에이전트 풀을 요구하지 않습니다. [MCP 안내](MCP_TOOL_EVALUATION_KR.md) · [SDK](SDK_README_KR.md) · [검증 범위](VERIFICATION.json).

## 필요한 판단과 작업 결과를 더 쉽게 확인하세요

Attention에서 사용자의 판단이 필요한 작업을 모아 보고, 결과 요약에서 변경 파일·검사 결과·현재 판정을 확인할 수 있습니다. 요청 도움 기능은 기존 초안을 유지하면서 원하는 결과와 확인 방법을 정리합니다. Light | Dark 토글로 중앙 영역을 전환하거나, CJK 작업 검색과 단축키로 작업을 찾을 수 있습니다. 좁은 창에서는 모니터를 접고, 접힌 동안에는 자원 조회도 멈춥니다.

하네스에도 같은 읽기 전용 Attention 조회를 제공합니다. 조회나 검색이 작업을 실행하거나 승인하지 않으며, 완료 기준과 기존 기록은 그대로 유지합니다. [사용 안내](WORKBENCH_CLARITY_KR.md) · [검증 범위](VERIFICATION.json).

## 할 수 있는 일

- 작업 계약과 검사 기준을 정하고 현재 파일과 검사 증거가 맞는지 확인합니다.
- Task Flow, Git Graph, Diff, Evidence와 워커 터미널로 진행 상황을 봅니다.
- unittest·pytest·Cargo 통합 검사·node:test를 사용하며 필요한 도구는 프로젝트에서 준비합니다.
- 선택한 로컬 참조만 다음 작업에 첨부하고 MCP·SDK·어댑터로 다른 런타임을 연결합니다.
- 같은 기록 위치에서 작업을 이어갑니다. 이전 작업에 고정된 실행 파일과 남은 시도 예산도 유지합니다.

Workbench **Task status**는 저장된 완료와 현재 조회 판정을 나눠 보여줍니다. 파일이 같아도 `LC_ALL`이 다르면 현재 `UNKNOWN`을 유지하며 차이를 표시합니다. 상세 정보는 필요할 때 읽습니다. 추가 모델·상시 서버·GPU 제어 연산은 필요하지 않습니다.

## 설치와 업데이트

[다운로드](DOWNLOADS.md)에서 macOS ARM64, Windows x64, Linux x64용 제품을 선택하고 새 폴더에 압축을 푸세요. 기존 기록 위치(`CALF_WORK_HOME`)·계약·설정과 이전 실행 파일은 보관하세요. 호스트 훅은 같은 설치 위치에서 검토 후 업데이트하고 새 세션으로 확인합니다. 이미 열린 세션을 강제로 바꾸거나 영구 허용 규칙을 추가하지 않습니다.

[호스트 연결](HOST_CONNECTIONS_KR.md) · [Claude 안내](CLAUDE_CONNECTION_KR.md) · [SDK 안내](SDK_README_KR.md) · [상태 조회](STATUS_CONTEXT_KR.md) · [이전 릴리즈](https://github.com/VibePakcr/CALF/releases)

Claude 호스트 어댑터는 macOS에서만 검증했습니다. Windows·Linux용 코어·SDK 검증과는 별개입니다. macOS 앱은 무결성 확인용 임시 서명본이며 Apple 공증본은 아닙니다. Windows 패키지에는 배포자 서명이 없습니다.

## Workbench 화면

![저장된 완료와 현재 조회 판정](workbench-status.png)

실제 Workbench 1.9.5에서 Claude 검사 기록을 조회한 화면입니다. 저장된 통과와 LC_ALL이 다른 현재 조회의 UNKNOWN을 구분합니다. 1.9.7에도 같은 상태 화면을 제공합니다.

[Task Flow](workbench-task-flow.png) · [Diff](workbench-diff.png) · [Runtime Work](workbench-runtime.png): 이전 1.9.2의 실제 기록 화면도 보존했습니다. 

![Diff · 보존된 실제 1.9.2 화면](workbench-diff.png)

![Runtime Work · 보존된 실제 1.9.2 화면](workbench-runtime.png)

## 무료 사용 · 비공개 코어 · 공식 확장

**CALF는 무료로 사용할 수 있지만 코어 소스는 공개하지 않습니다.** 공개 다운로드 저장소가 코어를 오픈소스로 제공한다는 뜻은 아닙니다. 코어의 무단 리버스 엔지니어링·디컴파일·디스어셈블·바이너리 패치·개변조를 허용하지 않으며, 위반 시 관계 법령에 따른 법적 제재를 받을 수 있습니다. 무료 사용은 코어 수정·추출·개변조본 재배포 권한을 포함하지 않습니다.

확장은 제공되는 **SDK·Adapter·MCP** 인터페이스로 구현하세요. SDK 소스는 별도의 통합 라이선스를 따르며 코어 구현은 비공개로 유지합니다. 이 제한은 사용자가 소유한 프로젝트 코드나 지원되는 설정·확장 인터페이스를 제한하려는 것이 아닙니다. 함께 배포하는 외부 구성요소의 라이선스와 고지는 유지합니다.

[선택형 FFmpeg 확장팩](https://github.com/VibePakcr/CALF-Extensions) · [릴리즈 변경사항](RELEASE-NOTES.md)
