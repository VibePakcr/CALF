# CALF 1.8.7·1.8.8 호스트 연결

[English](HOST_CONNECTIONS.md)

Codex, Antigravity, Claude Code에서 같은 CALF 네이티브 엔진을 사용할 수 있습니다. 각 호스트의 계정·모델·권한·설정은 그대로 유지합니다. 작업 하나에는 에이전트 하나를 연결하며, 추가 모델이나 상주 서비스, 로컬 LLM은 필요하지 않습니다.

## 연결 방식과 확인 범위

| 호스트 | 연결 방식 | 실제 확인한 범위 |
|---|---|---|
| Codex | CALF 네이티브 훅, `/hooks`에서 검토 | macOS 새 모델 세션, 독립 검사 8개 통과, `SATISFIED` |
| Antigravity | CALF 네이티브 훅, 기존 호환 브리지 유지 가능 | macOS 새 ACP 세션, 독립 검사 8개 통과, `SATISFIED` |
| Claude CLI·앱의 로컬 Code | Python 훅 어댑터와 선택한 1.8.7 또는 1.8.8 엔진 | macOS CLI·앱 Code, 독립 검사 8개 통과, 완료 판정과 저장된 세션 확인 |

호스트의 실제 모델 세션 검증과 Windows·Linux 네이티브 코어 검증은 별도입니다. Claude 어댑터는 POSIX 파일 잠금을 사용하며, 이번 호스트 검증 범위는 macOS입니다. 일반 Claude 채팅, Cowork, 클라우드 세션에는 별도 연결이 필요합니다.

## Codex와 Antigravity

[CALF 다운로드](https://github.com/VibePakcr/CALF/blob/main/DOWNLOADS.md)에서 제공하는 네이티브 설치기를 사용하세요. 버전별 바이너리와 설정 백업을 남기고 다른 훅을 보존합니다. 패키지의 설치 안내를 따르고, 업데이트할 때는 같은 설치 위치를 사용하세요. 기존 관리형 설치가 다른 곳에 있다면 현재 연결을 먼저 확인해야 합니다. CALF 연결을 중복으로 추가하지 마세요.

시험 설치에는 호스트 홈 경로를 명시하세요. Codex의 새 훅은 `/hooks`에서 검토해야 하며, Antigravity의 명령 승인·샌드박스 정책도 그대로 적용됩니다. 선택한 연결은 새 세션에서 확인하세요. 이미 실행 중인 세션이 새 설정을 다시 읽었다고 가정하지 않습니다.

## macOS의 Claude

로컬 키트에는 `hostkit.py`와 `claude/adapter.py`가 들어 있습니다. CALF 훅 8개만 추가하며, 허용 규칙이나 Claude 앱의 UI 설정은 수정하지 않습니다. 이 어댑터에는 네이티브 코어 외에 Python 3.10 이상이 필요합니다. [어댑터 동작과 한계](hosts/claude/README_KR.md).

네이티브 설치 위치, 별도의 키트 상태 폴더, Python 실행 파일, Claude가 사용하는 기존 settings JSON을 실제 절대 경로로 지정하세요. 설정 경로가 심볼릭 링크라면 실제 대상 파일을 선택해야 합니다. 도구는 링크를 교체하지 않습니다. 백업에는 개인 설정이 들어갈 수 있으므로 상태 폴더를 비공개로 보관하고 공유 저장소에 넣지 마세요.

먼저 훅을 바꾸지 않고 네이티브 엔진을 설치합니다.

```sh
/path/to/calf install --root /path/to/native-calf --no-hooks
```

출력에 나온 버전별 실행 파일과 `config.json` 경로를 다음 명령에 넣습니다.

```sh
python3 -B hostkit.py prepare --root /path/to/claude-calf --revision 1.8.8-hosts.1 --core /path/to/native-calf/versions/VERSION/calf --config /path/to/native-calf/config.json --python /physical/path/to/python3
python3 -B hostkit.py inspect --settings /physical/path/to/claude/settings.json
python3 -B hostkit.py apply --root /path/to/claude-calf --revision 1.8.8-hosts.1 --settings /physical/path/to/claude/settings.json --expected-sha256 INSPECT에_나온_해시
```

settings JSON은 기존 파일이어야 합니다. 새 프로필이라면 Claude를 한 번 실행하거나, Claude가 사용하는 위치에 `{}` 파일을 먼저 만드세요. `prepare`는 선택한 키트 상태 폴더 안에 새 버전만 만듭니다. `apply`는 지정한 해시를 확인하고 원래 설정 바이트를 보존한 뒤 CALF 훅을 합칩니다. 다른 훅, 권한·MCP 설정은 JSON 안에 유지됩니다. Claude에서 훅을 검토하고 새 로컬 Code 세션을 시작하세요.

이미 작동하는 CALF 훅 연결을 이 키트로 다시 설치할 필요는 없습니다. 키트가 관리하지 않는 훅 명령에 `CALF`가 들어 있으면 중복 연결을 추가하지 않고 중단합니다. 기존 연결은 그대로 유지할 수 있으며, 이관하려면 현재 연결을 먼저 명시적으로 검토해야 합니다.

## 업데이트와 복구

새 키트 버전을 나란히 준비하고 현재 설정 해시를 확인한 뒤 적용하세요. 이전 버전을 다시 선택할 때도 같은 `apply` 명령에 보존된 revision을 지정합니다. 이후 추가한 다른 설정·훅은 유지합니다. 관리 중인 CALF 훅이 수정되거나 사라졌다면 덮어쓰지 않고 중단합니다.

적용 중 종료됐다면 다음 명령으로 확인합니다.

```sh
python3 -B hostkit.py recover --root /path/to/claude-calf
python3 -B hostkit.py recover --root /path/to/claude-calf --acknowledge 작업_ID
```

복구는 현재 설정을 보존된 적용 전·후 해시와 비교해, 일치가 확인된 경우에만 키트의 설치 기록을 정리합니다. 설정 쓰기, 작업 실행, 과거 기록 복원, 모델 변경은 하지 않습니다. 어느 쪽과도 일치하지 않으면 `UNKNOWN`으로 남깁니다. 실패 기록과 원본 백업도 보존합니다.

## 실제 작업 확인

설치한 코어에 작업 계약을 명시적으로 등록합니다.

```sh
/path/to/calf register /path/to/work /path/to/contract.json --config /path/to/native-calf/config.json
```

등록 결과에 나온 검사 명령을 해당 작업 폴더에서 호스트의 일반 승인 절차를 거쳐 실행하세요. Claude Auto 모드에서도 처음 실행하는 로컬 명령은 승인이 필요할 수 있습니다. 영구 저장할 의도가 없다면 ‘항상 허용’을 선택하지 마세요. 실제 검사 영수증과 파일 버전 일치가 완료 근거이며, 호스트의 설명이나 종료 코드만으로 완료를 판단하지 않습니다. 작업의 `history.html`과 `SATISFIED`, `VIOLATED`, `UNKNOWN` 판정을 확인하세요.

위 호스트 동작은 1.8.7에서 확인한 macOS 실제 모델 세션의 검증 근거를 재사용합니다. 키트 설치 시험은 별도 설정에서 합치기, 업데이트·이전 버전 선택, 적용 중단 복구, 실제 로컬 훅 호출을 확인합니다. 추가 모델 호출이나 다른 OS의 호스트 지원을 주장하지 않습니다.

## 로컬 확장팩

별도 Local Pack Tools와 Repository inspect 프리뷰는 macOS·Windows·Linux에서 검증했습니다. 호스트 훅 경로나 네이티브 엔진은 변경하지 않습니다. [팩 릴리즈와 영·한 안내](https://github.com/VibePakcr/CALF-Extensions/releases/tag/packs-v0.1.0-preview.1)를 참고하세요. Claude 호스트 설치 검증은 macOS에 한정됩니다.
