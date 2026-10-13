# R01 · TRACE · A refund, from the model's tool call to the evidence log

**Lane:** OWN · **Repo:** aicoe-reference-build (branch `adk-2.5.0`, as checked out) · **Time:** 30–40 min · **Claude needed:** no (optional check after)
**Why first:** this one path *is* your governance story. Every demo, client question and interview answer about the build hangs off it.

## Step 0 — Predict (5 min, before opening any file)
Write your answers here, from memory, even if guessing:

1. List the hops a call to `issue_refund` takes, from the ADK agent to the moment money "moves" (fake payments). How many hops? Name them.
2. At which hop is a refund over the limit / without approval **stopped**? Who decides — Python code, the model, or a policy engine?
3. What gets written to the evidence log for (a) an allowed refund, (b) a denied one? Anything written *before* the decision?
4. If the evidence log is unwritable (disk full), does the refund happen?

> _Your predictions:_
>

## Step 1 — Run it first (5 min)
In the ARB repo: `make demo-before-after` — read the two columns (ungoverned vs governed). Note one refund that moved money ungoverned and was refused governed, and the control ID that refused it.

> _Refund + control ID:_

## Step 2 — Read in order (20 min). One question per stop; answer in a line.

| # | Stop | Question |
|---|---|---|
| 1 | `src/aicoe/agents/tools.py` → `issue_refund` (~line 305) | What does the ADK-facing function actually do with its arguments? What does it *not* do? |
| 2 | `src/aicoe/chokepoint.py` → `ToolChokepoint.call` (~line 170) | What decides between `_call_ungoverned` and `_call_governed`? |
| 3 | `src/aicoe/chokepoint.py` → `_call_governed` (~line 247) | In what order do *decide*, *write evidence*, and *execute* happen? Why that order? |
| 4 | `src/aicoe/chokepoint.py` → `EvidenceUnavailable` (~line 95) | Which invariant is this, and why does it fail **closed**? |
| 5 | `src/aicoe/enforcement/plane.py` → `EnforcementPlane.decide` (~line 885) | Skim only: list the *kinds* of checks you see before a decision is returned. |
| 6 | `src/aicoe/evidence/writer.py` → `EvidenceWriter` (~line 114) + `evidence/chain.py` → `record_digest` | What links one record to the previous one? |

> _Answers 1–6:_

## Step 3 — Close (5 min)
- **From memory**, draw the path (boxes + arrows, paper is fine). Photo/sketch optional.
- Compare against your Step 0 predictions: **what did you get wrong?** That line is the most valuable thing in this file.

> _Wrong predictions:_

## Done when
- [ ] Path drawn from memory with ≥ 5 correct hops
- [ ] You can say in one sentence why evidence is written where it is
- [ ] `LOG.md` line + 1–2 cards in `cards/REVIEW.md` + rate `chokepoint`, `plane`, `evidence writer` in `maps/comprehension_map.md`
