from models import Incident, Analysis

def analyze_incident(incident: Incident) -> Analysis:
    return Analysis(
        summary=f"Incident from {incident.source}: {incident.error_message}",
        root_cause="Not yet automated",
        severity="high" if "critical" in incident.error_message.lower() else "medium"
    )
