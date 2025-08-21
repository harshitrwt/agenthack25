from fastapi import APIRouter, Request, Header, HTTPException
from models import Incident, Analysis
from services import analyzer, slack, portia_plans
from utils import verify_github_signature

router = APIRouter()

@router.post("/ci")
async def ci_webhook(request: Request, x_hub_signature_256: str = Header(None)):
    await verify_github_signature(request)

    event_type = request.headers.get("X-GitHub-Event")
    
    if event_type == "ping":
        
        return {"msg": "pong"}

    if event_type not in ["workflow_run", "workflow_job"]:
        
        return {"msg": f"Ignored event type: {event_type}"}

    payload = await request.json()
    
    
    incident_data = {
        "source": payload.get("repository", {}).get("full_name", "unknown"),
        "error_message": payload.get("workflow_run", {}).get("conclusion", "unknown"),
        "metadata": payload,
    }
    try:
        incident = Incident(**incident_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid incident data: {e}")

    analysis = analyzer.analyze_incident(incident)
    plan = await portia_plans.generate_plan(incident, analysis, is_issue=False)
    slack.send_incident_alert(incident, analysis, plan)

    return {"status": "CI Incident processed"}