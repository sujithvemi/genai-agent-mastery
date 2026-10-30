# BT01 · OWN · Rebuild — the Python toolchain both builds stand on

**Lane:** OWN · Rebuild (build-tool lab) · **Where:** `genai-agent-mastery/labs/build-tools/toolchain/` · **Time:** 45 min · **Claude:** answers questions only, writes nothing
**📖 Read (consume):** [Ch7 The chassis](../fieldguide/chassis-seams-tests.html#why) §7.1 and §7.7–7.9 — why the builds' toolchain is strict (tests that guard the governance, falsifiers, pinned baselines). The tools' own docs stay the source for Step 1.

## Step 0 — Predict (3 min)
Both builds run `make check` = ruff + mypy strict + pytest. Before starting: what does each of those catch that the others don't? Why would a governance build pin mypy to *strict*?
> _Predictions:_

## Step 1 — Build it yourself (30 min, from the official docs only)
1. `uv init --package minichoke` inside `labs/build-tools/toolchain/`; `uv add --dev ruff mypy pytest pytest-cov pre-commit`.
2. Write `src/minichoke/core.py`: a typed function `decide(tool: str, amount: float, limit: float) -> bool` and a `Decision` dataclass.
3. Write 3 tests in `tests/` (allow, deny, boundary) and run `uv run pytest --cov`.
4. Configure ruff and `mypy --strict` in `pyproject.toml`; make both pass.
5. Add `.pre-commit-config.yaml` with ruff + mypy hooks; `uv run pre-commit install`; commit once and watch the hooks run.
6. Add a `Makefile` with `check: lint type test` (or a `check.ps1` if make isn't on your machine).
> _What tripped you up:_

## Step 2 — Diff against the build (10 min)
Open ARB's `pyproject.toml`, `Makefile` and `.pre-commit-config.yaml`. List 3 things Claude Code configured that you didn't, and why each is there (look for: mypy strictness overrides per module, ruff rule sets, pytest markers like `live`, coverage thresholds, `uv sync --frozen`).
> _Diff list:_

## Done when
- [ ] `make check` (or your script) passes in your package
- [ ] Diff list has 3 items with a reason each
- [ ] LOG line; tick BT01 in NEXT.md; rate the toolchain row in `maps/comprehension_map.md`
