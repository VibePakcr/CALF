# CALF — Controlled Agent Lifecycle Framework

## 최신 배포판 · 2026-11-09

**하네스 1.8.10 · Workbench 1.9.5 · SDK 0.2.3**

저장된 실행 결과와 현재 조회 판정을 나눠 보여줍니다. 검사 당시와 조회 환경의 `LC_ALL` 등이 다르면 어떤 항목이 바뀌었는지 확인할 수 있습니다. 과거 통과 결과로 현재의 `UNKNOWN`을 덮어쓰지 않으며, 기존 기록·계약·설정은 유지합니다.

- [다운로드](DOWNLOADS.md) · [영·한 사용 매뉴얼](CALF_mannual.html) · [이번 변경사항](RELEASE-NOTES.md)
- [상태 조회 안내](STATUS_CONTEXT_KR.md) · [SDK 안내](SDK_README_KR.md)

이전 버전과 GCN 프리뷰의 안내·다운로드도 아래에 남겨 두었습니다.

**GCN/MCL 프리뷰:** 하네스 1.8.9와 워크벤치 1.9.4가 CPU 기반 셀·레인 제어를 네이티브 코어에서 함께 제공합니다. [안내](GCN_CORE_KR.md) · [다운로드와 검증 범위](GCN_RELEASE.md). 아래의 기존 정식 다운로드도 유지합니다.

**문서 개정판 docs.1:** 배포 패키지 안의 영·한 매뉴얼도 최신 교정본으로 맞췄습니다. 실행 코드와 기존 버전은 유지합니다. [변경 내용·검증 범위](DOCUMENTATION-RELEASE-20261107.1.md).

CALF는 AI의 작업 실행과 검수를 관리하는 가벼운 로컬 하네스·워크벤치입니다. 에이전트 하나에게 작업을 맡기고, 진행 과정과 실제 변경을 살펴본 뒤 요구사항을 충족했는지 검사합니다. 실패하거나 끝내지 못한 시도도 로컬 기록에 남아 원인을 확인하고 작업을 이어갈 수 있습니다.

**Harness 1.8.x**는 창 없이 실행합니다. **Workbench 1.9.x**는 같은 런타임과 작업 기록에 Rust + Tauri 화면을 더합니다. Codex·Antigravity는 네이티브 훅으로, Claude CLI·앱의 로컬 Code 모드는 별도 macOS 어댑터로 연결합니다. 각 호스트의 계정·모델·승인 정책은 그대로 사용합니다.

**Harness 1.8.8 / Workbench 1.9.3 변경 사항:** Antigravity에서 긴 출력이 잘려 표시되더라도 실제 종료 결과를 읽을 수 있도록 고쳤습니다. 세션·단계·대화 기록 위치가 모두 맞아야 결과를 인정하며, 근거가 없거나 서로 다르면 UNKNOWN을 유지합니다. 영·한 안내 문장도 읽기 쉽게 다듬었습니다.


**Repository Navigator:** [무료 탐색 확장팩·한영 실화면 매뉴얼](#무료-통합-저장소-탐색-확장팩).

## 세 호스트 연결 키트

[CALF 1.8.8 연결 키트](https://github.com/VibePakcr/CALF/releases/tag/docs-20261107.1)에 Codex·Antigravity·Claude 로컬 Code의 연동 방법을 정리했습니다. [한국어](hosts/README_KR.md) · [English](hosts/README.md). Claude 어댑터는 macOS에서 검증했습니다. [별도 팩 관리기·Repository 팩](https://github.com/VibePakcr/CALF-Extensions/releases/tag/docs-20261107.1)은 macOS·Windows·Linux에서 설치·복구를 검증했습니다. 연결 키트는 네이티브 엔진·워크벤치와 별도로 받습니다.


[English](README.md) · [한국어](README_KR.md)

**[바로 다운로드 · Direct downloads](DOWNLOADS.md)** — 릴리즈 목록을 열지 않고 OS별 파일을 받습니다. 앱 내부 브라우저에서 릴리즈 조회 오류가 나면 이 링크를 이용하거나 외부 브라우저에서 여세요.

## 주요 기능

- **작업과 검수:** 변경 범위와 필수 검사를 먼저 정합니다. 시도마다 결과 파일을 따로 보관합니다. 검사한 파일과 채택할 파일의 해시가 일치해야 채택할 수 있습니다.
- **작업 화면:** Task Flow, Git Graph, Diff, Evidence에서 진행 상황과 실제 변경, 검사 결과를 확인합니다. Runtime Work에서는 Python·Node·로컬 HTTP 어댑터 작업도 같은 기록으로 관리합니다.
- **업데이트와 재개:** 새 작업은 시작할 때 사용한 런타임을 보관합니다. 업데이트 후에도 원래 검사와 남은 시도 횟수로 이어갑니다. 응답을 잃은 요청은 같은 ID로 조회해 중복 실행을 피합니다.
- **확장과 자료 연결:** Python·Node SDK와 Local MCP를 제공합니다. 로컬 자료는 사용자가 선택한 참조만 다음 작업에 첨부합니다. MCP의 작업 제어 도구는 직접 켜야 사용할 수 있습니다.
- **검사 환경:** unittest·pytest·단일 패키지 Cargo 통합 테스트·node:test를 지원합니다. 필요한 도구와 의존성은 프로젝트에 미리 준비해 주세요.

CALF는 에이전트 하나의 작업에 집중합니다. 필요한 작업과 파일만 불러오며, 별도 모델이나 상주 서비스를 추가하지 않습니다.

## 무료 사용 · 코어 비공개 · 공식 확장

**CALF는 무료로 사용할 수 있도록 배포합니다. 코어 소스 코드는 공개하지 않습니다.** 다운로드 저장소가 공개되어 있다는 사실이 오픈소스 제공이나 구현에 대한 권리 이전을 의미하지는 않습니다.

**CALF의 불법·무단 개변조는 금지합니다.** 배포 정책상 독점 소유인 CALF 런타임의 리버싱·디컴파일·디스어셈블·바이너리 패치·개조를 허용하지 않습니다. 위반 시 적용 법률에 따라 법적 조치를 취할 수 있습니다. 무료 사용은 코어의 추출·수정·변조본 재배포를 허락하는 것이 아닙니다.

확장은 코어를 개변조하지 않고 공식 **SDK·어댑터·MCP** 인터페이스를 통해 제공합니다. **이번 릴리즈에서 제공하는 기능:** 범위가 제한된 공급자·검사 어댑터 명세, 로컬 JSON 작업 인터페이스, 자료 조회용 Local MCP와 제어 기능을 선택적으로 켜는 작업 MCP입니다. **개발용 SDK 0.2.2를 별도로 제공합니다:** [한글 안내](SDK_README_KR.md), [English guide](SDK_README.md), [다운로드](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-SDK-0.2.2-docs.1.zip). macOS ARM64·Windows x64·Linux x64에서 실제 검증했습니다. SDK 소스는 확장 라이선스로 제공하며 CALF 코어는 계속 비공개입니다.

이 제한은 CALF 자체의 비공개 구현에 적용합니다. 사용자가 소유한 프로젝트 코드나 지원되는 설정·확장 인터페이스를 제한하는 의미가 아닙니다. 함께 사용하는 외부 구성요소에는 각각의 라이선스가 적용되며 `THIRD-PARTY-NOTICES.txt`에 고지를 포함합니다.

## 두 가지 에디션

| 에디션 | 버전 | 용도 |
|---|---|---|
| **Harness** | [1.8.8](https://github.com/VibePakcr/CALF/releases/tag/docs-20261107.1) | 기존 Codex·Antigravity 훅과 독립 headless 작업. WebView 없음 |
| **Workbench** | [1.9.3](https://github.com/VibePakcr/CALF/releases/tag/docs-20261107.1) | 같은 실행 코어와 작업 기록을 사용하는 Rust + Tauri 데스크톱 앱 |

먼저 스크린샷이 포함된 **[CALF_mannual.html](https://raw.githubusercontent.com/VibePakcr/CALF/main/CALF_mannual.html)**을 내려받아 로컬에서 열어 주세요. 상단 고정 메뉴와 **EN / KR** 버튼으로 목차·본문 전체·화면 설명을 전환할 수 있습니다. 각 패키지에는 해당 버전의 오프라인 매뉴얼이 들어 있으며, 위 링크에서 최신 문구 교정본을 받을 수 있습니다. [릴리즈 노트](RELEASE-NOTES.md)와 [docs.1 SHA256SUMS](DOCS-20261107.1-SHA256SUMS)도 확인하세요.

## 다운로드

| 플랫폼 | Harness 1.8.8 | Workbench 1.9.3 |
|---|---|---|
| macOS Apple Silicon | [ZIP](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Harness-1.8.8-macos-arm64-docs.1.zip) | [ZIP](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Workbench-1.9.3-macos-arm64-docs.1.zip) |
| Windows x64 | [ZIP](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Harness-1.8.8-windows-x86_64-docs.1.zip) | [ZIP](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Workbench-1.9.3-windows-x86_64-docs.1.zip) |
| Linux x64 | [tar.gz](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Harness-1.8.8-linux-x86_64-docs.1.tar.gz) | [tar.gz](https://github.com/VibePakcr/CALF/releases/download/docs-20261107.1/CALF-Workbench-1.9.3-linux-x86_64-docs.1.tar.gz) |

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

이전 훅 형식: [CALF 1.8.4](https://github.com/VibePakcr/CALF/releases/tag/v1.8.4).

## Check Profile과 업데이트 후 작업 재개

두 에디션에 Python unittest·pytest와 제한된 Cargo 통합 테스트용 네이티브 Check Profile이 적용됩니다. 기존 실패를 기준선으로 기록하고, 테스트 실패·도구 부재·무효 근거를 구분하며, 실질적인 진전 없는 반복 시도를 중단합니다. 기존 실패도 면제하지 않습니다. 필수 검사가 해결되지 않으면 PASS가 될 수 없습니다.

Python은 프로젝트 `.venv`, `venv`, 현재 활성화한 환경, 제한된 PATH 탐색 순서로 선택합니다. 검사에 사용한 인터프리터와 설치 패키지 메타데이터를 함께 기록합니다. Python·pytest·프로젝트 의존성을 자동 설치하지 않으며, 명시된 환경이 손상되면 다른 환경으로 바꾸지 않고 오류를 알립니다. Cargo는 단일 패키지의 통합 테스트를 locked·offline으로 실행하는 범위입니다. workspace 전체·unit test·doctest 검증을 의미하지 않습니다.

새 대기열 작업은 생성 당시 런타임을 해시로 검증해 로컬 기록 폴더에 보존합니다. 업데이트 후 Resume는 그 런타임과 원래 검사·근거를 사용합니다. `runtimes`를 포함한 기록 폴더 전체를 유지하세요. 실행 버전을 입증할 수 없는 이전 작업을 임의로 이관하거나 성공 처리하지 않습니다. 고급 `calf run`의 직접 상태 경로는 원래 호환 런타임으로 실행해야 합니다.

**SDK 0.2.2**에는 `CalfClient.discover_checks()`와 `Check.from_discovered()`가 포함되어 네이티브 검사 명세를 사용자 어댑터에서 그대로 연결할 수 있습니다. [SDK 안내](SDK_README_KR.md), [프로토콜](SDK_PROTOCOL_KR.md), `examples/check_profiles.py`를 참고하세요. Python 표준 라이브러리 클라이언트와 별도 의존성이 없는 Node 클라이언트를 제공합니다. 추가 에이전트 엔진이나 상주 서비스는 없습니다.

[Update details / 업데이트 내용](UPDATE.md) · [Universal Work SDK / 범용 작업 SDK](SDK_WORK_PROTOCOL.md)

<!-- workbench-gallery:start -->
## Workbench 실제 화면

실제 Workbench 1.9.2 캡처이며 OS 제목 표시줄만 제외했습니다. [화면 맥락과 검증 범위](SHOWCASE.md).

### Task Flow · 실행과 근거

![Task Flow · execution and evidence](workbench-task-flow.png)

Workbench 1.9.2에서 보존된 실제 Codex invoice 작업을 열었습니다. 기존 실패 3건을 해결하고 등록 검사 6개를 통과한 기록입니다. 원래 실행은 Harness 1.8.6이며, 이 화면은 새 AI 실행 결과가 아니라 이전 기록을 열 수 있는지 확인한 예시입니다.

### Diff · 검사한 변경 확인

![Diff · the exact checked change](workbench-diff.png)

Before / After에서 실제 변경과 같은 파일 버전의 CHECK 영수증을 확인합니다. Light Edit와 외부 에디터 호출은 검수 결과와 구분됩니다.

### Runtime Work · 런타임을 잇는 파일 산출물

![Runtime Work · file artifacts across runtimes](workbench-runtime.png)

보존된 1.9.2 예제의 Python Adapter가 CJK 문서를 생성했습니다. 생성된 문서의 UTF-8 내용을 별도로 검사하고, 검사한 파일 목록의 해시를 채택 기록에 남겼으며, Workbench를 다시 열어 같은 채택 기록이 남아 있는지 확인했습니다.

<!-- workbench-gallery:end -->

## 무료 통합 저장소 탐색 확장팩

**Repository Navigator 0.1.0-dev.1**은 Local Git과 수동 등록한 GitHub.com·GitLab.com 저장소를 같은 화면에서 관계 지도·설명·코드·Diff를 탐색하는 별도 무료 확장팩입니다. Python 3.10 이상, Git 2.43 이상과 최신 브라우저로 실행하며 CALF core·SDK·모델은 요구하지 않습니다.

- **프리뷰 다운로드·체크섬:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/releases/tag/docs-20261107.1) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/releases/docs-20261107.1).
- **스크린샷 매뉴얼:** [한글 - 9개 장, 실화면 6장](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/README_KR.md) · [English - 9 chapters, 6 screenshots](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/README.md).
- **한글 PDF:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/ko.pdf) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/ko.pdf).
- **English PDF:** [GitHub](https://github.com/VibePakcr/CALF-Extensions/blob/main/docs/navigator-manual/en.pdf) · [GitLab](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/navigator-manual/en.pdf).

ZIP 안에 한·영 오프라인 HTML/PDF 매뉴얼이 함께 들어 있습니다. 설치 프리뷰의 실제 검증 범위는 [확장팩 검증·한계](https://gitlab.com/vibepackr-group/CALF-Extensions/-/blob/main/docs/NAVIGATOR_PACK_VERIFICATION.json)를 참고하세요.
