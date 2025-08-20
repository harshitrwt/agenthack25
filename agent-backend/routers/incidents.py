from fastapi import APIRouter, Request
from services import slack

router = APIRouter()

@router.post("/issues")
async def handle_important_issues(request: Request):
    payload = await request.json()
    action = payload.get("action")
    issue = payload.get("issue")
    labels = [label["name"] for label in issue.get("labels", [])]

    important_labels = {"needs-attention", "high-priority"}

    if action in ("opened", "reopened") and important_labels.intersection(labels):
        title = issue.get("title")
        url = issue.get("html_url")
        message = f"Important Issue {action}: {title}\n{url}"
        slack.send_message(message)

    return {"status": "issue processed"}
