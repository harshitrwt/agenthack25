from fastapi import APIRouter
from models import Incident
from services import analyzer, slack, portia_plans

router = APIRouter()

@router.post("/error")
async def ingest_error(incident: Incident):
    # Run analysis
    analysis = analyzer.analyze_incident(incident)

    # Generate Portia plan
    plan = portia_plans.generate_plan(incident, analysis)

    # Send to Slack
    slack.send_incident_alert(incident, analysis, plan)

    return {"status": "ok", "analysis": analysis.summary}
