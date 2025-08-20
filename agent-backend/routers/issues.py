from fastapi import APIRouter, Request, Header
from models import Incident
from services import analyzer, slack, portia_plans

router = APIRouter()

@router.post("/ci")
async def ci_webhook(incident: Incident, x_github_signature_256: str = Header(None)):
    # TODO: validate webhook secret here for security
    analysis = analyzer.analyze_incident(incident)
    plan = portia_plans.generate_plan(incident, analysis)
    slack.send_incident_alert(incident, analysis, plan)
    return {"status": "ci incident processed"}
