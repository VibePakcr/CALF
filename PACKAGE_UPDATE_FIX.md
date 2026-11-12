# In-app update package correction — 12 November 2026

Harness **1.8.17** and Workbench **1.9.13** now have corrected update packages for macOS ARM64, Windows x64 and Linux x64. SDK **0.2.10** is unchanged. This is packaging revision 1; executable versions and executable hashes have not changed.

The earlier archives were missing the manifest and internal file checksums required by CALF's updater. The Mac ZIP also exceeded its 128-entry limit because it carried machine-specific metadata. The corrected archives include both verification files and contain at most 63 regular file entries. The updater's limits and validation rules have not been relaxed.

Download the refreshed archive if you want to use **Updates** inside the app. A copy downloaded before this correction still has the old layout. Check the current [SHA256SUMS](SHA256SUMS) against your exact download. Older versions remain available; superseded copies of these six archives are retained with `-before-update-fix` in their names and listed in [SUPERSEDED_SHA256SUMS](SUPERSEDED_SHA256SUMS).

The local staging qualification passed on all three operating systems: prepare and activate the package, resume an old paused task with its original checks, return to the previous version, and resume a newer task using its retained runtime. Deliberately incorrect hashes and unlisted prepared files are rejected. A compiled deterministic provider was used; these checks do not represent new paid AI sessions.

The Mac Workbench's existing Developer ID signature and stapled notarization ticket remain intact. Windows packages remain unsigned by a publisher. Linux qualification covers Debian 13 x86_64. Existing records, contracts, preferences, host-hook trust and older executables are retained. No additional agent, model, cloud service or product dependency is introduced.

Fresh public-download qualification is recorded separately in [VERIFICATION.json](VERIFICATION.json). Publication of a package does not itself update an existing installation.
