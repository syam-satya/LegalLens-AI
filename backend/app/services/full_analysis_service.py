from app.services.contract_parser_service import (
    ContractParserService
)

from app.services.risk_scoring_service import (
    RiskScoringService
)

from app.services.compliance_service import (
    ComplianceService
)

from app.services.retrieval_service import (
    RetrievalService
)

from app.services.ai_explanation_service import (
    AIExplanationService
)


class FullAnalysisService:

    retriever = RetrievalService()

    explainer = (
        AIExplanationService()
    )

    @classmethod
    def analyze(
        cls,
        contract_text: str
    ):

        contract_data = (
            ContractParserService.parse(
                contract_text
            )
        )

        risk = (
            RiskScoringService.analyze(
                contract_data
            )
        )

        compliance = (
            ComplianceService.check(
                contract_data
            )
        )

        rules = (
            cls.retriever.retrieve(
                contract_text
            )
        )

        summary = (
            cls.explainer.generate_summary(
                contract_data,
                risk,
                compliance,
                rules
            )
        )

        simplified = (
            cls.explainer.simplify_contract(
                contract_text
            )
        )

        return {
            "contract_data":
            contract_data,

            "risk":
            risk,

            "compliance":
            compliance,

            "rules":
            rules,

            **summary,

            "simplified_contract":
            simplified
        }