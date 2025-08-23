from slack_sdk import WebClient
from dotenv import load_dotenv
import os
from models import Incident, Analysis

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_INCIDENTS_CHANNEL = os.getenv("SLACK_INCIDENTS_CHANNEL")
SLACK_ISSUES_CHANNEL = os.getenv("SLACK_ISSUES_CHANNEL")

client = WebClient(token=SLACK_BOT_TOKEN)

def send_message(text: str, channel: str):
    client.chat_postMessage(channel=channel, text=text)

def send_incident_alert(incident: Incident, analysis: Analysis, plan: str, include_logs: bool = True):
    log_snippet = ""
    if include_logs and incident.metadata:
        try:
            import json
            logs_preview = json.dumps(incident.metadata, indent=2)[:800]
            log_snippet = f"\n*Logs Preview:*\n```{logs_preview}...```"
        except Exception:
            pass

    message = f"""
*🚨 Incident Alert*
*Source:* {incident.source or "N/A"}
*Error:* {incident.error_message or "N/A"}
*Analysis:* {analysis.summary or "No summary generated"}
*Root Cause:* {analysis.root_cause or "Not determined"}
*Contributor Note:* {plan or "AI did not generate a contributor note"}
{log_snippet}
    """
    send_message(message, SLACK_INCIDENTS_CHANNEL)


def send_important_issue_alert(issue: dict, plan: str = "AI did not generate a note"):
    title = issue.get("title") or "No title"
    url = issue.get("html_url") or "No URL"
    body = issue.get("body") or "No description"

    message = f"""
*⚠️ Issue Alert*
*Title:* {title}
*URL:* {url}
*Details:* {body}
*Contributor Note:* {plan}
    """
    send_message(message, SLACK_ISSUES_CHANNEL)
