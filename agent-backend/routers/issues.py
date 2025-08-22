from fastapi import APIRouter, Request
from services import slack, portia_plans
from utils import verify_github_signature

router = APIRouter()

@router.post("/issues")
async def handle_important_issues(request: Request):
    await verify_github_signature(request)

    payload = await request.json()
    action = payload.get("action")
    issue = payload.get("issue", {})
    labels = {label["name"] for label in issue.get("labels", [])}

    important_labels = {"good first issue", "help wanted"}

    if action in ("opened", "reopened") and important_labels.intersection(labels):
        plan = await portia_plans.generate_plan(
            incident=None,
            analysis=None,
            is_issue=True,
            issue_data={
                "title": issue.get("title"),
                "body": issue.get("body")
            }
        )
        slack.send_important_issue_alert(
            issue={
                "title": issue.get("title"),
                "html_url": issue.get("html_url", "N/A"),
                "body": issue.get("body", "")
            },
            plan=plan
        )
        slack.send_message(plan)

    return {"status": "Issue processed"}
