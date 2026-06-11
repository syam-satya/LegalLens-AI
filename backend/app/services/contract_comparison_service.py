from app.services.llm_service import (
    LLMService
)

class ContractComparisonService:

    @staticmethod
    def compare(
        contract_a,
        contract_b
    ):

        result = {}

        # Interest Rate

        rate_a = contract_a.get(
            "interest_rate",
            999
        )

        rate_b = contract_b.get(
            "interest_rate",
            999
        )

        result[
            "interest_rate_winner"
        ] = (
            "A"
            if rate_a < rate_b
            else "B"
        )

        # Processing Fee

        fee_a = contract_a.get(
            "processing_fee",
            999999
        )

        fee_b = contract_b.get(
            "processing_fee",
            999999
        )

        result[
            "processing_fee_winner"
        ] = (
            "A"
            if fee_a < fee_b
            else "B"
        )

        # Foreclosure

        foreclosure_a = contract_a.get(
            "foreclosure_charges",
            999999
        )

        foreclosure_b = contract_b.get(
            "foreclosure_charges",
            999999
        )

        result[
            "foreclosure_winner"
        ] = (
            "A"
            if foreclosure_a < foreclosure_b
            else "B"
        )

        # Risk Score

        risk_a = contract_a.get(
            "risk_score",
            100
        )

        risk_b = contract_b.get(
            "risk_score",
            100
        )

        result[
            "risk_score_winner"
        ] = (
            "A"
            if risk_a < risk_b
            else "B"
        )

        score_a = 0
        score_b = 0

        for key in [
            "interest_rate_winner",
            "processing_fee_winner",
            "foreclosure_winner",
            "risk_score_winner"
        ]:

            if result[key] == "A":
                score_a += 1
            else:
                score_b += 1

        result[
            "overall_winner"
        ] = (
            "A"
            if score_a > score_b
            else "B"
        )


        llm = LLMService()

    @staticmethod
    def compare(
        contract_a,
        contract_b
    ):

        result = {}

        # comparison logic
        ...
        
        return result

    @staticmethod
    def generate_explanation(
        comparison
    ):

        prompt = f"""
You are a financial analyst.

Explain these comparison results:

{comparison}

Which contract is better for the borrower?

Explain in simple English.
"""

        return (
            ContractComparisonService.llm.generate(
                prompt
            )
        )

        return result