# Engineering knowledge in CALF

[한국어](ENGINEERING_KNOWLEDGE_KR.md)

**Built-in references work immediately after installation. No import or CLI setup is required.**
CALF finds relevant references on the local CPU and connects them to new tasks.
Planning, repair and review use the task's retained selection, including after resume.

## Add your own material

1. Open **Engineering knowledge** in Workbench.
2. Click **Add a material folder…** and choose your folder.
3. CALF checks the files, builds a local search index and shows the connected document count.

Choose ordinary UTF-8 Markdown (`.md`) or text (`.txt`) files. You do not need to
prepare manifests or search chunks. An existing CALF knowledge export also works
with the same button. The import uses the current Workbench records folder;
there is no environment variable to set.

New tasks use the connected material automatically. Original files, existing task
references, records, contracts and settings are retained. An existing personal
library is kept and is never replaced automatically.

Cancelling the picker keeps the current references. Failed imports never select
partial material; built-in references remain available. After fixing the error,
you can choose the folder again.

## Coverage and data handling

The built-in catalogue contains 367 Pack, Pattern and Method references. Some
are `NAMED_REFERENCE` entries with names and links rather than a full definition.
A separate private corpus is not automatically included.

Import and search run locally, without AI calls, uploads or source execution.
**When you later start an AI task, selected excerpts are sent to your connected AI.**
Choose material that is appropriate for that provider. Full private corpora are
never added automatically to public packages.

Text folders support up to 1,000 files, 512 KiB per file, 32 MiB total and eight
subfolder levels. Hidden entries, links and `node_modules`, `target`, `dist`,
`build` and `vendor` directories are skipped. Unsupported files are not executed
and conversion dependencies are not installed.

Local lexical search and English/Korean topic aliases select bounded references.
Selection and integrity checks do not prove applicability or task completion.
Current registered project checks and review conditions still decide completion.

## Advanced use

The CLI uses the same import path when Workbench is not needed:

```sh
calf knowledge import /absolute/path/to/material
calf knowledge status
calf knowledge resolve "database query performance"
calf knowledge verify
```

`CALF_WORK_HOME` is an advanced override. Ordinary installations have a shared
OS-specific default for Harness and Workbench. Managed installations keep their
configured storage location.

The Workbench viewer and Repository Local MCP `engineering_knowledge` remain
read-only. Adding material uses a separate folder-selection command; search does
not provide import or execution authority.
