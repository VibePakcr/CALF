# Existing local model servers (preview)

[한국어](LOCAL_MODELS_KR.md)

The optional Rust transport connects to an **existing Ollama** or
**OpenAI-compatible chat server**, including MLX-LM. CALF's controller,
knowledge retrieval and checks still run locally on the CPU without a model.
The model server has its own inference and resource requirements.

In Workbench, open **AI connection → Existing local model server**. Choose the
server type, enter its address and the exact model name listed by that server.
Ollama normally uses `http://127.0.0.1:11434`; a chat server uses its actual port
and `/v1`, for example `http://127.0.0.1:8080/v1`.

**Verify connection** reads the model list. It does not generate a response,
download weights or start a server. CALF accepts only explicit HTTP loopback
addresses (`127.0.0.1` or `::1`), disables proxies for these calls and refuses
redirects. It does not change the machine's proxy or runtime settings. Start
your server separately; CALF does not fall back to a cloud service.

The API connection has `kind: "local"`, `protocol: "ollama"` or
`"openai-chat"`, `endpoint`, `model` and `outputTokens` (128–2048; Workbench
uses 512), alongside the usual native `helper`, `executable` and `account`
fields. New jobs retain their own connection and executable. Earlier jobs keep
their original settings. Local inference is classified as heavy work.

Responses must be complete JSON matching the existing plan/review contract.
Truncation, duplicate keys, tool calls and wrong shapes cannot become a valid
plan. File ownership, protected inputs, registered checks, independent review
and completion rules remain unchanged. Model context limits can still reject
a large task; CALF does not silently truncate evidence or weaken checks to fit.

Requests time out after 150 seconds. Ollama requests use a 4,096-token context
and `keep_alive: 0`. Model memory is separate from CALF memory. Interrupting
CALF does not guarantee that another server has cancelled its inference;
reconcile that server's state before resubmitting an uncertain request.

## Qualification of this release

On the MacBook Air M5 16 GB, a real Codex-connected synthetic task completed
with the same knowledge-selection digest, registered checks, a separate review
and three independently rerun tests. This validates that task, not the accuracy
or benefit of every knowledge reference.

The installed Qwen 7B Ollama model was reached, but loading caused a swap surge
and CALF interrupted the attempt. The installed Qwen 7B MLX model loaded using
MLX 0.32.4 / MLX-LM 0.32.2, but its existing guard stopped the isolated server
after memory warning persisted for 20 seconds. Neither trial completed the
task. Their failures are retained; the resource limits were not relaxed.
MLX/Ollama end-to-end task completion is therefore **not qualified** in this
release. This is separate from the successful model-list connection and
model-free transport tests. No new weights were downloaded.

Windows/Linux knowledge and queue qualification does not imply that MLX is
available there or that a local model has been tested on those hosts. This optional connection remains a preview. Installing this release does not
start or reconfigure an existing model server.
