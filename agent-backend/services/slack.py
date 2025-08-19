from slack_sdk import WebClient
from config import SLACK_BOT_TOKEN, SLACK_CHANNEL
from models import Incident, Analysis

client = WebClient(token=SLACK_BOT_TOKEN)

def send_incident_alert(incident: Incident, analysis: Analysis, plan):
    message = f"""
🚨 *Incident Alert*
*Source:* {incident.source}
*Error:* {incident.error_message}
*Analysis:* {analysis.summary}
*Root Cause:* {analysis.root_cause}
*Plan:* {plan}
    """
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
