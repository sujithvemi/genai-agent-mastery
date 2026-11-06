# Resource Registry — every saved resource, one verdict each

**Updated:** 2026-10-30 · **Rule:** a resource earns time only through a rep. Nothing here is a "someday read".

| Verdict | Meaning |
|---|---|
| **CORE** | Absorbed into a rep — you meet it inside the queue; no separate reading |
| **PICK** | A library: pull *one* lesson/video/chapter only when a rep's gap calls for it |
| **SKIM** | 5–10 min glance *after* the rep that covers the topic — to confirm, not to learn |
| **PARK** | Not now; named trigger to revisit |
| **DROP** | Stop. Unsubscribe / unsave / archive. Covered elsewhere or off-goal |

---

## 1. Saved links + downloaded posts (`production_gen_ai_learning/`)

| Resource | What it is | Verdict | Where it lands |
|---|---|---|---|
| AI Engineering from Scratch (aiengineeringfromscratch.com, free, 20 phases / 523 lessons) | Hands-on library, math→agents | **PICK** (primary GROUND library) | Ph7 attention/KV/spec-decoding, Ph5 tokenization + evals, Ph13 MCP, Ph14 agent loop, Ph17 infra — per gap |
| AI System Design Playbook — Himanshu Ramchandani (PDF, 39 pp, 18 cases × 2 pp) | Production case studies, sourced | **CORE** | One case per PROVE drill; #2 vLLM, #5 prompt cache, #10 KV cache, #11 MoE, #17 RouteLLM feed GROUND |
| LLM System Design handbook preview (AI Engineering Insider, 40 pp of 367) | Interview handbook | **PICK** | PROVE spine alongside Hello Interview; full book only if PROVE weight rises in 2027 |
| 30 Core Agentic Engineering Concepts (System Design One, Jun 2026) | Concept map | **SKIM** → used as a checklist | After shared-core reps: tick which of the 30 you can explain from your own code |
| Agentic Evals pt 1 (Yesha Shah, Aug 2026) | Conceptual intro (pass^k, trajectory grading) | **SKIM** | After the eval-harness trace rep |
| A Complete AI Agent Playbook (#213868098, ~1.5k words) | System design → backend → AWS ECS | **SKIM** | After the E4 deployment trace — compare their deploy story to yours |
| The AI Engineering Playbook — Neural Maze (#174442137) | Index of 5 free courses | **PICK** | Course IV "Kubrick" (MCP) if an MCP rebuild rep needs a reference |
| Building Agent Memory with Knowledge Graphs — Neural Maze (Jun 2026) | Hands-on Graphiti + Neo4j | **PICK** | When tracing pm-agent `platform/memory` (1k lines) |
| Day 59 Active-Passive Failover (#187618084, paywalled sample of a 254-day series) | Drip course | **DROP** | Covered by DDIA 2e + stability-patterns PDF |
| MLSD Interview #30 Transformation Debt (#198240857, paywalled sample) | Drip series | **DROP** | — |
| System Design: Zero to Production (sdcourse, 254 days) | Daily course | **DROP** | Poor fit for bursty time |
| Day 117–126 XGBoost tuning (aieworks) | Classic ML, paywalled code | **DROP** | Off-goal |
| `sys_des_scribd_downloads/stability_patterns_for_microservices.pdf` + `scalability_availability_stability_patterns.pdf` | Timeouts, circuit breakers, bulkheads | **CORE** | Reliability GROUND rep (maps to your gateways/budgets) |
| `intro_to_redis.pdf` | Cache primer | **PICK** | Caching/idempotency rep |
| Cassandra / ZooKeeper / Spark / Memcached / Mongo / Trino / Kafka-eventstorming decks | Tool intros | **PARK** | Trigger: a build actually needs one |
| Kafka: The Definitive Guide (2017) | Dated book | **PARK** | DDIA 2e (Mar 2026) streams chapter first |
| AI ENGINEERING SKILLS CHECKLIST.pdf | Skills checklist | **CORE** (once) | Used to cross-check `maps/coverage_matrix.md` — done |
| 8 Perplexity/Gemini/Claude learning-path PDFs + 3 `.md` roadmaps + `research/` | Generated learning paths | **DROP** (archived) | Already reconciled into the v1 L0–L9 map; superseded by v3 |
| AI Engineering Mastery.jpeg, NotebookLM mind map, haystack mind map | Images | **DROP** | Superseded |

## 2. YouTube playlists (24 · ~2,550 videos)

| Playlist | Owner · size | Verdict | Trigger |
|---|---|---|---|
| Build a Large Language Model (From Scratch) | Sebastian Raschka · 7 | **CORE** | GROUND: transformers/attention block |
| Deep Dives | Hello Interview · 15 | **CORE** | PROVE monthly drill (one deep dive each) |
| Arpit's System Design Masterclass — Pre-requisites | Arpit Bhayani · 22 | **PICK** | Distributed-systems GROUND gaps |
| Backend from first principles | Sriniously · 31 | **PICK** | When a trace hits HTTP/API/auth basics |
| LLM Tracing & Observability | Arize AI · 20 | **PICK** | Observability trace rep (OTel/Langfuse) |
| LangGraph Tutorial Series | Mohamed Naji Aboo · 37 | **PICK** | pm-agent runtime trace (graph, checkpointer, interrupt) |
| How Does Vector Search Work? | Zilliz · 15 | **PICK** | RAG/retrieval trace |
| PostgreSQL | Hussein Nasser · 41 | **PICK** | pm-agent Postgres checkpointer / state rep |
| API Design | Postman · 13 | **PICK** | pm-agent FastAPI run-API trace |
| CI/CD/DevOps | Triet Bui Minh · 16 | **PICK** | M1 rebuild rep (your own WIF pipeline) |
| AIGP Certification Masterclass | Dr. David · 58 | **PARK** | Governance is your strength; only if you pursue AIGP |
| Microsoft Agent Framework (MAF) | Shweta Lodha · 13 | **PARK** | when a build or Capstone B needs Microsoft-estate depth |
| Generative AI on AWS | AWS Developers · 97 | **PARK** | when R41/R45 or Capstone B needs AWS depth |
| Generative AI Program | Stanford Online · 24 | **PARK** | — |
| Experts on AI: LLM Eval/Training | Microsoft for Startups · 20 | **PARK** | — |
| State space models, Mamba · Diffusion Model · Diffusion Generative Models (155) | various | **DROP** | Off-goal |
| Node | WittCode · 34 | **DROP** | Off-stack |
| Your own: **AI** (1,600) · **Programming** (285) · **cloud** (14) · **math** (21) · **information theory** (8) | you | **DROP — declare bankruptcy** | A 1,600-item watch-later list is a guilt store, not a curriculum. Stop adding; anything genuinely needed will resurface through a rep |

## 3. Newsletters (Gmail, Substack — ~55 publications seen, almost all **unread**)

Surveyed by sender over ~10 months; older pages not exhaustive. Topic for lesser-known handles is inferred from the publication name — flag any I misread.

**KEEP — 6 feeds, read only via the research radar, never as inbox homework**

| Publication | Why |
|---|---|
| The Neural Maze (`theneuralmaze`) | Production agents, hands-on, matches your stack |
| Decoding AI Magazine (`decodingaimagazine`; `decodingml` is the older same-author feed → drop it) | Production LLM/agent engineering |
| System Design One (`systemdesignone`) | System design, concept-level |
| ByteByteGo (`bytebytego`) | System design visuals for PROVE |
| Ken Huang (`kenhuangus`) | Agentic AI security — OWASP/CSA work you cite |
| Oliver Patel (`oliverpatel`) | Enterprise AI governance — your specialism |

**ASSET-ONLY** (keep the asset, drop the feed): `himanshuramchandani` (playbook PDF), `aiengineeringinsider` (handbook).

**DROP — daily/drip courses (guilt generators at bursty capacity):** `sdcourse`, `systemdr`, `aieworks`, `handsonk8s`, `aiinterviewprep`.

**DROP / ARCHIVE — everything else** (opinion, general AI news, VC, career, writing, unrelated): `opinionai`, `thatdevopsguy`, `llmsresearch`, `openclaw`, `aiagentssimplified`, `emergingai`, `aimadesimple0`, `hungrymindsdev`, `aistoriesweekly`, `techworldwithmilan`, `louisbouchard`, `todatabeyond`, `thepalindrome`, `theaiengineer`, `multimodalai`, `afterdinnerconversation`, `theagenticreview`, `moretoyourlife`, `paulgp`, `thevccorner`, `techaudienceaccelerator`, `generativeaitech`, `theaicorner1`, `refactoring`, `gregorojstersek`, `decodingml`, `buildml`, `awesomeneuron`, `srilaxmi`, `enterpriseaiweekly`, `natesnewsletter`, `nlpnews`, `the-weekender`, `youssefh`, `unstacked`, `aiweekly`, `fullstackagents`, `ziegler`, `michaeldsimmons`, `artofsaience`.

**Suggested Gmail setup (you do this once, ~10 min):** a filter `from:(theneuralmaze OR decodingaimagazine OR systemdesignone OR bytebytego OR kenhuangus OR oliverpatel)` → label `Reading/Keep`, skip inbox; unsubscribe the DROP list (or filter it to `Reading/Archive`, skip inbox). The research radar reads `Reading/Keep` for you and surfaces at most 3 items that touch your builds.

## 3b. Added 2026-10-19

| Resource | What it is | Verdict | Where it lands |
|---|---|---|---|
| *Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents* (arXiv 2609.00006, Jul 2026) | Source-code study of 11 coding harnesses; 7 subsystems, 29 design patterns, 18 recommendations, a 90-line minimal harness | **CORE** | LL10, and a lens for your own builds: map ARB's and PM's runtime onto its 7 subsystems |

## 3c. Added 2026-11-05 — Fanout and the prompt-lifecycle tools

**Fanout** (fanout.sh): mapped courses, interactive labs and daily paper notes. Introductory lessons are free; a Pro plan unlocks the full catalog (monthly, quarterly, annual or lifetime, with a regional discount). Facts as of 2026-11-05 [Verify at use].
**Decision:** Pro is not bought. Use the free lessons and labs; where the free tier stops, the Orchestrator writes our own material from primary sources (papers, vLLM / SGLang / llama.cpp docs) into the field guide or a rep — never a copy of Fanout's paid lessons.

| Fanout stream | What it is | Verdict | Where it lands |
|---|---|---|---|
| Inference Engineering course (~26 modules: setup and GPU basics, first serving, forward pass, KV cache, metrics, saturation, batching, PagedAttention, prefix caching and chunked prefill, quantisation, profiling, Triton, FlashAttention, compilation, speculative decoding, runtimes, parallelism, MoE, prefill–decode disaggregation, multi-LoRA) | Hands-on syllabus for serving models | **PICK** — the MODEL lane's primary hands-on source; kernels and profiling (modules 12–15) **PARK** (below architect depth) | R13, R53–R58 |
| System Design course (18 modules: foundations, APIs, data modelling, NoSQL and partitioning, caching, distributed coordination, storage engines, async and streams, search, analytics and sketches, realtime and feeds, geo, media and CDN, reliability, design cases, case studies) | Classic distributed-systems design | **PICK** — GROUND for what your builds don't teach (modules 03–08); cases 15–18 feed PROVE drills | R11, R12, R20, R59, R60; PROVE |
| Interactive labs (16) | Browser labs: tokenizer, sampling, KV cache, latency numbers, scale, model router, timeouts, eval confidence, memory, RAG chunking, agent control room, math decoder | **CORE** as 10-minute warm-ups before the paired rep | `NEXT.md` → Fanout warm-ups |
| AI Research course (12 modules: math, PyTorch, transformers, RL, LLM from scratch, research writing, fine-tuning, MLOps) | Research-engineer track | **SKIM** — overlaps Raschka (CORE); fine-tuning and MLOps stay PARK | R07 |
| ML Mathematics course · Math Decoder · notation library | Math for ML papers | **PICK** — only when a MODEL rep or a paper needs the math | MODEL reps |
| Daily papers · blog | Paper notes and essays | Radar source — logged, not learned | research radar |
| Open Robotics | Robotics track | **PARK** — off the architect path | — |

| Prompt-lifecycle tool | What it is | Verdict | Where it lands |
|---|---|---|---|
| DSPy (+ GEPA optimiser, `dspy.GEPA`) | Prompts and few-shot examples as parameters tuned against a metric; GEPA evolves prompts from a model's reflection on failures | **CORE** in T22 | T22, R42 |
| promptfoo | CLI for prompt and agent evals and red-team; acquired by OpenAI (announced 9 Mar 2026), stated to remain open source [Verify] | **CORE** in T21 | T21, T03 |
| PromptHub | Hosted prompt management (versions, environments, testing); free plan [Verify limits] | **PICK** in T20 | T20 |
| Langfuse prompt management | Prompt versions and labels in the Langfuse you already run for tracing | **CORE** in T20 | T20, R52 |

## 4. Existing curated material (kept, re-purposed)

| Item | Verdict |
|---|---|
| `learning/fieldguide/` — *Architect's Field Guide*, edition 1 (55 chapters, appendices A–I, PDF) | **CORE** — the consume step for every rep (L-23). Appendix E lists the further reading behind each chapter; anything there that is not in this registry earns time only through a rep (R7) |
| `Governance/_Agentic_Governance_Mastery/library/L0…L9` guides | **PICK** — the per-layer index you search when a gap needs a resource |
| Learning Ledgers in both repos | **CORE** — the Defend reps |
| `Learning_Methodology.md` (Socratic + consume-first) | **CORE** — how rep sessions are coached |
| DDIA 2nd ed. (Kleppmann & Riccomini, published Mar 2026) | **PICK** — distributed-systems GROUND; one chapter per gap |
| OWASP Top 10 for Agentic Applications (Dec 2025) | **CORE** — security GROUND rep; map each item to your controls |
