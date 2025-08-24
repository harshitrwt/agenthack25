from services.portia_instance import portia_agent
from models import Incident, Analysis


ISSUE_PROMPT_TEMPLATE = """
You are an assistant helping classify GitHub issues.
Read the following issue and return:
- A short **summary** of the issue
- A note on whether this is good for *new contributors* or needs *experienced contributors*

Issue Title: {title}
Issue Body: {body}

Respond in plain text. Do not use JSON or code blocks.
"""

INCIDENT_PROMPT_TEMPLATE = """
You are an assistant helping engineers handle software incidents.
Analyze the following incident and provide:
- A short **summary** of what happened
- A possible **root cause**
- A note for contributors on how to proceed (new vs experienced)

Incident Summary: {summary}
Source: {source}
Error Message: {error_message}
Root Cause: {root_cause}

Respond in plain text. Do not use JSON or code blocks.
"""



def _serialize_for_slack(ai_obj) -> str:
    """
    Convert AI JSON response into a Slack-friendly message.
    Removes raw plan dumps and instead shows summary + contributor note + meta.
    """
    import json

    try:
        dump = ai_obj if isinstance(ai_obj, dict) else ai_obj.model_dump()
        summary = dump.get("summary", "No summary for this one.")
        contributor_note = dump.get("contributor_note", "")
        meta = dump.get("meta", {})

        priority = meta.get("priority", "unspecified")
        next_action = meta.get("next_action", "Not provided")

        message = (
            f"*Summary*: {summary}\n"
            f"*Note*: {contributor_note}\n"
            
        )
        return message
    except Exception as e:
      
        return f"*AI Output (raw)*\n```{json.dumps(str(ai_obj), indent=2)}```\n_Error_: {e}"


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
            raw_result = portia_agent.plan(prompt)
            if raw_result:
                
                if isinstance(raw_result, str):
                    return raw_result.strip()
                if hasattr(raw_result, "content"):
                    return str(raw_result.content).strip()
                return str(raw_result).strip()
        except Exception as e:
            last_err = e

    fallback = "*Contributor Note generation failed.*\n"
    if last_err:
        fallback += f"_Reason_: {last_err}"
    else:
        fallback += "_Reason_: LLM returned no content."
    fallback += "\n_Suggested next step_: Triage manually and retry."
    return fallback
