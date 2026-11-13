# Install CALF Workbench

[CALF website](https://calf.vibepackr.com/en/) · [Downloads](https://calf.vibepackr.com/en/#downloads) · [Illustrated installation](https://calf.vibepackr.com/manual/?lang=en#install) · [Online manual](https://calf.vibepackr.com/manual/?lang=en) · [한국어](INSTALL_KR.md)

**Installing for the first time?** Choose [Workbench for your OS](https://calf.vibepackr.com/en/#downloads), then open the [illustrated installation and first-task manual](https://calf.vibepackr.com/manual/?lang=en#install). The short instructions below remain available here.

1. Download the latest **published Workbench** for your OS from [Downloads](DOWNLOADS.md). Compare its SHA-256 with that release's SHA256SUMS. A source candidate is not a published package.
2. Extract the whole archive into a **new folder** and keep its files together. On macOS, open CALF Workbench.app. On Windows, run calf-terminal.exe. On Linux, run ./calf-terminal in a graphical desktop.
3. Follow [First task](FIRST_TASK.md): choose a project folder, connect your existing AI account, describe the result and limits, then find the project's checks. Finding checks does not run them.
4. After the task, review Diff and the current result summary. A saved success can become UNKNOWN if files or the check environment change.

CALF is free to use independently. Your AI service keeps its own account, fees and approval rules. Project tools such as Python, Cargo or Node are needed only for the corresponding project checks. Current native host adapters run in Rust; optional SDK examples may use their own client language.

## OS requirements

- macOS ARM64: macOS 14 or newer. Check the exact release's Developer ID and Apple notarization status; local source candidates need their own distribution checks.
- Windows x64: Microsoft Edge WebView2 Runtime. Publisher signing is not currently claimed. Follow your normal OS security policy.
- Linux x64: GTK 3 and WebKitGTK 4.1. Debian 13 is the qualified distribution; other distributions are not automatically covered.

## Existing installations

Keep the complete CALF_WORK_HOME, contracts, settings and old version folders. Use the same data home with the new executable. Tasks may remain pinned to an older runtime. Read [Update and recovery](UPDATE.md) before switching a managed launcher; do not delete an old runtime to make room.

For Codex, Antigravity or Claude, follow the [host connection guide](HOST_CONNECTIONS.md) and use the matching kit included in your package. Inspect an existing installation before adding a route. New Codex hook definitions require the host's normal review. Publishing a package does not update running sessions or grant command permission.
