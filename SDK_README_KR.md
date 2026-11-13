# CALF SDK 0.2.11

공유 Rust 코어를 연결하는 가벼운 통합 도구입니다. 이번 버전에는 필요한 공학 지식만 조회하는 Python·Node·Rust 예제를 추가했습니다. 인덱싱·출처 해시·조회 제한·완료 검사는 코어에서 처리하며, SDK가 별도 모델·상주 서비스·데이터베이스를 요구하지 않습니다.

[공학 지식 안내](sdk/docs/ENGINEERING_KNOWLEDGE_KR.md) · [Python](sdk/examples/engineering_knowledge.py) · [Node](sdk/examples/engineering_knowledge.mjs) · [Rust](sdk/examples/engineering_knowledge.rs) · [로컬 모델 미리보기](sdk/docs/LOCAL_MODELS_KR.md)

공학 지식 API는 하네스 **1.8.18** 또는 워크벤치 **1.9.15** 이상이 필요합니다. 선택형 로컬 모델 연결은 미리보기입니다. Qwen7B 시험은 기존 자원 가드가 중단했으므로 작업 완료까지 지원 검증을 마쳤다는 뜻은 아닙니다. 비공개 검증 자료는 포함하지 않습니다.

SDK 0.2.10에서 도입한 작업 요약과 로컬 요청 초안 API도 유지합니다. 조회·내보내기는 실행 권한이나 현재 완료 판정을 부여하지 않으며 자동 업로드도 하지 않습니다.

SDK 0.2.9에 `artifacts()`를 추가했습니다. 하네스 1.8.16 / 워크벤치 1.9.12에서 기록된 파일을 조회하고, 새로 만드는 작은 임시 텍스트에 생성 근거·참조·보존 기한을 붙일 수 있습니다. 조건을 충족한 파일은 확인 후 격리·복원하며, 기존 소스·테스트·후보·복구 근거는 계속 보호합니다. [사용 안내](sdk/docs/ARTIFACT_LIFECYCLE_KR.md), [Python 예제](sdk/examples/managed_artifact.py), [Node 읽기 전용 예제](sdk/examples/artifacts.mjs)를 참고하세요. 상주 탐색기나 자동 삭제는 추가하지 않습니다.

Universal Work v1은 작업 계약을 고정하고 검사한 파일 버전과 결과를 함께 확인하는 범용 작업 규약입니다. 범용 어댑터, 별도 런타임 라이브러리가 필요 없는 Python·Node 클라이언트, 제어 기능을 선택적으로 켤 수 있는 MCP를 제공합니다. [규약과 실행 예제](sdk/docs/WORK_PROTOCOL_KR.md)를 참고하세요. Workbench 1.9.2의 **Runtime Work**에서 같은 작업을 조회·제어할 수 있으며 기존 코드 작업 API도 유지됩니다.


[English](README.md) · [프로토콜 규격](sdk/docs/PROTOCOL_KR.md) · [확장 라이선스](LICENSE-SDK.txt)

**CALF Harness 1.8.7–1.8.18** 및 **CALF Workbench 1.9.2–1.9.15**에 포함된 네이티브 코어를 연결하는 작은 SDK입니다. Python 3.10 이상과 표준 라이브러리로 동작합니다. 상주 서비스·모델 런타임·데이터베이스·네트워크 의존성을 추가하지 않으며, 비공개 코어 소스는 포함하지 않습니다.

OS별 실행 파일·SDK·MCP 검증 결과는 압축 파일의 `VERIFICATION.json`에 있습니다. 합성 작업과 실제 로컬 프로세스로 검사하며 AI 실서비스 호출이나 모든 배포판 지원을 주장하지 않습니다.

[SDK 0.2.11 다운로드](https://github.com/VibePakcr/CALF/releases/tag/sdk-v0.2.11). 하나의 공용 소스 압축 파일에 SDK·영문/한글 안내·영문/한글 프로토콜·예제·검사 실행기가 포함됩니다. 해당 OS의 CALF 네이티브 릴리즈는 별도로 설치합니다. SDK 압축 파일에 코어 런타임은 포함하지 않습니다.

## 시작하기

압축을 풀고 SDK 루트에서 Python을 실행하거나 해당 폴더를 import 경로에 추가합니다. 설치된 네이티브 `calf` 또는 `calf.exe`와 **기존 CALF와 같은 기록 폴더**를 명시합니다. SDK는 경로를 추측하거나 기존 기록을 이동하지 않습니다. 평소 CALF 실행 환경에서 `calf task home`으로 기록 경로를 확인할 수 있습니다. 처음 시험할 때는 새로운 절대 경로를 사용하세요.

```python
from pathlib import Path
from calf_sdk import CalfClient, is_satisfied

client = CalfClient(Path("/절대경로/calf"), Path("/절대경로/CALF/workbench"))
print(client.version())
for job in client.tasks()["jobs"]:
    current = client.inspect(job["task"])
    print(job["task"], current["state"], is_satisfied(current))
```

Windows는 `Path(r"C:\Tools\CALF\calf.exe")` 같은 절대 경로를 사용합니다. GUI 실행기나 `.app` 폴더 대신 내부 네이티브 코어를 선택합니다. 제공자·검사 명령의 실행 파일은 `Path(sys.executable).resolve()`처럼 실제 경로를 사용해야 합니다.

setuptools가 설치된 개발 환경에서는 `python -m pip install --no-build-isolation .`로 로컬 설치할 수도 있습니다. 외부 런타임 라이브러리는 필요하지 않습니다. PyPI에는 게시하지 않았습니다.

## 작업 등록과 제어

AI 연결은 먼저 CALF에서 설정합니다. 간편 큐는 지원되는 Python `unittest`·설정된 `pytest`·제한된 Cargo 통합 테스트 검사 명세를 찾습니다. 지원하는 검사가 없는 폴더는 등록을 거절합니다.

```python
job = client.submit(Path("/절대경로/project"), "청구서 반올림 오류를 수정하세요")
task = job["task"]
client.control(task, "pause")
client.control(task, "resume")
```

등록은 큐에 넣는 동작이며 AI 프로세스를 자동 시작하지 않습니다. Workbench의 기존 워커를 이용하거나 다음과 같이 포그라운드 워커를 명시적으로 실행합니다.

```python
import subprocess
subprocess.run(client.worker_argv(), check=True)
print(is_satisfied(client.inspect(task)))
```

호출자가 포그라운드 프로세스를 관리하며 CALF의 중단·취소 처리가 끝나도록 기다려야 합니다. 워커 종료 코드 0은 작업 성공을 뜻하지 않습니다. `cancel` 응답은 취소 요청 접수이며 완료 영수증이 아닙니다. 취소한 작업은 재개할 수 없습니다. `recheck`도 기존 예산과 Guard를 따릅니다.

`tasks()`는 최근 32개 작업을 반환합니다. `changes(task, mode="task")`는 읽기 전용 변경 조회이며 모드는 `task`, `attempt`, `recovery`입니다. `path`로 파일 하나, `attempt`로 시도를 지정합니다. 과거 텍스트가 없으면 그대로 미확인으로 남습니다. Working Tree Git diff는 별도의 Workbench 기능입니다.

`reuse(task)`의 레시피를 `submit(..., reuse=recipe)`에 넘기면 새 작업을 만듭니다. 레시피는 성공 증거가 아니며 digest가 일치해야 합니다. `preferences(text)`는 CALF를 통해 작업 성향을 추가 기록합니다. 빈 문자열은 해당 성향의 현재 값을 비우고, 인수 없이 호출하면 현재 값을 조회합니다.

## Local Sources와 MCP

```python
root = "/절대경로/참고자료"
registry = client.sources("add", root=root)
source = next(s for s in registry["sources"] if s["root"] == root)
listing = client.sources("browse", source=source["id"])
uri = listing["resources"][0]["uri"]
preview = client.sources("read", source=source["id"], uri=uri)
reference = client.reference(source["id"], preview)
job = client.submit(Path("/절대경로/project"), "첨부 요구사항을 반영하세요",
                    attachments=[reference])
```

폴더 추가·조회·미리보기만으로 AI에게 전송하지 않습니다. 위 예제에서는 `submit`을 호출할 때 선택한 참조를 첨부합니다. 미리보기 이후 파일이 바뀌면 기존 참조로 등록할 수 없습니다. 참조 최대 4개, 직렬화된 문맥 총 8KiB 제한이 적용됩니다. 네이티브 어댑터는 숨김·자격증명 관련 경로와 링크를 제외합니다. 이는 문맥 전송 통제이며 외부 AI 프로세스의 기존 파일 접근 권한을 제한하는 샌드박스는 아닙니다.

`client.mcp_server(Path("/절대경로/참고자료"))`는 MCP 클라이언트가 서버를 실행할 때 사용할 `command`와 `args`를 반환합니다. 이 호출 자체는 서버를 시작하지 않습니다. 서버는 읽기 전용이며 초기화·`resources/list`·`resources/read`를 지원합니다. 임의 MCP 도구를 실행하는 플러그인 호스트가 아닙니다. 사용 후 stdin을 닫고 프로세스 종료를 확인합니다.

## 제공자·검사 어댑터

`Check`·`ProviderConfig`는 기존 네이티브 JSON 설정을 만듭니다. `read_request`·`plan`·`action`·`review`·`emit`으로 제공자 프로토콜을 구현할 수 있습니다. 제공자는 변경안을 반환하고 네이티브 코어가 동일성·보호 파일·검사·증거를 판정합니다. 최종 완료 여부는 실제 검사 결과로 확인합니다.

```python
import sys
from calf_sdk import Check, ProviderConfig

python = str(Path(sys.executable).resolve())
config = ProviderConfig(
    command=[python, "/절대경로/my_adapter.py"],
    checks=[Check("unit", [python, "-m", "unittest"], ["test_invoice.py"])],
    max_attempts=4,
)
config.write_new("/절대경로/new-provider.json")
```

검사 명령은 빈 검사·전체 건너뛰기·불완전한 검증을 계약에 맞춰 실패로 처리해야 합니다. 종료 코드만으로는 필요한 검사가 실제로 수행됐는지 알 수 없습니다. `write_new`는 기존 설정을 덮어쓰지 않습니다.

사용자 정의 어댑터는 `calf run WORKSPACE REQUEST PROVIDER.json STATE`로 실행하고 `calf run-status WORKSPACE STATE TASK`로 조회합니다. 이 명시적 상태 경로는 Workbench 큐와 별개이며 **Workbench 작업 목록으로 자동 가져오지 않습니다.** 공유 목록이 필요한 작업은 `client.submit`을 사용합니다.

제공자 명령의 마지막 인수에 요청 JSON 파일 경로가 붙습니다. stdout에는 JSON 객체 하나, 진단은 stderr로 출력합니다. `examples/provider_demo.py`는 한 번 실패하고 수정·검토하는 합성 예제이며 실제 AI를 호출하지 않습니다. 제공자 프로세스에서도 SDK를 import할 수 있어야 합니다.

## 실패 처리와 범위

- `CalfError`: 네이티브 명령이 실패했습니다. `error.response`에 구조화된 응답이 있습니다.
- `CalfTransportError`: 시간 초과·출력 한도·실행·파싱 문제입니다. 변경이 이미 일어났을 수 있으므로 **조회한 뒤 재시도 여부를 판단합니다. 자동 재시도하지 않습니다.**
- `is_satisfied`는 전달된 응답의 명시적 `SATISFIED`만 인식합니다. 임의 데이터의 진위나 서명을 검증하지 않으며 저장된 응답을 최신화하지 않습니다. 신뢰하는 바이너리에서 새 `inspect`·`run-status` 응답을 받아 사용합니다.
- API 입력은 64KiB, 기본 응답 한도는 8MiB, 기본 응답 제한 시간은 30초입니다. 출력은 임시 파일에 모으고 한도를 확인한 뒤 메모리로 읽습니다. 폴링 사이에 디스크 출력이 일시적으로 한도를 초과할 수 있습니다. 호출 간 캐시는 없습니다.
- 조회 중에도 CALF 자체 폴더 생성·색인 재구성이 일어날 수 있습니다. SDK는 저널·계약·설정을 직접 다시 쓰지 않습니다.
- 제공자와 검사 프로그램은 호스트 권한을 유지합니다. 신뢰하는 어댑터만 실행하세요. SDK는 실행 승인·보안 정책을 변경하지 않고 모델 설치나 인증정보 관리를 하지 않습니다.

## 검증 실행

SDK 루트에서 `python -m unittest discover -s tests -v`를 실행합니다. 실제 바이너리 연결 시험은 다음과 같습니다.

```text
python ops/verify.py --harness /절대경로/calf-1.8.11 --workbench /절대경로/calf-1.9.6 --output /절대경로/새-시험-폴더
```

새 상태와 합성 제공자, 실제 Python 검사로 실패→수정→검수, 외부 변경 이후 증거 무효화, 공유 기록, 작업 제어, CJK, MCP 종료와 오래된 참조 거절을 확인합니다. 실제 AI 호출·기존 CALF 홈 접근·메모리 벤치마크는 하지 않습니다. 출력 폴더는 없어야 하며 실패 보고서도 보존합니다.

## Check Profile과 업데이트 (0.2.2)

검사 탐색에는 최소 Harness 1.8.7 또는 Workbench 1.9.2가 필요합니다. 기존 0.1 API도 유지합니다.

```python
from calf_sdk import Check, ProviderConfig
checks = [Check.from_discovered(c) for c in client.discover_checks(project)]
config = ProviderConfig(command=[python, adapter_path], checks=checks)
```

`discover_checks`는 설치된 도구의 메타데이터를 확인하며 검사 실행·의존성 설치·작업 등록을 하지 않습니다. Python은 `.venv`, `venv`, 활성 환경, PATH 순서로 선택하며 명시된 환경이 불완전하면 다른 환경으로 바꾸지 않고 오류를 알립니다. Python v2는 인터프리터·환경 설정·패키지 메타데이터를 결속하지만 설치된 모든 패키지 파일의 해시를 보장하지 않습니다. Cargo는 잠금 파일이 있는 단일 패키지의 통합 검사를 지원합니다.

코어가 작업 전 실패를 기록하고 기존·새로운·해결된 실패를 구분합니다. 실패한 검사에서 파일과 결과가 계속 같으면 무효 재시도를 멈춥니다. 검사가 없거나 전부 건너뛰었거나 결과가 불완전하면 완료로 판정하지 않습니다. `no_progress`, `UNKNOWN`, 요청 접수 응답을 성공으로 해석하지 마세요.

새 큐 작업은 기록 폴더에 버전별 실행 파일 한 개를 공유 보관합니다. 업데이트할 때 전체 기록 폴더를 유지하고, `control(task, "resume")` 후 워커를 실행하면 원래 런타임과 남은 시도 횟수로 이어집니다. 런타임이 없거나 변조되면 거부하며 기존 계약을 고쳐 통과시키지 않습니다. 고급 `calf run` 경로는 명시적으로 고정한 바이너리·설정·상태를 사용하며 큐로 자동 이관되지 않습니다.


### JavaScript / TypeScript

CALF 1.8.7 / 1.9.2는 Node 24 이상 내장 node:test 프로파일을 지원합니다. `Check.from_discovered()`가 v3와 실행 명령을 그대로 유지합니다. `examples/check_profiles.py`를 참고하세요. npm 스크립트·Jest·Vitest·TypeScript 타입 검사는 이 프로파일 범위 밖입니다.


## 저장 결과와 현재 상태 조회

하네스 1.8.10 / Workbench 1.9.5에서 `client.registered_tasks(workspace)`로 등록 작업을 찾고 `client.registered_status(workspace, task)`로 현재 판정과 `statusView` 진단 정보를 읽습니다. `is_satisfied(response)`는 최상위 현재 판정만 확인합니다. 저장된 과거 `SATISFIED`를 완료 근거로 사용하지 않습니다. 검사·AI 실행이나 환경 변수 변경은 하지 않습니다. [예제](sdk/examples/status_context.py) · [상세 안내](sdk/docs/STATUS_CONTEXT_KR.md).

## Claude 연결 키트 (0.2.4)

호스트 훅 처리와 연결 설정을 Rust 코어로 통합했습니다. Claude 이벤트 9개, 배치 결과 연결, 등록 검사 영수증, 버전별 설치를 macOS·Windows·Linux의 합성 작업으로 검증했습니다. Windows·Linux의 실제 Claude 앱 새 세션 검증을 뜻하지는 않습니다. Python·Node는 선택적으로 쓰는 얇은 SDK 클라이언트로 남깁니다. [호스트 설정](hosts/README_KR.md) · [Claude 승인·상태](hosts/claude/README_KR.md).

## MCP 도구 정책 연결 (0.2.7)

새 MCP 경로에는 하네스 **1.8.12** 또는 Workbench **1.9.8**이 필요합니다. Python의 `tool_contract`는 계약을 정규화하고, `tool_status`는 현재 네이티브 완료 판정을 읽습니다. `prepare_tool`은 검토할 실행안만 만듭니다. 도구를 실행하거나 승인하지 않습니다. 반환된 `argv`는 내용을 검토한 뒤 기존 호스트 승인 절차로 실행하세요. 티켓이 사용자 승인 버튼 클릭을 증명하지는 않습니다.

```python
prepared = client.prepare_tool(policy_path, exact_policy_sha256, request)
assert prepared["state"] == "REQUIRE_APPROVAL"
assert prepared["authorityGranted"] is False
print(prepared["review"])
print(prepared["argv"])
```

Python의 `tool_mcp_server`와 Node의 `toolMcpServer`는 같은 포그라운드 stdio 연결 명세를 반환합니다. 기본 도구는 상태 조회뿐이며 `control=True` 또는 `{control:true}`를 명시하면 읽기 호출과 실행안 준비 도구를 추가합니다. 연결 정보를 반환할 뿐 호스트 설정을 수정하거나 프로세스를 상주시켜 두지 않습니다. 실행 예제는 `examples/mcp_policy.py`를 참고하세요.

지원 범위는 검토한 로컬 읽기, 새 후보 생성, 원래 정책에 미리 설정한 로컬 복구입니다. 불명확한 호출을 자동으로 다시 보내지 않습니다. 삭제·덮어쓰기·외부 전송·원격 작업 복구는 이 규약의 검증 범위에 포함되지 않습니다. 기존 호스트 권한과 완료 기준은 그대로 적용됩니다.

## 네이티브 Repository 문맥

하네스 1.8.15 / 워크벤치 1.9.11부터 사용할 수 있습니다. `client.repository_context(workspace, task="청구서", registry=registry)`는 Rust 코어에서 필요한 로컬 기록만 조회합니다. `client.repository_mcp_server(registry, workspace)`는 읽기 전용 MCP 연결 설정을 반환하며, Node에서는 `repositoryMcpServer`를 사용합니다. 조회한다고 AI에게 자료를 보내거나 완료를 판정하지 않습니다. SDK는 언어별 연결층이며 별도 실행 엔진이 아닙니다.

기존 Ollama·MLX 서버 연결은 선택형 미리보기입니다. [연결 방법과 검증 범위](sdk/docs/LOCAL_MODELS_KR.md)를 확인하세요. 모델 목록 연결과 실제 작업 완료는 구분합니다.
