# import hmac
# import hashlib
# from fastapi import Request, HTTPException
# from config import GITHUB_WEBHOOK_SECRET

# async def verify_github_signature(request: Request):
#     signature = request.headers.get("X-Hub-Signature-256")
#     if signature is None:
#         raise HTTPException(status_code=400, detail="Missing signature")

#     body = await request.body()
#     mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), body, hashlib.sha256)
#     expected_signature = "sha256=" + mac.hexdigest()
#     if not hmac.compare_digest(expected_signature, signature):
#         raise HTTPException(status_code=401, detail="Invalid signature")
import hmac
import hashlib
from fastapi import Request, HTTPException
from config import GITHUB_WEBHOOK_SECRET
from slack_sdk import WebClient
import os

# --- GitHub webhook signature verification ---
async def verify_github_signature(request: Request):
    signature = request.headers.get("X-Hub-Signature-256")
    if signature is None:
        raise HTTPException(status_code=400, detail="Missing signature")

    body = await request.body()
    mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), body, hashlib.sha256)
    expected_signature = "sha256=" + mac.hexdigest()
    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

# --- Slack Helper ---
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

def send_slack_message(channel: str, title: str, body: str):
    """
    Send a clean, consistently formatted Slack message.
    """
    message = f"*{title}*\n{body}"
    client.chat_postMessage(channel=channel, text=message)
