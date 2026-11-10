# Install CALF Workbench

[한국어](INSTALL_KR.md) · [Downloads](DOWNLOADS.md) · [First task](FIRST_TASK.md) · [Visual manual](CALF_mannual.html#install)

1. Download **Workbench 1.9.7** for macOS ARM64, Windows x64 or Linux x64 from [Downloads](DOWNLOADS.md). Compare the file's SHA-256 with the release SHA256SUMS.
2. Extract the complete archive into a **new folder**. Keep its files together. macOS: open CALF Workbench.app. Windows: run calf-terminal.exe. Linux: run ./calf-terminal in a graphical desktop with WebKitGTK 4.1 and its runtime dependencies.
3. Follow [First task](FIRST_TASK.md): select a folder, connect an existing AI account, write the result, limits and checks.

Updating an existing installation: retain the complete CALF_WORK_HOME, contracts, settings and old version directories. Use the same records home for the new executable. Old tasks can remain pinned to their prior runtime. See [Update and recovery](UPDATE.md) before switching a managed launcher. Do not delete an older runtime to make room for this update.

An external AI account/host and project check tools are separate dependencies. The included hosts/ kit supports Workbench 1.9.7; the older SDK 0.2.4 archive remains unchanged. Use this release's included host kit for a 1.9.7 core. Claude host installation is qualified on macOS only.

macOS has an ad-hoc integrity signature, not Apple notarization. Windows has no publisher signature. Review an OS security prompt using your normal policy; this guide does not ask you to disable protections. See the manual for platform requirements and supported execution paths.
