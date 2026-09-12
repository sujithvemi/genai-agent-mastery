from datetime import UTC, datetime

from google.adk.agents import Agent


def get_current_time() -> dict[str, str]:
    """
    Returns the current UTC time in ISO 8601 format.
    """
    return {"utc_time": datetime.now(UTC).isoformat()}


root_agent = Agent(
    name="hello_agent",
    model="gemini-3.5-flash",
    description="M0 proof-of-life agent: confirms the ADK + GCP wiring works end to end.",
    instruction=(
        "You are a minimal test agent. When asked the time, call get_current_time "
        "and report it back clearly. Otherwise, respond briefly and honestly that "
        "you are a scaffold agent used to validate deployment planning."
    ),
    tools=[get_current_time],
)
