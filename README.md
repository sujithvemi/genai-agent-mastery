# GenAI Agent Mastery - GCP Track
Hands-on, production-grade build track for enterprise Agentic AI on GCP (ADK/Gemini Enterprise Agent Platform).

## Structure
- `agents/` - one directory per ADK agent (`adk create agents/<name>`), starting with `hello_agent`
- `infra/terraform` - reproducible infra
- `docs/milestones/` - a short defend-log per milestone
- `docs/SOP.md`

## Setup
\`\`\`bash
uv sync
uv run pre-commit install
uv run pre-commit autoupdate
\`\`\`
