from services.portia_instance import portia_agent
from models import Incident, Analysis

INCIDENT_PROMPT_TEMPLATE = """
You are a planning assistant.
Create a concrete, step-by-step remediation plan for the software incident below.

Incident Summary: {summary}
Source: {source}
Error Message: {error_message}
Root Cause: {root_cause}

Return a clear plan with numbered steps and short justifications.
"""

ISSUE_PROMPT_TEMPLATE = """
You are a planning assistant.
Analyze the GitHub issue below and produce a short, actionable plan (1–5 steps)
including priority, owners (if guessable), and next actions.

Issue Title: {title}
Issue Body: {body}

Return a clear plan with numbered steps and short justifications.
"""

def _serialize_plan_for_slack(plan_obj) -> str:
    """
    Convert Portia plan object into a readable Slack message.
    Falls back gracefully if structure is unexpected.
    """
   
    try:
        
        dump = plan_obj.model_dump()  
        steps = []
        raw_steps = (
            dump.get("steps")
            or (dump.get("plan") or {}).get("steps")
            or []
        )
        for idx, s in enumerate(raw_steps, 1):
            name = s.get("name") or s.get("step_name") or "Step"
            desc = s.get("description") or s.get("task") or ""
            steps.append(f"{idx}. *{name}*: {desc}".strip())
        if steps:
            return "*Plan*\n" + "\n".join(steps)
        import json
        return "*Plan (raw)*\n```" + json.dumps(dump, indent=2) + "```"
    except Exception:
        return f"*Plan*\n{str(plan_obj)}"

async def generate_plan(
    incident: Incident = None,
    analysis: Analysis = None,
    is_issue: bool = False,
    issue_data: dict = None
) -> str:
    if is_issue and issue_data:
        prompt = ISSUE_PROMPT_TEMPLATE.format(
            title=issue_data.get("title", "No title provided"),
            body=issue_data.get("body", "No description provided"),
        )
    else:
        prompt = INCIDENT_PROMPT_TEMPLATE.format(
            summary=(analysis.summary if analysis else "N/A"),
            source=(incident.source if incident else "N/A"),
            error_message=(incident.error_message if incident else "N/A"),
            root_cause=(analysis.root_cause if analysis and analysis.root_cause else "Not determined"),
        )

    
    last_err = None
    for _ in range(2):
        try:
            plan_result = portia_agent.plan(prompt)  
            if plan_result:
                return _serialize_plan_for_slack(plan_result)
        except Exception as e:
            last_err = e

    
    fallback = "*Plan generation failed.*\n"
    if last_err:
        fallback += f"_Reason_: {last_err}"
    else:
        fallback += "_Reason_: LLM returned no content."
    fallback += "\n_Suggested next step_: Triage manually and retry."
    return fallback
