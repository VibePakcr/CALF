# Workbench 1.9.14 — monitor and sidebar update

The system monitor keeps mint usage bars and numeric values, with thin dark blue-gray tracks in the unused space. Warning colours still reflect high usage. CPU shows the three busiest logical cores and the detected total. Labels accommodate larger core numbers. The left panel scrolls independently so the bottom navigation and version remain reachable with shorter windows and long workspace paths.

Actual GUI checks passed on Mac, Windows with 16 logical CPUs and Debian 13 with 8 logical CPUs. Additional 128-core and unknown-value checks used synthetic input, not 128-core hardware. The Linux test machine had no GPU driver counter and correctly showed Unavailable. These UI sources are unchanged in the 1.9.14 build; the new package identities and update/resume checks are recorded separately in [VERIFICATION.json](VERIFICATION.json).

Workbench uses a new version so existing 1.9.13 installations can find the update. Harness 1.8.17, SDK 0.2.10, host-hook trust and completion rules are unchanged. Records, work contracts, preferences and older runtimes remain in place. No additional agent, local model, background service or cloud dependency is added.

Choose Updates or download the package for your OS, keeping your existing records home. Earlier releases remain available. The Mac app uses Developer ID signing and Apple notarization; Windows publisher signing is not provided. Linux qualification covers Debian 13 x86_64 with GTK 3 and WebKitGTK 4.1. Check [SHA256SUMS](SHA256SUMS) against the exact archive you download.
