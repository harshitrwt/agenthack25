from portia import Portia
from config import GEMINI_API_KEY
from models import Incident, Analysis

# Base prompt template for incidents
INCIDENT_PROMPT_TEMPLATE = """
You are an AI assistant tasked with analyzing software incidents and generating clear, actionable plans to resolve them. The output should be formatted as a message fit for Slack notifications.

Incident Summary:
{summary}

Details:
Source: {source}
Error Message: {error_message}
Root Cause: {root_cause}

Please provide a step-by-step plan to resolve this incident effectively.
"""

# Optional: Separate prompt template for new issues
ISSUE_PROMPT_TEMPLATE = """
You are an AI assistant tasked with analyzing newly created GitHub issues and generating clear, concise summaries or escalation plans. The output should be formatted as a message fit for Slack notifications.

Issue Title:
{title}

Issue Body:
{body}

Please identify the importance and next steps for this issue.
"""

async def generate_plan(incident: Incident, analysis: Analysis, is_issue: bool = False, issue_data: dict = None):
    agent = Portia(api_key=GEMINI_API_KEY)

    if is_issue and issue_data:
        # Format prompt for issues
        prompt = ISSUE_PROMPT_TEMPLATE.format(
            title=issue_data.get("title", "No title provided"),
            body=issue_data.get("body", "No description provided")
        )
    else:
        # Format prompt for incidents/failures
        prompt = INCIDENT_PROMPT_TEMPLATE.format(
            summary=analysis.summary,
            source=incident.source,
            error_message=incident.error_message,
            root_cause=analysis.root_cause or "Not determined"
        )
    
    plan = await agent.plan(goal=prompt, context={})
    return plan
