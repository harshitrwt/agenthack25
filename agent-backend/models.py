from pydantic import BaseModel, Field
from typing import Optional, Dict

class Incident(BaseModel):
    source: str = "Unknown Source"
    error_message: str = "No error message"
    metadata: Dict = Field(default_factory=dict)

class Analysis(BaseModel):
    summary: str = "No summary available."
    root_cause: Optional[str] = "Not yet determined."
    severity: str = "medium"
