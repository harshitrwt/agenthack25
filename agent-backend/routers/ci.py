from fastapi import APIRouter
from models import Incident
from services import analyzer, slack, portia_plans

router = APIRouter()

@router.post("/ci")
async def ci_webhook(incident: Incident):
    # Analyze
    analysis = analyzer.analyze_incident(incident)

    # Create Portia plan
    plan = portia_plans.generate_plan(incident, analysis)

    # Notify Slack
    slack.send_incident_alert(incident, analysis, plan)

    return {"status": "ci incident processed"}
