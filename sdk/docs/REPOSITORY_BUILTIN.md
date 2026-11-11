# Built-in Repository Intelligence

[한국어](REPOSITORY_BUILTIN_KR.md)

Repository Intelligence now belongs to the shared CALF Rust core. Harness and Workbench use the same module index, exact-record reader and GCN/MCL gate. There is no Repository extension to install and no Python, Node, local model or background indexer in this runtime path. FFmpeg remains a separate, optional extension.

## Start with one project

In Workbench, choose your workspace, open **Repository context**, then **Connect records…**. Select the folder that contains that project's CALF `history.html`. CALF validates the existing native history and creates an additive registration and derived module map outside the project. It does not replace an existing registration. Refresh the module list, choose one module and select **Read module**. Search looks through that module's bounded metadata; selecting a match reads the exact original record.

An existing explicit module map and lane plan can instead be registered from Harness:

```sh
calf context --home /absolute/registry bind --project /absolute/project --history /absolute/records/history.html --modules /absolute/modules.json --cache /absolute/cache
calf context --home /absolute/registry read --cwd /absolute/project --task "Continue the invoice work"
calf context --home /absolute/registry search --cwd /absolute/project --module billing --query rounding
calf context --home /absolute/registry record --cwd /absolute/project --module billing --seq 42
```

The cache must be outside the project and records folder. Add `--lanes /absolute/lanes.json` when binding an existing lane plan; use `resume`, `lane` and `gate` for that plan. An unregistered project returns `UNBOUND`; an ambiguous request returns a small `SELECT_MODULE` catalogue. Neither case triggers a scan of your home or other projects.

## What stays authoritative

The original `history.html`, record IDs, sequence numbers, hash chain, contracts and native checks remain authoritative. Markdown files are derived reference views. Warm module reads load only the selected projection and report source bytes read. Old decisions can be located through bounded metadata and read by exact offset and hash. A changed source invalidates the cached view. A historical PASS or `READY` lane is not permission to execute or evidence of current completion. Use native `status` for a current verdict; `UNKNOWN` and `WAIT` remain incomplete.

Opening a module in Workbench does not attach it to a prompt or send it to an AI. Record content is displayed as text and treated as untrusted reference material.

## SDK and Local MCP

The Python SDK is a thin client:

```python
context = client.repository_context(workspace, task="Continue invoice work", registry=registry)
server = client.repository_mcp_server(registry, workspace)
```

Node provides `client.repositoryMcpServer(registry, workspace)`. The equivalent native command is `calf repository-mcp REGISTRY PROJECT`. This foreground, read-only MCP connection exposes only scoped repository queries. It cannot register projects, execute work, adopt results or change policy.

## Related-file analysis

The related-files view uses a bounded Rust lexical scanner for Python import, symbol and call candidates: at most 64 files, 1 MiB and three seconds per query. It ignores comments and string bodies. It does **not** provide full Python grammar validation, semantic analysis or automatic test selection. Its response explicitly says `syntaxValidation: NOT_PERFORMED`; project checks still run in the project's own language runtime. The earlier Python AST cache is retained and not reused as a native result.

## Update and recovery

Install a new CALF version beside the previous one. Existing project registrations, aliases, module maps and lane plans are read directly; derived native views get a new cache identity. Old extension files and stores remain available for provenance or rollback and are excluded from the active extension catalogue. No query rewrites the original journal, contracts or settings. Do not delete old task runtimes or scene versions merely because a new core is selected.

## Retained local Git observations

**Capture local Git** in Workbench reads a bounded file map and raw HEAD/index/working versions. It does not run Git status, worktree diff, filters, hooks or fetch. Only installed Git 2.43+ is used; no Python reader or viewer server is needed. Capture data stays outside the inspected repository. Symlinks, credential-named and generated paths are excluded; incomplete coverage is labelled PARTIAL.

```sh
calf repository capture --project /absolute/repository --data /absolute/captures
calf repository inspect --data /absolute/captures --capture CAPTURE_SHA
calf repository source --data /absolute/captures --capture CAPTURE_SHA --path pkg/invoice.py --version working
calf repository export --data /absolute/captures --capture CAPTURE_SHA --output /absolute/new-export
```

Select `head`, `index` or `working` explicitly when reading saved source. A later edit cannot change those retained bytes. Capture, source and graph hashes are checked when read. Offline export omits origin paths and source bodies by default; add `--include-source` only when you intend to copy code. A saved capture or lexical relationship map is an observation, not a current application CHECK. Hosted browsing and the separate Navigator interface are not merged.
