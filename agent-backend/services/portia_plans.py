from portia import Portia
from config import GEMINI_API_KEY
from models import Incident, Analysis

PROMPT_TEMPLATE = """
You are an AI assistant tasked with analyzing software incidents and generating clear, actionable plans to resolve them. The output should be formatted as a message fit for Slack notifications.

Incident Summary:
{summary}

Details:
Source: {source}
Error Message: {error_message}
Root Cause: {root_cause}

Please provide a step-by-step plan to resolve this incident effectively.
"""

async def generate_plan(incident: Incident, analysis: Analysis):
    agent = Portia(api_key=GEMINI_API_KEY)

    prompt = PROMPT_TEMPLATE.format(
        summary=analysis.summary,
        source=incident.source,
        error_message=incident.error_message,
        root_cause=analysis.root_cause or "Not determined"
    )
    
    plan = await agent.plan(goal=prompt, context={})
    return plan
