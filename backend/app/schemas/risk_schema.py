from pydantic import BaseModel
from typing import List


class RiskFinding(BaseModel):
    title: str
    severity: str
    explanation: str


class RiskAnalysis(BaseModel):
    score: int
    level: str
    findings: List[RiskFinding]