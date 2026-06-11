from pydantic import BaseModel
from typing import List


class RiskItem(BaseModel):
    title: str
    severity: str
    explanation: str


class AIAnalysisResponse(BaseModel):
    contract_summary: str

    risks: List[RiskItem]

    recommendations: List[str]

    overall_risk_score: int

    borrower_explanation: str

    recommendations: List[str]

    simplified_contract: str