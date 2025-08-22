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

def send_incident_alert(incident: Incident, analysis: Analysis, plan: str):
    message = f"""
*🚨 Incident Alert*
*Source:* {incident.source}
*Error:* {incident.error_message}
*Analysis:* {analysis.summary}
*Root Cause:* {analysis.root_cause}
*Plan:* {plan}
    """
    send_message(message, SLACK_INCIDENTS_CHANNEL)

def send_important_issue_alert(issue: dict, plan: str = "No plan provided"):
    title = issue.get("title", "No title")
    url = issue.get("html_url", "No URL")
    body = issue.get("body", "No description")

    message = f"""
*⚠️ Issue Alert*
*Title:* {title}
*URL:* {url}
*Details:* {body}
*Plan:* {plan}
    """
    send_message(message, SLACK_ISSUES_CHANNEL)
