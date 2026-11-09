# Recorded results and current status

[한국어](STATUS_CONTEXT_KR.md)

CALF separates saved execution results from later status queries. A check that
passed in Claude remains evidence of that execution. A query from another app
can return `UNKNOWN` if its environment differs; it does not change the original
result.

In Workbench, choose a workspace and open **Task status**. Select a registered
task to see **Recorded completion**, **Current observer**, the recorded CHECK
result, file-version binding and context differences. **Refresh status** only
reads evidence; it does not run checks or call an AI. Managed task cards also
have an expandable recorded/current status summary.

```text
calf status WORKSPACE TASK
calf run-status WORKSPACE STATE TASK
```

The existing top-level `outcome`, reasons and evidence remain authoritative.
The additive `statusView` is diagnostic. Saved `SATISFIED` or process exit 0 never
overrides current `UNKNOWN` or `VIOLATED`.

For example, `LC_ALL` unset during execution and `LC_ALL=C.UTF-8` during a query
appears as `LC_ALL: Not set → C.UTF-8`. The current verdict stays `UNKNOWN`.
CALF does not change environment variables to make fingerprints match. Unset
and empty values remain distinct. Safe locale values can be shown; arbitrary
environment values are redacted and compared by digest. Check Profile changes
are also reported without saving raw search paths or interpreter options in
the new diagnostics.

New registered checks add optional context observations as ordinary ACTION
records linked to the unchanged CHECK id and envelope hash. CALF 1.8.9 can read
this format. Managed checks add details to their existing journal payload.
Observations never participate in completion rules.

Older receipts keep their original fingerprints. If bound field details are
missing, CALF says so and does not infer old values. When the original context
has been independently established, an operator can run:

```text
calf observe-context WORKSPACE TASK CHECK_ID
```

Details are appended only if the full current context fingerprint matches that
CHECK exactly. A mismatch is refused without changing history. Later observations
are labelled as such; they do not rerun or approve checks. Existing envelopes,
hashes, contracts and settings are kept.

Details load on demand and are released when closed. No background indexer,
model or GPU is used. Tasks pinned to older managed runtimes keep using those
runtimes; absent details are not reconstructed or treated as fresh verification.
Pending, cancelled, inactive and stale evidence keep their completion restrictions.
