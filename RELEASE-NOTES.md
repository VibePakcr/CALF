# CALF Harness 1.8.12 · Workbench 1.9.8 · SDK 0.2.5

## Governed local MCP tools

- Added exact policy/task/tool binding, read mediation and host-admitted creation of new candidates. `tool-prepare` and `calf_tool_prepare` return a reviewable command without running or approving the tool.
- Bound validated candidates to native `mcpArtifact` evidence. Independent registered checks run after a verified write; a tool success response or exit zero cannot establish completion. Older cores reject the required extension rather than ignore it.
- Added opt-in local recovery from an original stopped execution receipt, exact candidate hashes and fresh checks. Recovery never resubmits the original tool call or rewrites the first result. Expired/replayed/tampered intents, unknown cleanup and explicit cancellation remain blocked.
- Propagated native cancellation through response waiting and independent checks. Added Python SDK preparation/status helpers and matching Python/Node foreground MCP descriptors, with no new runtime dependency.
- Retained the foldable first-task guide, request outline, English/Korean manual and existing host workflow. Updated the host kit's qualified core list.

macOS ARM64, Windows x64 and Linux x64 (Debian 13) each passed 11 read groups and 14 execution/recovery groups for both editions. SDK boundary tests and actual local integration are separately recorded in [VERIFICATION.json](VERIFICATION.json). Tests use real local processes and synthetic work, not a new AI-service benchmark. The earlier 66-test native suite is reused against unchanged runtime source; version metadata differs.

The profile covers reviewed local stdio reads, absent candidate creation and preconfigured local artifact recovery. It does not qualify arbitrary destructive/external calls, remote job reconciliation, all OS variants or independent human-consent signatures. Existing GCN/MCL and native TASK/ACTION history remain the integration boundary; missing named GCI/ETS interfaces are not invented. No new model, daemon, agent pool, GPU control, global MCP registration or permanent allow rule is added.

## 한국어

- 정책·작업·도구·파일 버전을 묶는 로컬 MCP 경로를 추가했습니다. `tool-prepare`와 `calf_tool_prepare`는 검토할 명령을 준비하며 요청한 도구를 실행하거나 승인하지 않습니다.
- 새 후보의 검증 결과를 네이티브 `mcpArtifact` 근거에 연결했습니다. 정상 쓰기 뒤 등록된 독립 검사를 자동 실행합니다. 도구의 성공 응답이나 종료 코드 0만으로는 완료하지 않습니다. 이 계약을 모르는 구버전 코어는 기록을 무시하지 않고 거부합니다.
- 원래 정책에 미리 설정한 로컬 복구를 지원합니다. 기존 종료 영수증·후보 해시·새 검사를 대조하고, 최초 호출을 다시 보내거나 이전 결과를 고쳐 쓰지 않습니다. 만료·중복·변조된 실행안, 불명확한 종료와 명시적 취소는 통과시키지 않습니다.
- 응답 대기와 독립 검사에도 네이티브 취소 신호를 전달합니다. Python SDK의 준비·상태 API와 Python·Node의 포그라운드 MCP 연결 명세를 추가했습니다. 새 런타임 라이브러리는 필요하지 않습니다.
- 접고 펼칠 수 있는 첫 작업 안내·요청 초안·영한 매뉴얼과 기존 호스트 흐름을 유지했습니다. 연결 키트의 검증된 코어 버전 목록도 맞췄습니다.

macOS ARM64·Windows x64·Linux x64(Debian 13)에서 두 제품 각각 읽기 11개·실행 및 복구 14개 그룹을 통과했습니다. SDK 경계 검사와 실제 로컬 연동 결과는 [VERIFICATION.json](VERIFICATION.json)에 구분합니다. 실제 로컬 프로세스와 합성 작업을 사용했으며 새 AI 실서비스 시험은 아닙니다. 네이티브 66개 검사는 런타임 소스가 동일한 이전 결과를 재사용하고 버전 메타데이터 변경을 별도로 확인했습니다.

지원 범위는 검토한 로컬 stdio 읽기, 새 후보 생성과 미리 설정한 로컬 파일 복구입니다. 임의 삭제·외부 전송·원격 작업 복구·모든 OS 변형이나 독립적인 사용자 동의 서명까지 검증한 것은 아닙니다. 기존 GCN/MCL과 네이티브 TASK/ACTION 기록을 재사용하며 확인되지 않은 GCI/ETS 인터페이스를 만들어 넣지 않습니다. 모델·상주 서비스·에이전트 풀·GPU 제어·전역 MCP 등록·영구 허용 규칙은 추가하지 않습니다.

[Downloads / 다운로드](DOWNLOADS.md) · [MCP](MCP_TOOL_EVALUATION.md) · [한국어 MCP](MCP_TOOL_EVALUATION_KR.md) · [SDK](SDK_README.md)
