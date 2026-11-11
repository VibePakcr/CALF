# CALF에 통합된 Repository Intelligence

[English](REPOSITORY_BUILTIN.md)

Repository Intelligence를 CALF의 공통 Rust 코어에 통합했습니다. 하네스와 워크벤치가 같은 모듈 인덱스, 원문 기록 조회와 GCN/MCL 검사를 사용합니다. Repository 확장을 따로 설치할 필요가 없으며, 이 실행 경로는 Python·Node·로컬 모델·백그라운드 인덱서 없이 동작합니다. 별도 선택 확장으로는 FFmpeg만 남습니다.

## 프로젝트 하나부터 연결하기

워크벤치에서 작업 폴더를 선택한 뒤 **Repository context → Connect records…**를 엽니다. 해당 프로젝트의 CALF `history.html`이 있는 폴더를 선택하세요. CALF는 기존 네이티브 기록을 검증하고, 프로젝트 밖에 연결 정보와 조회용 모듈 지도를 새로 만듭니다. 이미 등록된 연결을 덮어쓰지 않습니다. 모듈 목록을 새로고침하고 하나를 선택해 **Read module**로 읽으세요. 검색은 선택한 모듈의 제한된 메타데이터만 조회하며, 결과를 선택하면 정확한 원문 기록을 읽습니다.

기존 모듈 지도와 레인 계획이 있으면 하네스에서 직접 등록할 수 있습니다.

```sh
calf context --home /absolute/registry bind --project /absolute/project --history /absolute/records/history.html --modules /absolute/modules.json --cache /absolute/cache
calf context --home /absolute/registry read --cwd /absolute/project --task "청구서 작업 이어가기"
calf context --home /absolute/registry search --cwd /absolute/project --module billing --query rounding
calf context --home /absolute/registry record --cwd /absolute/project --module billing --seq 42
```

캐시는 프로젝트와 원본 기록 폴더 밖에 두어야 합니다. 기존 레인 계획이 있다면 등록할 때 `--lanes /absolute/lanes.json`을 추가하고 `resume`, `lane`, `gate`로 조회하세요. 미등록 프로젝트는 `UNBOUND`, 모듈을 특정하기 어려운 요청은 작은 `SELECT_MODULE` 목록을 반환합니다. 홈 폴더나 다른 프로젝트를 찾아다니지 않습니다.

## 완료를 판단하는 근거

원본 `history.html`, 기록 ID·순번·해시 체인, 계약과 네이티브 검사가 판단의 기준입니다. Markdown은 조회용으로 만든 참고 자료입니다. 캐시가 준비된 뒤에는 선택한 모듈만 읽고 원본을 몇 바이트 읽었는지도 표시합니다. 오래된 결정은 메타데이터로 찾은 뒤 정확한 위치와 해시로 확인합니다. 원본이 바뀌면 기존 캐시는 무효가 됩니다. 과거의 PASS나 레인의 `READY`는 실행 허가나 현재 완료의 근거가 아닙니다. 현재 판정은 네이티브 `status`로 확인하며, `UNKNOWN`과 `WAIT`는 미완료로 유지합니다.

워크벤치에서 기록을 연다고 AI에게 자동으로 보내지는 않습니다. 기록은 일반 텍스트로 표시하며, 지시가 아닌 참고 자료로 취급합니다.

## SDK와 Local MCP

Python SDK는 Rust 코어를 호출하는 얇은 연결층입니다.

```python
context = client.repository_context(workspace, task="청구서 작업 이어가기", registry=registry)
server = client.repository_mcp_server(registry, workspace)
```

Node에서는 `client.repositoryMcpServer(registry, workspace)`를 사용합니다. 직접 실행하는 명령은 `calf repository-mcp REGISTRY PROJECT`입니다. 연결 중에만 실행되는 읽기 전용 MCP로, 등록된 프로젝트 범위의 조회만 제공합니다. 프로젝트 등록·작업 실행·결과 채택·정책 변경은 할 수 없습니다.

## 관련 파일 분석의 범위

관련 파일 화면은 Rust로 Python의 import·심볼·호출 후보를 추출합니다. 조회당 최대 64개 파일·1 MiB·3초로 제한하며, 주석과 문자열 본문은 제외합니다. Python 문법 전체의 검증, 의미 분석이나 필수 테스트 자동 선택을 제공하는 것은 아닙니다. 응답에 `syntaxValidation: NOT_PERFORMED`를 명시하며, 실제 프로젝트 검사는 해당 언어의 실행 환경을 사용합니다. 이전 Python AST 캐시는 보존하되 Rust 분석 결과로 재사용하지 않습니다.

## 업데이트와 복구

새 CALF는 이전 버전과 나란히 설치하세요. 기존 프로젝트 연결·별칭·모듈 지도·레인 계획을 그대로 읽고, Rust 조회 캐시는 새 식별자로 만듭니다. 이전 확장 파일과 저장소는 추적·복구용으로 남기며 현재 확장 목록에서는 제외합니다. 조회 과정에서 원본 기록·계약·설정을 다시 쓰지 않습니다. 코어를 바꿨다는 이유로 과거 작업의 실행 파일이나 씬 버전을 삭제하지 마세요.

## 로컬 Git 관측 기록

워크벤치의 **Capture local Git**은 제한된 파일 지도와 HEAD·인덱스·작업 파일의 원본 바이트를 저장합니다. Git status·작업 파일 diff·필터·훅·fetch를 실행하지 않습니다. 설치된 Git 2.43 이상을 사용하며 Python 리더나 뷰어 서버는 필요하지 않습니다. 저장 위치는 조사하는 저장소 밖이어야 합니다. 링크·자격증명 이름·생성 경로는 제외하고, 범위를 다 확인하지 못하면 PARTIAL로 표시합니다.

```sh
calf repository capture --project /absolute/repository --data /absolute/captures
calf repository inspect --data /absolute/captures --capture CAPTURE_SHA
calf repository source --data /absolute/captures --capture CAPTURE_SHA --path pkg/invoice.py --version working
calf repository export --data /absolute/captures --capture CAPTURE_SHA --output /absolute/new-export
```

저장된 소스를 읽을 때 `head`, `index`, `working` 중 버전을 명시합니다. 나중에 파일을 수정해도 저장된 바이트는 바뀌지 않습니다. 관측 기록·소스·관계 지도의 해시는 조회할 때 확인합니다. 오프라인 내보내기는 기본적으로 원래 저장 경로와 소스 본문을 제외합니다. 코드를 복사하려는 경우에만 `--include-source`를 추가하세요. 저장된 관측이나 정적 관계 지도는 현재 앱 검사의 통과 근거가 아닙니다. 외부 저장소 탐색과 별도 Navigator 화면은 통합하지 않습니다.
