# Install CALF and start a task

[Website](https://calf.vibepackr.com/en/) · [Download](https://calf.vibepackr.com/en/#downloads) · [Picture guide](https://calf.vibepackr.com/manual/?lang=en#install) · [한국어](INSTALL_KR.md)

## 1. Download Workbench

Choose the file for your computer on the [download page](https://calf.vibepackr.com/en/#downloads). Workbench is the desktop app; Harness is for terminal use.

| Computer | Requirements |
| --- | --- |
| Mac with Apple Silicon | macOS 14 or later. Workbench 1.9.18 is signed and Apple notarized. |
| Windows x64 | Microsoft Edge WebView2 Runtime. The Windows package has no publisher signature. |
| Linux x64 | Debian 13, GTK 3, WebKitGTK 4.1 and a graphical desktop. Other distributions need a separate compatibility check. |

Compare the downloaded file’s SHA-256 with `SHA256SUMS` on the same release page. Follow your OS’s usual security checks when opening the app.

## 2. Extract and open

Extract the **whole archive into a new folder** and keep its files together.

| System | Open |
| --- | --- |
| macOS | `CALF Workbench.app` |
| Windows | `calf-terminal.exe` |
| Linux | `./calf-terminal` from a terminal in the extracted folder |

On Linux, use `tar -xzf FILE.tar.gz` to keep executable permissions. Keep `calf` or `calf.exe` beside the desktop executable. On macOS, both are inside the app bundle.

## 3. Start a small task

1. Choose **Choose workspace** and select your project folder.
2. Use **Connect AI** to select the AI you already use.
3. Describe the result you want, what to keep unchanged and how to check it. **Use a request outline** can help you get started.
4. Check that your project’s tools are ready, review the request and choose **Submit**.
5. Open **Diff** and the result summary to review the changed files and checks.

CALF uses the checks already set up in your project, such as unittest, configured pytest, supported Cargo integration tests or node:test. Install missing project tools yourself. Choosing checks does not run them; look at the results after the task.

Use **Current** for the latest status and **Recorded** for earlier results. If the files or check environment change, an earlier success may need checking again.

[Follow the first-task guide](FIRST_TASK.md) · [Open the illustrated manual](https://calf.vibepackr.com/manual/?lang=en#start)

## If you already use CALF

Keep your complete `CALF_WORK_HOME`, contracts, settings and older version folders. Point the new program to the same data folder. Older tasks may need the runtime they started with, so keep the `runtimes` folder too.

Read [Update and recovery](UPDATE.md) before switching an existing installation. For Codex, Antigravity or Claude, follow [Host connections](HOST_CONNECTIONS.md) and review any new hooks through the host’s normal approval steps.

CALF is free to use. Your AI service keeps its own account, fees and approval settings.
