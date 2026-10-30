# R04 · TRACE + DEFEND · Why one agent is CRITICAL and the other MEDIUM

**Lane:** OWN · **Repo:** ARB · **Time:** 35–40 min
**📖 Read (consume):** [Ch13 Fleet-first risk tiering](../fieldguide/risk-tiering.html) (all), [Ch14 The control as a contract](../fieldguide/control-as-contract.html#what) §14.1–14.2 and [Ch15 The lifecycle and its gates](../fieldguide/lifecycle-gates.html#gate) §15.3–15.5 — after Predict, before Run. [Ch13 Prove it](../fieldguide/risk-tiering.html#prove) is extra Defend practice.

## Predict (5 min)
Without looking: what properties of `customer_service_ops` make it CRITICAL? What would have to change for `knowledge_advisor` (MEDIUM) to become HIGH? What does "fleet-first" mean for how a control declares where it applies?
> _Predictions:_

## Run (5 min)
`make demo-regate` (or `uv run python -m aicoe.cli demo regate`) (knowledge_advisor copy with action_class raised → tier re-derived → gate BLOCKED). Note which axis moved and which controls got pulled in.
> _Observed:_

## Read (15 min)
1. `src/aicoe/governance/tiering/` (228 lines, read it all) — how is the tier derived? Highest-wins or average?
2. One catalog control in root `governance/catalog/` — find `min_tier` and `applies_when`. Explain them in one line each.
3. `src/aicoe/governance/gate/` — skim: what makes the gate say BLOCKED?
> _Answers:_

## Defend (10 min)
Ledger **P2** self-test, cold → compare → grade (same protocol as R02).
Then one more, cold (field guide Appendix G, F-03): **Is the CRITICAL pair clause ever decisive with today's axes? What change would make it so?** Check your answer against ARB `governance/taxonomy/tiers.yaml`.
> _Answers / grade:_
