from models import Incident, Analysis
from utils import send_slack_message
import os

SLACK_INCIDENTS_CHANNEL = os.getenv("SLACK_INCIDENTS_CHANNEL")
SLACK_ISSUES_CHANNEL = os.getenv("SLACK_ISSUES_CHANNEL")


def send_incident_alert(incident: Incident, analysis: Analysis, plan: str, include_logs: bool = True):
    log_snippet = ""
    if include_logs and incident.metadata:
        try:
            import json
            logs_preview = json.dumps(incident.metadata, indent=2)[:800]
            log_snippet = f"\n*Logs Preview:*\n```{logs_preview}...```"
        except Exception:
            pass

    body = f"""
*Source:* {incident.source or "N/A"}
*Error:* {incident.error_message or "N/A"}
*Analysis:* {analysis.summary or "No summary generated"}
*Root Cause:* {analysis.root_cause or "Not determined"}
{log_snippet}
    """

    send_slack_message(SLACK_INCIDENTS_CHANNEL, "🚨 Incident Alert", body)


def send_important_issue_alert(issue: dict, plan: str = "No contributor note generated"):
    title = issue.get("title") or "No title"
    url = issue.get("html_url") or "No URL"
    body_text = issue.get("body") or "No description"

    body = f"""
*Title:* {title}
*URL:* {url}
*Details:* {body_text}
    """

    send_slack_message(SLACK_ISSUES_CHANNEL, "⚠️ Issue Alert", body)
