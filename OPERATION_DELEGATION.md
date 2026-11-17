# CALF credential-isolated operation delegation

Harness 1.8.24 · Workbench 1.9.21 · same-version Under Patch.

A trusted Mac broker performs a fixed read operation requested through a separately provisioned Linux environment. Operator credentials stay on the Mac; the separated protocol client receives only the required result. Existing Codex, Claude, Antigravity sessions and running tasks are not automatically moved into this route.

## Operation and result

The supported operation is `github.repository.status` for the exact repository declared in the profile, through a fixed HTTPS API. No arbitrary command, shell, URL, environment, stdin or approval field is accepted for privileged execution. Results contain only `repositoryId`, `private`, `archived` and `disabled`. Raw provider responses, errors and tokens are not returned.

## Separation boundary

The Mac broker uses the system SSH client to connect to a fixed `calf authority client` on an independently provisioned and qualified Linux host. It does not launch a local untrusted executable. Loopback and local Mac interface addresses are denied. The trusted SSH binary and known-host material are bound to the exact profile.

Agent, port, X11 and filesystem forwarding, connection reuse, ambient SSH configuration, proxies and local commands are disabled. The existing SSH key is used only by the trusted local SSH client for authentication; neither the key nor the original authentication socket is handed to the separated client.

The deployment operator must provide a separate environment without access to Mac credentials and a trusted local deployment observation. A hostname or remote process self-description does not prove isolation. CALF does not automatically certify arbitrary machines or isolate every existing host process.

The credential-holding broker currently runs on macOS. Linux and Windows deny this broker profile while retaining their existing task routes. The Linux protocol client can run in the separated environment.

## Approval and single-use authority

Inspect capabilities with `calf authority describe`. `calf authority prepare PROFILE_JSON SHA256` prepares a reviewable ticket and grants no authority. Run the exact returned `calf execute TICKET SHA256` command through the host's existing permission flow.

A separate trusted Mac dialog shows the repository, peer, task and request digest. `Allow once` is required before SSH authentication or GitHub credential access. The default is `Deny`; cancellation or timeout denies. Model prose and remote approval fields are not authority. This local dialog is neither Touch ID nor a cryptographic human-consent signature.

Authority is process-local, monotonic, single-use and limited to at most 60 seconds. It is reserved before starting the SSH transport. Failed attempts do not restore the use budget. Persistent, reusable and restart-resumable leases are unsupported. Channel loss, uncertain lock observation, cancellation or changed policy identity denies new provider dispatch. Uncertain dispatched outcomes or lost acknowledgements remain `UNKNOWN` with the original receipt and no automatic retry.

Acknowledgements bind to the same session, request and result digest. They are not independent verification or current task completion. Cleanup proves termination of the local SSH transport only; it does not control an existing remote agent's lifecycle.

## Profile and credential references

A `calf.operation-profile.v2` binds an accepted TASK workspace/ID/digest, operation and repository, GitHub account reference, numeric separated-host SSH address/port/user/host-key alias, trusted SSH and known-host digests, local key reference, fixed remote client path, empty transport cwd and a trusted local deployment observation reference. `lifetimeMs` is 1–60000 and `maxUses` is 1. Keep the profile and observation outside the untrusted client's write boundary.

The operator separately provisions an OS credential-store entry using service `CALF.operation.github` and the profile's `credentialAccount`. Never put a token in a profile, argv or client input. No credential-import or credential-writing CLI is provided. Use only the minimum repository read permission required; an unavailable store fails closed.

## Evidence and preservation

Preparation, reservation and termination bind to native ACTIONs under the same TASK and the exact execution ticket/terminal receipt. A result does not replace an independent CHECK or current completion judgment. Existing enterprise VibePackr Binding and Runtime Invocation authority remain with their canonical Rust owner.

Existing records, contracts, settings and pinned task runtimes are retained. The route is opt-in. Rollback selects the prior installation while retaining receipts and unresolved outcomes without replay.

Qualification uses actual SSH to the approved separated host and synthetic GitHub replies. Synthetic proof is not proof of an operator token's permissions or an authenticated GitHub operation. See `OPERATION-DELEGATION-VERIFICATION.json` for the actually executed scope.
