# R04 · TRACE + DEFEND · Why one agent is CRITICAL and the other MEDIUM

**Lane:** OWN · **Repo:** ARB · **Time:** 35–40 min

## Predict (5 min)
Without looking: what properties of `customer_service_ops` make it CRITICAL? What would have to change for `knowledge_advisor` (MEDIUM) to become HIGH? What does "fleet-first" mean for how a control declares where it applies?
> _Predictions:_

## Run (5 min)
`make demo-regate` (knowledge_advisor copy with action_class raised → tier re-derived → gate BLOCKED). Note which axis moved and which controls got pulled in.
> _Observed:_

## Read (15 min)
1. `src/aicoe/governance/tiering/` (228 lines, read it all) — how is the tier derived? Highest-wins or average?
2. One catalog control in root `governance/catalog/` — find `min_tier` and `applies_when`. Explain them in one line each.
3. `src/aicoe/governance/gate/` — skim: what makes the gate say BLOCKED?
> _Answers:_

## Defend (10 min)
Ledger **P2** self-test, cold → compare → grade (same protocol as R02).
> _Answers / grade:_
