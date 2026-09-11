# Standard Operating Procedure

## Per-milestone workflow
1. Create/extend the relevant agent under `agents/`, or infra under `infra/terraform/`
2. Design choices get justified (Socratically, with the coach) before being written down
3. Log key design choices + why in `docs/milestones/M<n>.md` - feeds M0.6-style defend checkpoints and future teach-to-D writeups
4. Update Notion (Modules & Tasks) status as the task completes
5. Commit referencing the milestone, e.g. `M0.3: trivial local ADK agent with get_current_time tool`

## Tooling
- Env/deps: `uv` - `uv sync`, `uv run <cmd>`
- Lint/format: `uv run ruff check --fix.` / `uv run ruff format .`.
- Types: `uv run mypy .` (strict, outside `infra/`).
- New agent: `adk create agents/<agent_name>`.

## Secrets discipline
- Real values only in an agent's own `.env`, never committed
- `.env.example` documents variable names, no values
- GCP auth via Application Default Credentials or (from M0.5) a per-agent service account - never a personal API key or a downloaded key file in the repo.
