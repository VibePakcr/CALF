# Clearer views and retained task status

Harness **1.8.22** · Workbench **1.9.19** · SDK **0.2.11** unchanged.

[Install](INSTALL.md) · [Downloads](DOWNLOADS.md) · [한국어](UI_STATUS_PATCH_KR.md)

## Open and close a view

Preferences, Updates, Engineering knowledge, Task status and other sidebar views occupy the central work area. Underlying task buttons no longer overlap. The sidebar remains available and the title and **Close ×** stay visible while contents scroll.

Use **Close ×** or Escape to return. Request drafts and unsaved form text are retained. Tab moves through fields and actions and back to navigation. Request help and task finding use separate dialogs when needed.

Empty folders and missing material show an actionable message and disable unavailable actions. Updates enables download only for an offered newer version. Preparing a local package requires both the file and its full SHA-256.

## Read a retained task

1. Choose the existing work folder.
2. Open **Task status** and select a task; use **Refresh** when needed.
3. Read **Recorded completion** and **Current observer** separately, together with file versions and available check details.

Workbench-managed tasks and CALF records inside the folder are separate sources. A plain empty HTML file is never converted into a CALF record. A retained task uses its original pinned runtime for the current observation. Missing or changed runtimes never silently fall back to the new executable.

Historical success does not imply current success. Missing execution-context details remain **Unavailable**. Partial-record and bounded-list warnings remain visible. Reading status does not rerun AI work or repair records, contracts or settings.

## Update safely

Extract into a new folder or use the app’s update feature. Keep your data folder and task runtimes. Earlier releases remain available. The macOS distribution app uses the existing Developer ID and Apple notarization. Windows binaries have no publisher signature. Debian 13 is the qualified Linux distribution.

Earlier screenshots retain their original version labels. See the included `UI-STATUS-PATCH-VERIFICATION.json` for this patch’s recorded qualification scope.
