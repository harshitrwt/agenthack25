from pydantic import BaseModel
from typing import Optional, Dict

class Incident(BaseModel):
    source: str         
    error_message: str
    metadata: Optional[Dict] = None

class Analysis(BaseModel):
    summary: str
    root_cause: Optional[str] = None
    severity: Optional[str] = "medium"
