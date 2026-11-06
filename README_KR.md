# CALF — Controlled Agent Lifecycle Framework

[English](README.md) · [한국어](README_KR.md)

**[바로 다운로드 · Direct downloads](DOWNLOADS.md)** — 릴리즈 목록을 열지 않고 OS별 파일을 받습니다. 앱 내부 브라우저에서 릴리즈 조회 오류가 나면 이 링크를 이용하거나 외부 브라우저에서 여세요.

CALF는 가볍게 로컬에서 사용하는 **AI 실행 하네스이자 개발 워크벤치**입니다. AI 공급자에 범위를 정한 작업을 위임하고, 실제 실행을 기록하고, 등록된 요구사항·검사·파일 버전 근거로 변경을 검증합니다. 실패하거나 완료되지 않은 작업은 그 상태와 근거를 보존하여 확인·재개·복구할 수 있게 합니다.

Harness는 화면 없는 네이티브 런타임입니다. 기존 Codex·Antigravity 호스트에 훅으로 연결하거나 데스크톱 창 없이 작업을 실행할 수 있습니다. Workbench는 같은 코어와 새 작업 기록을 관측·제어하는 Rust + Tauri 화면을 제공합니다. 전체 IDE를 만드는 대신 AI의 실행·변경·검수에 집중하며, 기존 호스트의 승인·샌드박스 정책을 대체하지 않습니다.

**전문적인 싱글 에이전트 작업에 집중합니다.** Codex·Antigravity의 지원 연결 경로를 사용하며 실행·검사·검수 단계를 구분하여 기록합니다. 멀티 에이전트 구성을 요구하지 않습니다.

## 무료 사용 · 코어 비공개 · 공식 확장

**CALF는 무료로 사용할 수 있도록 배포합니다. 코어 소스 코드는 공개하지 않습니다.** 다운로드 저장소가 공개되어 있다는 사실이 오픈소스 제공이나 구현에 대한 권리 이전을 의미하지는 않습니다.

**CALF의 불법·무단 개변조는 금지합니다.** 배포 정책상 독점 소유인 CALF 런타임의 리버싱·디컴파일·디스어셈블·바이너리 패치·개조를 허용하지 않습니다. 위반 시 적용 법률에 따라 법적 조치를 취할 수 있습니다. 무료 사용은 코어의 추출·수정·변조본 재배포를 허락하는 것이 아닙니다.

확장은 코어를 개변조하지 않고 공식 **SDK·어댑터·MCP** 인터페이스를 통해 제공합니다. **이번 릴리즈에서 제공하는 기능:** 범위가 제한된 공급자·검사 어댑터 명세, 로컬 JSON 작업 인터페이스, 읽기 전용 stdio Local MCP입니다. **개발용 SDK 0.2.0을 별도로 제공합니다:** [한글 안내](SDK_README_KR.md), [English guide](SDK_README.md), [다운로드](https://github.com/thermany/CALF/releases/download/sdk-v0.2.0/CALF-SDK-0.2.0.zip). macOS ARM64·Windows x64·Linux x64에서 실제 검증했습니다. SDK 소스는 확장 라이선스로 제공하며 CALF 코어는 계속 비공개입니다.

이 제한은 CALF 자체의 비공개 구현에 적용합니다. 사용자가 소유한 프로젝트 코드나 지원되는 설정·확장 인터페이스를 제한하는 의미가 아닙니다. 함께 사용하는 외부 구성요소에는 각각의 라이선스가 적용되며 `THIRD-PARTY-NOTICES.txt`에 고지를 포함합니다.

## 두 가지 에디션

| 에디션 | 버전 | 용도 |
|---|---|---|
| **Harness** | [1.8.6](https://github.com/thermany/CALF/releases/tag/v1.8.6) | 기존 Codex·Antigravity 훅과 독립 headless 작업. WebView 없음 |
| **Workbench** | [1.9.1](https://github.com/thermany/CALF/releases/tag/v1.9.1) | 같은 실행 코어와 새 작업 기록을 사용하는 Rust + Tauri 데스크톱 |

먼저 스크린샷이 포함된 **[CALF_mannual.html](https://github.com/thermany/CALF/releases/download/v1.9.1/CALF_mannual.html)**을 내려받아 로컬에서 열어 주세요. 상단 고정 메뉴와 **EN / KR** 버튼으로 목차·본문 전체·화면 설명을 전환할 수 있습니다. 모든 패키지에 같은 오프라인 매뉴얼이 들어 있습니다. [릴리즈 노트](RELEASE-NOTES.md)와 [SHA256SUMS](SHA256SUMS)도 확인하세요.

## 다운로드

| 플랫폼 | Harness 1.8.6 | Workbench 1.9.1 |
|---|---|---|
| macOS Apple Silicon | [ZIP](https://github.com/thermany/CALF/releases/download/v1.8.6/CALF-Harness-1.8.6-macos-arm64.zip) | [ZIP](https://github.com/thermany/CALF/releases/download/v1.9.1/CALF-Workbench-1.9.1-macos-arm64.zip) |
| Windows x64 | [ZIP](https://github.com/thermany/CALF/releases/download/v1.8.6/CALF-Harness-1.8.6-windows-x86_64.zip) | [ZIP](https://github.com/thermany/CALF/releases/download/v1.9.1/CALF-Workbench-1.9.1-windows-x86_64.zip) |
| Linux x64 | [tar.gz](https://github.com/thermany/CALF/releases/download/v1.8.6/CALF-Harness-1.8.6-linux-x86_64.tar.gz) | [tar.gz](https://github.com/thermany/CALF/releases/download/v1.9.1/CALF-Workbench-1.9.1-linux-x86_64.tar.gz) |

해시를 확인하고 전체 압축을 푸세요. Workbench는 **CALF Workbench.app**, `calf-terminal.exe`, `./calf-terminal` 중 해당 플랫폼의 실행 파일로 엽니다. Harness는 `./calf --help` 또는 PowerShell의 `.\calf.exe --help`로 시작합니다. 간편 작업 실행은 지원되는 unittest·pytest·Cargo 검사를 찾으며 프로젝트 검사 도구는 별도 준비해야 합니다.

```sh
./calf task connect codex
./calf task run "/absolute/path/project" "버그를 수정하고 기존 검사는 보존해 주세요."
./calf task list
```

새 headless 작업과 Workbench는 같은 `CALF_WORK_HOME`을 사용합니다. 기존 1.8.4 훅의 `history.html`·계약·설정은 보존하지만, 기존 훅 기록을 Workbench 작업 목록으로 자동 변환하지는 않습니다. 훅 업그레이드는 같은 설치 루트로 수행하고 이전 버전 실행 파일을 유지하세요. 기존 1.8.4 배포 파일과 태그도 유지합니다.

## Workbench에서 확인하는 것

Task Flow·타임스탬프, Git Graph, Diff·Before / After, Evidence, Light Edit, 자동 감지·수동 추가 외부 에디터, 워커 터미널, 시스템 자원, 사용자가 선택한 로컬 참조를 한 화면에서 확인합니다. Git 관측은 읽기 전용입니다. 앱 인터페이스는 영어 기본이며 요청·파일명·본문 등은 CJK를 포함한 유니코드를 지원합니다.

## 지원 환경과 검증 범위

macOS 14 이상 ARM64, Windows x64, Linux glibc x64 패키지를 제공합니다. Workbench는 Windows에서 WebView2, Linux에서 GTK 3·WebKitGTK 4.1과 그래픽 세션이 필요합니다. Debian 13에서 검증했으며 모든 Linux 배포판을 보장하지 않습니다. Intel Mac·Windows/Linux ARM64·musl 빌드는 포함하지 않습니다.

이번 버전은 초기 공개 바이너리 릴리즈입니다. 실제 AI 작업은 로그인된 Codex로 검증했고, 세 운영체제의 코어는 합성 공급자와 실제 검사 프로세스로 검증했습니다. 새 메모리 장시간 시험과 직접 API 실서비스 검증은 수행하지 않았습니다. macOS는 ad-hoc 무결성 서명이며 Apple 공증은 아닙니다. Windows 게시자 서명도 없습니다. 자세한 범위는 릴리즈 노트를 참고하세요.

PASS는 등록한 검사와 요구사항의 근거 범위에 한정됩니다. 근거가 없거나 파일 버전이 달라지면 UNKNOWN으로 남아야 합니다. 로컬 기록과 원격 AI 추론은 별개이며, 원격 AI 사용 시 선택한 작업 문맥은 공급자에게 전달됩니다.

GitLab의 이전 릴리즈: [CALF 1.8.4](https://gitlab.com/vibepackr-group/CALF/-/releases/v1.8.4).

## Check Profile과 업데이트 후 작업 재개

두 에디션에 Python unittest·pytest와 제한된 Cargo 통합 테스트용 네이티브 Check Profile이 적용됩니다. 기존 실패를 기준선으로 기록하고, 테스트 실패·도구 부재·무효 근거를 구분하며, 실질적인 진전 없는 반복 시도를 중단합니다. 기존 실패도 면제하지 않습니다. 필수 검사가 해결되지 않으면 PASS가 될 수 없습니다.

Python은 프로젝트 `.venv`, `venv`, 명시적으로 활성화된 환경, 제한된 PATH 탐색 순서로 선택합니다. 검사에 사용한 인터프리터와 설치 패키지 메타데이터를 함께 기록합니다. Python·pytest·프로젝트 의존성을 자동 설치하지 않으며, 명시된 환경이 손상되면 다른 환경으로 조용히 바꾸지 않습니다. Cargo는 단일 패키지의 통합 테스트를 locked·offline으로 실행하는 범위입니다. workspace 전체·unit test·doctest 검증을 의미하지 않습니다.

새 대기열 작업은 생성 당시 런타임을 해시로 검증해 로컬 기록 폴더에 보존합니다. 업데이트 후 Resume는 그 런타임과 원래 검사·근거를 사용합니다. `runtimes`를 포함한 기록 폴더 전체를 유지하세요. 실행 버전을 입증할 수 없는 이전 작업을 임의로 이관하거나 성공 처리하지 않습니다. 고급 `calf run`의 직접 상태 경로는 원래 호환 런타임으로 실행해야 합니다.

**SDK 0.2.0**에는 `CalfClient.discover_checks()`와 `Check.from_discovered()`가 추가되어 네이티브 검사 명세를 사용자 어댑터에서 그대로 연결할 수 있습니다. [SDK 안내](SDK_README_KR.md), [프로토콜](SDK_PROTOCOL_KR.md), `examples/check_profiles.py`를 참고하세요. Python 표준 라이브러리만 사용하는 얇은 클라이언트이며 별도 에이전트 엔진이나 상주 서비스를 추가하지 않습니다.
