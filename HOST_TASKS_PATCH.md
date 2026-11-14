# Connected host tasks and status lookup

Harness **1.8.23** · Workbench **1.9.20** · SDK **0.2.11** unchanged.

[Install](INSTALL.md) · [Downloads](DOWNLOADS.md) · [한국어](HOST_TASKS_PATCH_KR.md)

## Connected tasks

Connected tasks displays explicitly linked Codex CALF journals. Select a card to read its details in Task status. Cards refresh while visible and follow newer responses in that same host session. No cards are shown when no links are registered. Worker graph counts Workbench-owned work.

Links observe work in its original host. Linking or reading never submits, pauses, resumes, cancels or restarts it. The original host keeps its execution and permission boundaries.

## Recorded evidence and current observation

Recorded completion is historical. Current observer / Current tracking describes this observation. Activity recorded and Tool start recorded describe receipts. Response ended means one response ended; these labels do not establish process liveness or completion of a whole work program.

Unregistered completion criteria retain UNKNOWN. Changed, unreadable or ambiguous observations stay unavailable. A different task or historical success cannot substitute for the selected evidence.

## Writer-safe lookup

Background lists no longer invoke a retained runtime's writer journal. If an explicit query finds that the original writer holds its lock, it reads the committed checkpoint and leaves current validation unknown. It never removes locks or repairs/converts records. Missing or changed original runtimes remain errors.

## Preservation

Existing records, contracts, settings, pinned task runtimes and previous releases are retained. New versions stage separately and do not automatically replace the running window or host work. Private task bindings and user records are excluded from public packages.

## Local links to existing CALF records

Existing registered links continue to work. For a new link, the CALF records home's local host-status.json explicitly identifies the existing journals. Keep this file local. The existing CALF_WORK_HOME selection or calf task home identifies the records home.

Schema 1 has a sources array. Each source declares id, title, host (codex), the original session and journals. Each journal declares the existing response directory's absolute physical path, original workspace identity and original turn. Optional followSession: true selects the newest response inside that exact workspace/session namespace. The first journal is the primary activity stream; additional journals expose receipts for other workspaces of that same session.

Limits are 16 links, eight journals per link, 128 session entries and the existing canonical history read limits. Modification time selects an observation candidate only. Canonical history, session, turn, namespace and workspace identities are verified. Tied ordering or a changing read stays unknown. Do not edit original journals or contracts to make a link match.
