# Technology Track — basic hands-on with the tools at every layer

**Updated:** 2026-10-16 · **Priority:** Part A (tools your builds use) is part of the OWN lane; Part B (other market tools) is low priority, about one lab every 2 weeks or a bonus slot. **Goal:** for each architecture component, you have run the leading tools yourself at least once, can compare them from experience, and know when you'd pick which. Depth stays at "hello-world plus one real integration"; mastery comes from the OWN and SYSTEMS lanes.

**📖 Field guide:** Ch46 is the component map and the build-vs-buy method (§46.5); Ch35–37 frame frameworks, tools and sandboxes, and runtimes; Appendix I maps each managed service across Google Cloud, AWS and Microsoft. Read the component's chapter before its lab (📖 column in `NEXT.md`).

## How labs work (one target, many tools)
- Every lab instruments the **same small target**: your own `agents/hello_agent` in genai-agent-mastery, grown into a 2-tool ADK agent (Capstone A's agent once it exists). One target means every tool comparison is like-for-like.
- Each component gets a **bake-off**: 2–4 tools wired to the same target, then one row per tool in `labs/<component>/COMPARISON.md`: setup time, what it showed you, what it couldn't, cost model, when you'd pick it.
- Labs live in `genai-agent-mastery/labs/<component>/`. You write the code; Claude may pair but never authors.
- Free tiers, trials and OSS self-hosting change often: check the current terms when you start a lab **[Verify]** and never put a paid plan on a card without deciding to.

Levels: **T0** know what it is and when to use it (5-min read) · **T1** ran a hello-world against your target · **T2** you integrated it yourself into a build or capstone · ✅ = used in your builds by Claude Code — **does not count as hands-on**; its BT lab in Part A comes first

## Part A — Build-tool labs: hands-on with every tool Claude Code used (do these first)

Your builds use these tools, but Claude Code wrote the code, so reading it doesn't count as having used them. Each BT lab has two halves:
1. **Build it yourself (30–40 min):** a minimal working thing with the tool, from its official docs, in `genai-agent-mastery/labs/build-tools/<tool>/`. No AI authoring; Claude may answer a question.
2. **Diff against the build (10–15 min):** open where ARB or PM uses the same tool. List what Claude Code did that you didn't, and why (a seam, a test fake, fail-closed handling, a pin). That list is the learning.

BT labs count as **OWN · Rebuild** reps: every third OWN rep can be one. They are not low priority.

Inventory taken from both builds' `pyproject.toml`, Dockerfiles, compose files, CI and `infra/gcp/` on 2026-10-16:

| Lab | Tool(s) | Build it yourself | Then diff against | Pairs with |
|---|---|---|---|---|
| **BT01** | uv · ruff · mypy (strict) · pytest + pytest-cov · pre-commit · Make | A tiny typed package with 3 tests, lint/type/test hooks, a Makefile | ARB/PM `pyproject.toml`, `Makefile`, `.pre-commit-config.yaml` | R02 |
| BT02 | Pydantic v2 · pydantic-settings · jsonschema · PyYAML | Model a tool-call request + result; load settings from env; export and validate a JSON Schema; load a YAML manifest | PM `contracts/`, ARB `governance/manifest.py`, `_schemas/` | R04 |
| BT03 | Google ADK (+ LiteLLM → LM Studio) | An ADK agent with 2 tools, a Runner and a session, running on your local model | ARB `agents/customer_service_ops.py`, `platform/runtime` | R01 |
| BT04 | LiteLLM | Same prompt to LM Studio and Vertex; a fallback; a per-call budget | ARB `platform/model`, `enforcement/model_budget.py` | SD-07, SD-11 |
| BT05 | FastAPI · uvicorn · httpx | A run API: `POST /runs` → 202, `GET /runs/{id}`, `GET /runs/{id}/events` as SSE; an httpx client test | PM `api/app.py` | R05 |
| BT06 | Rego (regopy, plus the OPA CLI for `opa test`) | A deny-by-default `tool_call` policy with 3 rules and unit tests | ARB `governance/policies/rego/tool_call.rego`, `platform/policy/rego.py` | R09 |
| BT07 | Cedar (cedarpy) | The same 3 rules in Cedar; run the same cases | ARB `platform/policy/cedar.py` | R09, GF-5 |
| BT08 | cryptography (Ed25519) | A hash-chained JSONL log, signed head, verify, then tamper and watch verify fail | ARB `evidence/chain.py`, `platform/signing.py`; PM `platform/crypto` | R08, R10 |
| BT09 | OpenTelemetry SDK + OTLP exporter · Langfuse (self-hosted) | Instrument BT03's agent; see the spans in Langfuse | ARB/PM `platform/observability` | SD-09, T01 |
| BT10 | MCP Python SDK · FastMCP | An MCP server with 2 tools and a client that lists and calls them | ARB `gateways/`, `enforcement/mcp_integrity.py`; PM `platform/jira` | R11 |
| BT11 | LangGraph · langgraph-checkpoint-postgres · psycopg · Postgres (Docker) | A 3-node graph with a Postgres checkpointer and an interrupt/resume for approval | PM `platform/runtime`, `platform/approval` | R21 |
| BT12 | Docker · Docker Compose | Containerise BT05 with Postgres; healthcheck; env-based config | ARB/PM `Dockerfile`, `docker-compose*.yml` | SD-08 |
| BT13 | GitHub Actions | CI that runs BT01's lint/type/test on every PR (then the M1 WIF deploy) | ARB/PM `.github/workflows/ci.yml` | R19, R24 |
| BT14 | GCP services via Python clients + gcloud: Vertex AI (google-genai) · Firestore · Cloud Storage · Cloud KMS asymmetric sign · Model Armor | One script per service in your own project; tear down after **[Verify] cost before running** | ARB E4: `infra/gcp/setup.sh`, `platform/{model,state,anchor,screening}`, `platform/signing.py` | R17 |
| BT15 | OpenAI Agents SDK | Rebuild BT03's agent; note where a governance hook can attach | ARB `hosts/openai_agents` | T07 |
| BT16 | Microsoft AGT (pinned version) | Install it in its own environment; write one policy; evaluate 5 cases | ARB `spikes/agt/` | R25 |

## Part B — The map: market tools per component (low priority, bake-offs)

| # | Component | Tools (★ = do the lab; others T0) | Already in your builds | Lab |
|---|---|---|---|---|
| TC-01 | **Agent frameworks** | ★ Google ADK ✅ · ★ LangGraph ✅ · ★ OpenAI Agents SDK ✅ (ARB E3 host) · ★ Microsoft Agent Framework · CrewAI · AWS Strands Agents · Pydantic AI · LlamaIndex agents | ADK, LangGraph, OpenAI Agents SDK | T07 |
| TC-02 | **Protocols** | ★ MCP via FastMCP ✅ · ★ A2A SDK · MCP Inspector | ARB gateways, a2a | T05 |
| TC-03 | **Model access & AI gateways** | ★ LiteLLM ✅ · ★ Vertex AI ✅ · Azure AI Foundry · AWS Bedrock · Portkey · Kong AI Gateway · Apigee | LiteLLM, Vertex (E4) | T06 |
| TC-04 | **Local inference & serving** | ★ Ollama / LM Studio ✅ · ★ vLLM · llama.cpp · SGLang · TGI | LM Studio | T10 (pairs with the MODEL lane) |
| TC-05 | **Observability & tracing** | ★ OpenTelemetry (GenAI conventions) ✅ · ★ Langfuse ✅ · ★ LangSmith · ★ Arize Phoenix / AX · ★ Datadog LLM Observability · W&B Weave · Helicone · OpenLLMetry | OTel → Langfuse in ARB and PM | **T01, T02** |
| TC-06 | **Evaluation** | ★ DeepEval ✅ · ★ Ragas · ★ Vertex Gen AI Evaluation ✅ · promptfoo · Inspect AI · Braintrust · LangSmith evals | DeepEval, Vertex eval | T03 |
| TC-07 | **Guardrails & content safety** | ★ Model Armor ✅ · ★ NeMo Guardrails · ★ Llama Guard · Guardrails AI · Microsoft Presidio (PII) · Azure AI Content Safety · Bedrock Guardrails · Lakera | Model Armor (E4), own guardrails | T04 |
| TC-08 | **Policy & authorization** | ★ OPA/Rego ✅ · ★ Cedar ✅ · ★ Microsoft AGT ✅ · Cerbos · OpenFGA / SpiceDB (relationship-based) | OPA, Cedar, AGT spike | T08 |
| TC-09 | **Identity** | ★ OIDC with Keycloak or Auth0 · ★ GCP Workload Identity Federation ✅ (your M0) · Microsoft Entra ID · SPIFFE/SPIRE | WIF (yours), ARB tokens | T09 |
| TC-10 | **Edge, API gateway, load balancing** | ★ GCP HTTPS Load Balancer + Cloud Run ingress · ★ Envoy or Kong · Apigee · MuleSoft Flex · nginx | — | T11 |
| TC-11 | **Messaging, workflows, durable execution** | ★ GCP Pub/Sub · ★ Temporal · Kafka · Redis Streams · Cloud Tasks / Workflows | — | T12 |
| TC-12 | **Data & vector stores** | ★ Postgres + pgvector ✅ (PM seam) · ★ Firestore ✅ · ★ Redis · Vertex Vector Search · Qdrant · Pinecone · AlloyDB · BigQuery | Postgres seam, Firestore (E4) | T13 |
| TC-13 | **RAG & document processing** | ★ LlamaIndex · ★ Docling or Unstructured · Vertex AI Search · Haystack (you know it) | ARB KB retrieval | T14 |
| TC-14 | **Agent memory** | ★ Vertex AI Memory Bank · ★ Graphiti + Neo4j (Neural Maze lab) · Mem0 · Zep | PM memory seam | T15 |
| TC-15 | **Deployment & runtime** | ★ Docker ✅ · ★ Cloud Run · ★ Vertex AI Agent Engine · ★ GKE basics (kubectl, Helm) · Terraform ✅ · GitHub Actions ✅ · Argo CD | Docker, Terraform, GH Actions | T16 |
| TC-16 | **Prompt & model lifecycle (AgentOps)** | ★ Langfuse prompt management · ★ MLflow (models + LLM tracking) · Vertex Model Registry · LangSmith Hub | — | T17 |
| TC-18 | **Open-source agent harnesses** | ★ OpenHands · ★ Goose · ★ opencode · DeepSeek Harness (preview, DeepSeek-only) · Cline · Hermes Agent · Aider | — (your builds hand-roll their own harness) | T19 — run the same small coding task through two of them; compare loop, permissions, sandbox, logs |
| TC-17 | **Security testing / red-team** | ★ garak · ★ PyRIT · promptfoo red-team | ARB red-team corpus | T18 |

## Lab order (low priority, about one every 2 weeks)
Ordered so each lab lands on something a current OWN or SYSTEMS rep is already teaching.

| Lab | Component | What you do | Pairs with |
|---|---|---|---|
| **T01** | Observability bake-off, part 1 | Instrument the target with OpenTelemetry; send the same traces to **Langfuse** (self-hosted Docker) and **Arize Phoenix** (local) | SD-09, ARB observability |
| **T02** | Observability bake-off, part 2 | Same target into **LangSmith** and **Datadog LLM Observability** (trial); fill `COMPARISON.md` for all four | SD-09 |
| T03 | Evals bake-off | One golden set run through **DeepEval**, **Ragas** and **Vertex Gen AI Eval** | R-evals traces |
| T04 | Guardrails bake-off | Same 10 attack prompts through **Model Armor**, **NeMo Guardrails**, **Llama Guard**; PII via **Presidio** | OWASP GF-2 |
| T05 | Protocols | Wrap one tool as an MCP server (FastMCP) and call it from two frameworks; one A2A call between two agents | R11 |
| T06 | Model gateway | Route the target through **LiteLLM** to Vertex + a local model with budgets and fallbacks | SD-07, SD-11 |
| T07 | Frameworks | Rebuild the target in **Microsoft Agent Framework** and **CrewAI**; note where governance hooks attach | GF-1, R15 |
| T08 | Policy engines | Same rule in OPA, Cedar, AGT, and **OpenFGA** (ReBAC) | R27 |
| T09 | Identity | OIDC login with Keycloak in front of the target's API; validate JWTs | R06 (SD-04) |
| T10–T18 | the rest of the map | one lab each, in the order the queue reaches the paired topic | |

**Done means** the `COMPARISON.md` row exists and you can answer, without notes: "for a regulated enterprise on GCP, which would you pick and why not the others?"
