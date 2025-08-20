from fastapi import APIRouter, Request, Header
from models import Incident
from services import analyzer, slack, portia_plans
from utils import verify_github_signature

router = APIRouter()

@router.post("/ci")
async def ci_webhook(incident: Incident, request: Request, x_hub_signature_256: str = Header(None)):
    await verify_github_signature(request)

    analysis = analyzer.analyze_incident(incident)
    plan = await portia_plans.generate_plan(incident, analysis)
    slack.send_incident_alert(incident, analysis, plan)

    return {"status": "ci incident processed"}



