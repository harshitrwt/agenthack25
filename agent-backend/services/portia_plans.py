# from services.portia_instance import portia_agent
# from models import Incident, Analysis

# INCIDENT_PROMPT_TEMPLATE = """ 
# You are an incident response assistant.
# Incident Summary: {summary}
# Source: {source}
# Error Message: {error_message}
# Root Cause: {root_cause}

# Generate a clear remediation plan step by step.
# """

# ISSUE_PROMPT_TEMPLATE = """ 
# You are a GitHub issue triage assistant.
# Issue Title: {title}
# Issue Body: {body}

# Suggest a plan to resolve this issue step by step.
# """

# async def generate_plan(incident: Incident, analysis: Analysis, is_issue: bool = False, issue_data: dict = None):
#     if is_issue and issue_data:
#         prompt = ISSUE_PROMPT_TEMPLATE.format(
#             title=issue_data.get("title", "No title provided"),
#             body=issue_data.get("body", "No description provided")
#         )
#     else:
#         prompt = INCIDENT_PROMPT_TEMPLATE.format(
#             summary=analysis.summary,
#             source=incident.source,
#             error_message=incident.error_message,
#             root_cause=analysis.root_cause or "Not determined"
#         )

#     plan = await portia_agent.plan(goal=prompt, context={})
#     return plan



from services.portia_instance import portia_agent
from models import Incident, Analysis

INCIDENT_PROMPT_TEMPLATE = """
You are an assistant generating an incident plan.
Summary: {summary}
Source: {source}
Error: {error_message}
Root Cause: {root_cause}
"""

ISSUE_PROMPT_TEMPLATE = """
You are an assistant analyzing a GitHub issue.
Title: {title}
Body: {body}
"""

async def generate_plan(incident: Incident = None, analysis: Analysis = None,
                       is_issue: bool = False, issue_data: dict = None):
    if is_issue and issue_data:
        prompt = ISSUE_PROMPT_TEMPLATE.format(
            title=issue_data.get("title", "No title provided"),
            body=issue_data.get("body", "No description provided")
        )
    else:
        prompt = INCIDENT_PROMPT_TEMPLATE.format(
            summary=analysis.summary if analysis else "N/A",
            source=incident.source if incident else "N/A",
            error_message=incident.error_message if incident else "N/A",
            root_cause=analysis.root_cause if analysis and analysis.root_cause else "Not determined"
        )

   
    plan_result = portia_agent.plan(prompt)

    if plan_result is None:
        
        return "⚠️ Failed to generate a plan (Portia returned None). Check your LLM/API key setup."

    
    return str(plan_result)
