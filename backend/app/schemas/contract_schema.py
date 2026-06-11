from pydantic import BaseModel
from typing import Optional


class ContractData(BaseModel):

    borrower_name: Optional[str] = None
    lender_name: Optional[str] = None

    loan_amount: Optional[float] = None

    interest_rate: Optional[float] = None

    interest_type: Optional[str] = None

    emi_amount: Optional[float] = None

    loan_duration_months: Optional[int] = None

    processing_fee: Optional[float] = None

    foreclosure_charges: Optional[str] = None

    late_payment_fee: Optional[str] = None

    penalty_charges: Optional[str] = None