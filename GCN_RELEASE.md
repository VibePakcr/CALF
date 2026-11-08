# CALF GCN/MCL core preview

Harness **1.8.9** and Workbench **1.9.4** share the native CPU implementation of GCN cells and MCL lanes. The Repository pack supplies module references; the Rust core handles dependencies, write-owner conflicts and current native check evidence. One agent remains the executor.

- macOS ARM64, Windows x64 and Debian x64 passed actual checks, file-change invalidation, wrong-scope refusal, both API envelope forms and the Workbench native bridge.
- Repository preview.5 passed 41 contracts per OS. Fresh Codex and Antigravity context sessions passed. Claude recovered the same exact references in one call; its strict report-format failure and separate functional review are retained.
- The existing Python SDK 0.2.2 generic call supports the new endpoint. Existing hooks and their 1.8.8 runtimes remain pinned.
- The 938 original history prefixes are preserved. Documented host configuration/state changes are listed in the guide and report; whole-app-state byte identity is not claimed. Settings were not restored or baselines advanced.

Extract into a new folder and keep the complete existing records home, contracts, settings and runtimes. This is a feature preview, with native bridge self-checks rather than a new GUI interaction or memory benchmark. The core remains free to use and closed-source.

[English guide](GCN_CORE.md) · [한국어 안내](GCN_CORE_KR.md) · [Verification](GCN-VERIFICATION.json)

## 한국어

하네스 **1.8.9**와 워크벤치 **1.9.4**의 공통 Rust 코어에 CPU 기반 GCN 셀·MCL 레인을 넣었습니다. Repository 팩은 필요한 모듈의 참고 기록을 제공하고, 코어는 의존 순서·수정 소유권 충돌·현재 네이티브 검사 증거를 확인합니다. 실행자는 에이전트 하나로 유지합니다.

세 OS에서 실제 검사와 파일 변경 후 무효화, 다른 범위의 통과 증거 거절, 두 API 요청 형식과 워크벤치 브리지를 확인했습니다. Repository 팩 검사는 OS별 41개입니다. Codex·Antigravity 새 세션은 통과했고, Claude도 원본을 정확히 찾았습니다. Claude의 보고 형식 실패와 별도의 기능 확인은 함께 보존했습니다.

기존 SDK 0.2.2의 Python 범용 호출을 사용하며 1.8.8 감독 훅과 이전 실행기는 유지합니다. 기존 이력 938개의 접두 기록도 보존했습니다. 호스트 설정·앱 상태의 관측된 변경과 한계는 안내·보고서에 명시했으며 원본 설정 복원이나 검사 기준 갱신은 하지 않았습니다.

새 폴더에 압축을 풀고 기존 기록 전체·계약·설정·실행기를 보관하세요. 이번 검증은 네이티브 브리지 자체 점검을 포함한 기능 프리뷰입니다. 새 GUI 조작·메모리·장시간 시험은 포함하지 않습니다. 코어는 무료 사용·비공개 소스 배포 방식을 유지합니다.

## Downloads / 다운로드

- [CALF-Harness-1.8.9-macos-arm64-gcn-preview.1.zip](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Harness-1.8.9-macos-arm64-gcn-preview.1.zip)
- [CALF-Workbench-1.9.4-macos-arm64-gcn-preview.1.zip](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Workbench-1.9.4-macos-arm64-gcn-preview.1.zip)
- [CALF-Harness-1.8.9-windows-x86_64-gcn-preview.1.zip](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Harness-1.8.9-windows-x86_64-gcn-preview.1.zip)
- [CALF-Workbench-1.9.4-windows-x86_64-gcn-preview.1.zip](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Workbench-1.9.4-windows-x86_64-gcn-preview.1.zip)
- [CALF-Harness-1.8.9-linux-x86_64-gcn-preview.1.tar.gz](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Harness-1.8.9-linux-x86_64-gcn-preview.1.tar.gz)
- [CALF-Workbench-1.9.4-linux-x86_64-gcn-preview.1.tar.gz](https://github.com/VibePakcr/CALF/releases/download/gcn-20261109-preview.1/CALF-Workbench-1.9.4-linux-x86_64-gcn-preview.1.tar.gz)
