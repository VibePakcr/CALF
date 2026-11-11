# A fresh Codex session with built-in Repository Intelligence

[한국어](REPOSITORY_SESSION_VERIFICATION_KR.md) · [Machine-readable result](REPOSITORY_SESSION_VERIFICATION.json) · [Download CALF](https://github.com/VibePakcr/CALF/releases/latest)

Observed on 11 November 2026; published on 12 November 2026. Harness **1.8.15**, Workbench **1.9.11**, SDK **0.2.8**.

## What was actually done

A new Codex session prepared an English/Korean release handoff from frozen, real CALF release and installation evidence. It used the installed Rust core to discover the registered workspace, saw a small module catalogue and selected only `release-handoff`. It read one exact original record, including its sequence and hash; unrelated module records were not loaded. Each read of the selected source reference accounted for **2,724 bytes**. This is a bounded observation, not a claimed percentage reduction or a memory benchmark.

The agent wrote two report files. The registered independent check compared them with the frozen source digests, versions, platform results and claim limits. It ran **once and passed**. Native completion was **SATISFIED**, with the check bound to the same output versions and matching execution context. The checker and contract were not weakened to obtain that result.

An isolated Workbench 1.9.11 review window, copied from the installed application code, then read the same native records. Task status showed both **Recorded completion: SATISFIED** and **Current observer: SATISFIED**, with **File version: MATCH** and **Execution context: MATCH**. This was a record lookup, not another AI task or another check run.

## What the run also caught

The initial test lane had a prerequisite cell with no required check. CALF kept the registered lane at **WAIT**, even though the report task itself passed. A separate corrected lane definition connected that same registered check to the prerequisite and evaluated **READY** in the shared native GCN. The original definition, registration and WAIT evidence were retained. No core or completion rule changed. READY for that separate definition is not a claim that the original registered lane became READY or that the whole project is complete.

## Scope and preservation

All **938** previously captured history files retained their exact hashes. The **12** frozen task-input, contract and checker files also matched, and the initial native task records remained intact.

This adds a real fresh-session handoff observation on **macOS ARM64**. It does not repeat the earlier synthetic Windows/Linux qualification, establish every automatic hook event, or verify all three AI hosts. No memory or soak test was run. Existing release binaries and versioned assets were not rebuilt or replaced; this is an additional verification note for the published release.
