from app.schemas.contract_schema import ContractData

from app.utils.regex_extractors import (
    extract_loan_amount,
    extract_interest_rate,
    extract_emi_amount,
    extract_duration
)

from app.utils.parser_helpers import (
    extract_borrower_name,
    extract_lender_name
)

from app.utils.regex_extractors import (
    extract_loan_amount,
    extract_interest_rate,
    extract_emi_amount,
    extract_duration,
    extract_processing_fee,
    extract_foreclosure_charges,
    extract_late_payment_fee,
    extract_penalty_clause,
    detect_interest_type
)


class ContractParserService:

    @staticmethod
    def parse(text: str):

        return ContractData(

    borrower_name=extract_borrower_name(text),

    lender_name=extract_lender_name(text),

    loan_amount=extract_loan_amount(text),

    interest_rate=extract_interest_rate(text),

    interest_type=detect_interest_type(text),

    emi_amount=extract_emi_amount(text),

    loan_duration_months=extract_duration(text),

    processing_fee=extract_processing_fee(text),

    foreclosure_charges=
        extract_foreclosure_charges(text),

    late_payment_fee=
        extract_late_payment_fee(text),

    penalty_charges=
        extract_penalty_clause(text)
)
    
        