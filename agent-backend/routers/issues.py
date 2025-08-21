from fastapi import APIRouter, Request
from services import slack, portia_plans
from utils import verify_github_signature


router = APIRouter()

@router.post("/webhook/issues")
async def handle_important_issues(request: Request):
    await verify_github_signature(request)

    payload = await request.json()
    action = payload.get("action")
    issue = payload.get("issue", {})
    labels = {label["name"] for label in issue.get("labels", [])}

    important_labels = {"needs-attention", "high-priority"}

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
        slack.send_message(plan)


    return {"status": "issue processed"}
