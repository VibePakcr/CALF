# Routing and lane evaluation

`calf evaluation` evaluates supplied model/skill selections and reads accounting from explicit native task journals. The Rust core reuses GCN planning, write-owner validation and canonical journal observation. Reports are read-only and keep `executionAuthority: false` and `currentCompletion: "NOT_EVALUATED"`.

## Evaluate selections

```sh
calf evaluation < routing.json
```

```json
{
  "schema": "calf.evaluation.v1",
  "op": "routing",
  "provenance": "synthetic",
  "cases": [{
    "id": "prose-negative-control",
    "category": "prose",
    "expectedModels": ["model-a"],
    "requiredSkills": [],
    "forbiddenSkills": ["release"],
    "selectedModel": "model-a",
    "selectedSkills": []
  }]
}
```

Use `synthetic` for fixtures or `source_reported` for supplied observations. This label does not authenticate the source. The report separates model agreement, missing required skills and forbidden skill selections. Contradictory labels, duplicate IDs and duplicate selections are rejected.

An empty skill list is an observed selection of no skills. `null` is an unavailable observation and is excluded from the accuracy denominator. An observed model with no expected labels is unlabelled. These scores measure agreement with the supplied labels; they do not prove actual host skill invocation or model quality.

## Read a checkpoint and account for lanes

Send this request with real, absolute paths:

```json
{
  "schema": "calf.evaluation.v1",
  "op": "checkpoint",
  "workspace": "/absolute/project",
  "journal": "/absolute/state"
}
```

For `op: "lanes"`, supply `moduleIds`, the existing `calf.gcn.lanes.v1` plan, `bindings`, and `rates` (an empty array is valid). Each binding contains `cell`, `workspace`, `journal`, `task` and the exact observed `head` with its `seq` and `hash`. See the Korean guide for a complete plan example. The native API accepts the same request through `{"op":"evaluation","request":…}`.

Bindings explicitly attribute a recorded task to a cell. They do not prove that the task contract's file scope equals the plan's write scope. The native planner validates dependencies and write conflicts. Shared prerequisite cells count once in the overall total; each lane subtotal includes its own prerequisites, so lane subtotals are not additive.

`UNBOUND_NOT_OBSERVED` means a cell has no supplied task binding. `NO_START_RECORDED` means the bound journal has no process start for that task. Neither proves that a task never ran elsewhere. Saved outcomes and check receipts remain historical. Required, observed and missing recorded checks are reported separately; the query runs no checks and grants no current completion verdict.

A changed checkpoint, an in-progress journal extension or a bounded observation limit rejects the query. The reader neither takes over the writer nor repairs the source. Inputs are limited to 512KiB and reports to 256KiB, within the existing journal record/byte budgets. Lanes retain the native logical single-executor meaning.

## Usage, time and estimates

New native provider attempts record monotonic elapsed time for success and failure. `sumProviderElapsedMs` is a sum of call durations, including transport overhead. It is not total task makespan or pure inference time.

Built-in adapters collect numeric counters when a supported response supplies them: OpenAI Responses usage, a single Codex `turn.completed` usage event, local OpenAI-compatible Chat usage, or Ollama prompt/evaluation counts. Ollama cached-input counts and Antigravity usage remain unavailable. The configured/requested `model` is not independent attestation of the provider's resolved backend model.

Counters travel through an optional receipt bound to the operation and input hash. Provider reply formats and task checks are retained. Missing, malformed, unsupported and legacy counters stay `null`. A partial total stays `null`; `known…` fields and observed-call counts expose only the known portion. Known zero with incomplete coverage does not mean a free call.

Each optional rate entry has `provider`, `model`, `sourceSha256`, `inputMicrosPerMillion`, `outputMicrosPerMillion` and `cachedInputMicrosPerMillion`. Units are micro-USD per million tokens. Uncached input and cached input are priced separately, with each call rounded down to micro-USD. The exact provider/model rate and all required counters must be present. The source hash binds supplied data but does not verify a current tariff. `billedCost` remains `null`.

## Real-model pilot

On 2026-11-19, the official Codex CLI ran three isolated tasks per model at requested medium reasoning, one attempt each: decimal CSV totals, half-open interval merging and a skill-selection fixture. CALF recorded 12 planner/reviewer calls. Both models passed all three native checks, current status reads and separate check reruns.

| Requested model | Tasks passed | Median task time | Input/output tokens, all three tasks | Standard API equivalent, all three tasks |
| --- | --- | --- | --- | --- |
| GPT-6.2-Sol | 3/3 | 40.112s | 145,156 / 3,459 | $0.324902 |
| GPT-6.2-Astra | 3/3 | 38.319s | 151,341 / 2,780 | $1.321928 |

The token counts are provider-reported. The price column applies the published short-context Standard API rates, excluding unreported cache writes, tier multipliers and subscription credit accounting; it is not an invoice. Each model has only three single-attempt samples. Backend load, service tier and cache state were not controlled, so this pilot does not establish a general model ranking or repeatable speedup. The generated selector passed four observed required/forbidden selection cases; it did not invoke host skills.

[OpenAI Sol rates](https://developers.openai.com/api/docs/models/gpt-6.2-sol) · [Astra rates](https://developers.openai.com/api/docs/models/gpt-6.2-astra) · [한국어 안내](ROUTING_EVALUATION_KR.md) · [Qualification](https://github.com/VibePakcr/CALF/releases/download/v1.9.21/ROUTING-LANE-VERIFICATION.json)
