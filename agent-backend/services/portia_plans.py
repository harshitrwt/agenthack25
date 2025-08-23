from services.portia_instance import portia_agent
from models import Incident, Analysis


INCIDENT_PROMPT_TEMPLATE = """
You are a helpful assistant.
Analyze the following software incident and provide:

1. A short summary of what might have happened (one or two sentences).
2. A contributor note:
   - If it sounds simple (docs, typo, config), suggest it's good for new contributors.
   - If it sounds harder (infra, logic, CI failures), suggest it's better for experienced contributors.

Incident Summary: {summary}
Source: {source}
Error Message: {error_message}


Return ONLY valid JSON:
{{
  "summary": "...",
  "contributor_note": "...",
}}
"""


ISSUE_PROMPT_TEMPLATE = """
You are a helpful assistant.
Analyze the following GitHub issue and provide:

1. A short summary of what the issue is about (one or two sentences).
2. A contributor note:
   - If it sounds simple (docs, typo, config), suggest it's good for new contributors.
   - If it sounds harder (infra, logic, CI failures), suggest it's better for experienced contributors.

Issue Title: {title}
Issue Body: {body}

Return ONLY valid JSON:
{{
  "summary": "...",
  "contributor_note": "...",
}}
"""


def _serialize_for_slack(ai_obj) -> str:
    """
    Convert AI JSON response into a Slack-friendly message.
    Removes raw plan dumps and instead shows summary + contributor note + meta.
    """
    import json

    try:
        dump = ai_obj if isinstance(ai_obj, dict) else ai_obj.model_dump()
        summary = dump.get("summary", "No summary provided.")
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
                return _serialize_for_slack(raw_result)
        except Exception as e:
            last_err = e

    fallback = "*Summary Generation in Queue...*\n"
    if last_err:
        fallback += f"_Reason_: {last_err}"
    else:
        fallback += "_Reason_: LLM returned no content."
    fallback += "\n_Suggested next step_: Triage manually and retry."
    return fallback
