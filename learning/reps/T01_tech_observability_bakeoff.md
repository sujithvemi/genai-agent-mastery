# T01 · TECH · Observability bake-off, part 1 — Langfuse vs Arize Phoenix

**Lane:** TECH (low priority / bonus slot) · **Repo:** genai-agent-mastery (your hand-written code) · **Time:** 60–90 min · **Needs:** Docker Desktop running
**📖 Read (consume):** [Ch31 §31.3 OpenTelemetry for agents](../fieldguide/observability-agentops.html#otel) and [§31.9 AgentOps tools](../fieldguide/observability-agentops.html#tools), plus [Ch46 §46.2](../fieldguide/tool-landscape.html#map) — before Step 2. Check current free-tier terms yourself [Verify].

## Step 0 — Predict (5 min)
Your ARB already sends OpenTelemetry traces to Langfuse. Before starting: what does a trace of one agent turn contain (spans for what?), and what would make one observability tool better than another for an *agent* rather than a web app?
> _Predictions:_

## Step 1 — Target (10 min)
Use `agents/hello_agent`. If it has only `get_current_time`, add one more tool (e.g. `lookup_order(order_id)` returning fake data) so traces show a tool call.

## Step 2 — OpenTelemetry once (15 min; skip if you did BT09 and reuse it)
Instrument the agent with OpenTelemetry using the GenAI semantic conventions (ADK and OpenInference both offer instrumentation; check the current docs [Verify]). Export OTLP to an endpoint you can switch by environment variable. This is the point of the lab: **instrument once, send anywhere**.

## Step 3 — Langfuse (20 min)
Run Langfuse self-hosted with its Docker Compose quickstart. Point OTLP at it. Run 5 conversations. Find: the tool-call span, token usage, latency per span, cost.
> _What it showed / what it didn't:_

## Step 4 — Arize Phoenix (20 min)
Run Phoenix locally (`pip install arize-phoenix` or its Docker image). Point the same OTLP export at it. Same 5 conversations.
> _What it showed / what it didn't:_

## Step 5 — Compare (10 min)
Create `labs/observability/COMPARISON.md` with one row per tool: setup time · trace view quality for agents · evals built in? · prompt management? · self-host vs SaaS · cost model · when you'd pick it. (T02 adds LangSmith and Datadog.)

## Done when
- [ ] Same traces visible in both tools from one instrumentation
- [ ] COMPARISON.md has two rows
- [ ] LOG line; tick T01 in NEXT.md
