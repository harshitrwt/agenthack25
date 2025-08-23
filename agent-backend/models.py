from pydantic import BaseModel, Field
from typing import Optional, Dict


class Incident(BaseModel):
    source: str
    error_message: str
    metadata: Dict = Field(default_factory=dict)  

class Analysis(BaseModel):
    summary: str
    root_cause: Optional[str] = None
    severity: str = "medium" 
