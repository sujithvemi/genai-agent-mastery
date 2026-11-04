# R25 · OWN · GF-1 — Microsoft's Agent Governance Toolkit, through your own build

**Lane:** OWN (governance frameworks track) · **Repo:** aicoe-reference-build (ARB) · **Time:** 40 min · **Claude needed:** no
**Why now:** "Why not just use Microsoft's toolkit?" is the first build-vs-buy question a CISO, an architect or an interviewer will ask. Your build already ran the experiment; this rep makes the answer yours.
**📖 Read (consume):** [Ch47 Microsoft AGT through your build](../fieldguide/agt-through-your-build.html#model) §47.2–47.6 — after Step 0. Open [§47.7 The mapping table](../fieldguide/agt-through-your-build.html#map) only after you have filled in your own in Step 3. Platform facts in the chapter are dated 2026-10-21; per D63, quote the version your spike pinned, not the latest release.

## Step 0 — Predict (5 min)
Without opening anything: what would you expect a vendor OSS toolkit's policy language to handle well, and where would you expect it to struggle compared with Rego? If it could only express *some* of your controls, how would you wire it so that it could never weaken enforcement?
> _Predictions:_

## Step 1 — AGT's model (10 min)
Read the toolkit's own README/overview (github.com/microsoft/agent-governance-toolkit) — skim for its **components** and its **policy model**. Write 5 lines: what the parts are, which one is the policy engine, what the policy language looks like.
> _AGT in 5 lines:_

## Step 2 — How your build tested it (15 min)
1. `docs/architecture/AGT_INTEROP.md` — read the **Verdict**, **How it is wired** and **The gaps, measured (G1–G7)**.
2. `spikes/agt/README.md` and `spikes/agt/policies/tool_call.yaml` — what does one AGT policy look like next to `governance/policies/rego/tool_call.rego`?
3. Run `make agt-parity` and watch it pass (no `make`? run `uv sync --project spikes/agt --frozen` then `uv run pytest -q tests/test_policy_parity_agt.py`).
Answer:
- Why does AGT run in **its own environment**, and why does its adapter live in `tests/` rather than the package?
- Why is each AGT policy written **deny-by-default with one positive allow** rule? Use G1, G3 or G5 in your answer.
- Why can't CTL-0002 (refund ≤ order total) be expressed? (G1)
> _Answers:_

## Step 3 — The mapping table (5 min)
| AGT concept | Your component (file) | equal / stronger / weaker / absent |
|---|---|---|
| Policy engine + YAML policies | `platform/policy/` (OPA, Cedar) behind `PolicyEngine` | |
| Agent identity / trust | `enforcement/tokens.py`, `platform/identity` | |
| Audit / evidence | `evidence/` | |
| (add any other AGT component you found in Step 1) | | |

## Step 4 — Defend (5 min)
Write the 3-sentence answer to a stakeholder's "why not just use Microsoft's toolkit?" that obeys the **D63 wording rule** (versioned, factual, reproducible). Then: when *would* you recommend AGT?
> _Your answer:_

## Done when
- [ ] Mapping table filled; answer obeys D63
- [ ] Save the table + answer as `learning/frameworks/AGT.md` (create the folder) — this is your GF-L1 output
- [ ] LOG line + 1–2 cards
