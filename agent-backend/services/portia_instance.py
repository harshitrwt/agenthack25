from services.portia_instance import portia_agent
from models import Incident, Analysis

def generate_plan(incident: Incident, analysis: Analysis):
    plan = portia_agent.plan(
        goal=f"Fix incident: {analysis.summary}",
        context={
            "incident_source": incident.source,
            "error_message": incident.error_message,
            "root_cause": analysis.root_cause
        }
    )
    return plan
