# CALF 네이티브 호스트 연결

[English](README.md)

하네스 1.8.15와 워크벤치 1.9.11은 Codex·Antigravity·로컬 Claude Code에서 에이전트 하나의 작업을 감독합니다. 계정·모델·명령 승인·무관한 훅은 각 호스트가 계속 관리합니다. 추가 모델·데몬·로컬 LLM은 필요하지 않습니다.

Codex와 Antigravity는 `calf install`과 기존 네이티브 훅을 사용합니다. Codex는 명령이 바뀌면 공식 `/hooks`에서 다시 검토해야 합니다. 기존 T9 등 사용자가 관리하는 보호 연결은 유지하고, 새 경로로 몰래 교체하거나 중복 연결하지 마세요.

## Claude Code

이벤트 어댑터와 버전별 설치·업데이트·복구도 Rust 코어 명령으로 옮겼습니다. 이 연결에 Python은 필요하지 않습니다. 일반 Claude 채팅·Cowork·클라우드 세션은 별도 모드입니다.

```sh
/absolute/calf install --root /absolute/native-calf --no-hooks
/absolute/calf host prepare --root /absolute/claude-kit --revision 1.8.15-hosts.1 --core /absolute/calf --config /absolute/native-calf/config.json
/absolute/calf host inspect --settings /absolute/claude/settings.json
/absolute/calf host apply --root /absolute/claude-kit --revision 1.8.15-hosts.1 --settings /absolute/claude/settings.json --expected-sha256 HASH_FROM_INSPECT
```

실제 위치의 절대 경로를 사용하고, `prepare`의 코어 경로는 현재 실행한 코어와 일치해야 합니다. 설치 후 계속 사용할 때는 `install`이 반환한 버전별 실행 파일로 후속 명령을 실행하세요. 새 연결 버전은 이전 버전 옆에 저장합니다. `apply`는 설정 원본을 그대로 백업하고 권한·MCP 항목·무관한 훅을 보존합니다. 관리 대상으로 등록되지 않은 기존 CALF 연결이 있으면 중단하므로, 그 위에 새 연결을 추가하지 말고 차이를 먼저 확인하세요. 연결을 업데이트한 뒤에는 새 호스트 세션을 시작해야 합니다.

이전 연결을 선택하려면 현재 설정 해시를 확인한 뒤 해당 버전으로 `apply`하세요. 설치 중 중단됐다면 `calf host recover --root STORE`로 조회하고, 변경 전후 상태가 확인될 때만 `--acknowledge OPERATION_ID`를 추가합니다. 복구는 설정을 다시 쓰거나 작업을 실행하지 않습니다. 원인을 확인할 수 없는 변경은 UNKNOWN으로 남깁니다.

## 실행과 근거

어댑터는 거절이나 등록 검사의 변경된 입력만 전달하고, 네이티브의 permissionDecision=allow를 호스트 승인으로 전달하지 않습니다. Claude의 승인 절차는 그대로 유지합니다. 완결된 PostToolBatch로 일치하는 일반 도구 호출을 종결할 수 있지만, 실제 실행됐다고 판단하지는 않습니다. 등록 검사는 실제 소유 프로세스의 종료 기록과 검사한 파일 버전이 일치해야 합니다. 시작하지 않은 검사는 명령을 실행하지 않고 취소할 수 있으며, 이미 시작했거나 불명확한 실행은 UNKNOWN으로 남깁니다.

합성 프로토콜 시험과 실제 AI·앱 세션은 구분합니다. 릴리즈 검증 보고서에서 시험한 OS와 범위를 확인하세요. 과거 데스크톱 세션 근거는 보존하며, 새 바이너리를 빌드했다고 이미 열린 앱이 이를 읽었다고 주장하지 않습니다.

Repository 문맥·읽기 전용 Local MCP·CPU GCN/MCL 연결은 코어의 기본 기능입니다. 현재 선택 확장은 FFmpeg만 제공합니다. 이전 연결·기록·계약·설정·과거 실행 파일도 보존합니다.
