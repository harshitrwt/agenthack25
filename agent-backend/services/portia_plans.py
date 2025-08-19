from portia import Portia
from models import Incident, Analysis

def generate_plan(incident: Incident, analysis: Analysis):
    agent = Portia()
    plan = agent.plan(
        goal=f"Fix incident: {analysis.summary}",
        context={
            "incident_source": incident.source,
            "error_message": incident.error_message,
            "root_cause": analysis.root_cause
        }
    )
    return plan
