from pydantic import BaseModel


class ContractComparisonResponse(
    BaseModel
):

    interest_rate_winner: str

    processing_fee_winner: str

    foreclosure_winner: str

    risk_score_winner: str

    overall_winner: str

    explanation: str