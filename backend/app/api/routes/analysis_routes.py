from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.analysis_history import AnalysisHistory

from app.services.contract_parser_service import ContractParserService
from app.services.retrieval_service import RetrievalService
from app.services.ai_analysis_service import AIAnalysisService
from app.services.risk_scoring_service import RiskScoringService
from app.services.compliance_service import ComplianceService
from app.services.ai_explanation_service import AIExplanationService
from app.services.contract_comparison_service import ContractComparisonService
from app.services.llm_service import LLMService

from app.services.full_analysis_service import (
    FullAnalysisService
)


router = APIRouter()

retriever = RetrievalService()
analysis_service = AIAnalysisService()
explanation_service = AIExplanationService()
llm = LLMService()


# -----------------------------------
# Extract Contract
# -----------------------------------

@router.post("/extract")
async def extract_contract(text: str):

    result = ContractParserService.parse(text)

    return result


# -----------------------------------
# Retrieve Rules
# -----------------------------------

@router.post("/retrieve-rules")
async def retrieve_rules(query: str):

    return retriever.retrieve(query=query)


# -----------------------------------
# Full Analysis
# -----------------------------------

@router.post("/analyze")
async def analyze_contract(
    contract_text: str,
    db: Session = Depends(get_db)
):

    parsed_contract = (
        ContractParserService.parse(
            contract_text
        )
    )

    rules = (
        retriever.retrieve(
            contract_text
        )
    )

    result = (
        analysis_service.analyze(
            parsed_contract,
            rules
        )
    )

    risk_score = (
        result.get("risk", {})
        .get("score", 0)
    )

    risk_level = (
        result.get("risk", {})
        .get("level", "LOW")
    )

    history = AnalysisHistory(
        file_name="Manual Input",
        risk_score=risk_score,
        risk_level=risk_level,
        contract_summary=str(
            result.get(
                "contract_summary",
                ""
            )
        )
    )

    db.add(history)
    db.commit()

    return result


# -----------------------------------
# Risk Analysis
# -----------------------------------

@router.post("/risk-analysis")
async def risk_analysis(
    text: str
):

    contract = (
        ContractParserService.parse(text)
    )

    risk_result = (
        RiskScoringService.analyze(
            contract
        )
    )

    compliance_issues = (
        ComplianceService.check(
            contract
        )
    )

    return {
        "risk": risk_result,
        "compliance": compliance_issues
    }


# -----------------------------------
# AI Explanation
# -----------------------------------

@router.post("/explain-contract")
async def explain_contract(
    contract_text: str
):

    contract_data = (
        ContractParserService.parse(
            contract_text
        )
    )

    risk_analysis = (
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
        retriever.retrieve(
            contract_text
        )
    )

    summary = (
        explanation_service.generate_summary(
            contract_data,
            risk_analysis,
            compliance,
            rules
        )
    )

    simplified = (
        explanation_service.simplify_contract(
            contract_text
        )
    )

    return {
        **summary,
        "simplified_contract":
        simplified
    }


# -----------------------------------
# History
# -----------------------------------

@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):

    return (
        db.query(
            AnalysisHistory
        )
        .order_by(
            AnalysisHistory.id.desc()
        )
        .all()
    )


# -----------------------------------
# Compare Contracts
# -----------------------------------

@router.post("/compare-contracts")
async def compare_contracts():

    contract_a = {
        "interest_rate": 12.5,
        "processing_fee": 5000,
        "foreclosure_charges": 2,
        "risk_score": 45
    }

    contract_b = {
        "interest_rate": 13.8,
        "processing_fee": 3500,
        "foreclosure_charges": 5,
        "risk_score": 60
    }

    comparison = (
        ContractComparisonService.compare(
            contract_a,
            contract_b
        )
    )

    explanation = (
        ContractComparisonService.generate_explanation(
            comparison
        )
    )

    return {
        **comparison,
        "explanation":
        explanation
    }


# -----------------------------------
# Dashboard Statistics
# -----------------------------------

@router.get("/dashboard-stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    analyses = (
        db.query(
            AnalysisHistory
        ).all()
    )

    total = len(analyses)

    high_risk = len([
        a for a in analyses
        if a.risk_level == "HIGH"
    ])

    medium_risk = len([
        a for a in analyses
        if a.risk_level == "MEDIUM"
    ])

    low_risk = len([
        a for a in analyses
        if a.risk_level == "LOW"
    ])

    return {
        "total_contracts": total,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk
    }


# -----------------------------------
# LLM Test
# -----------------------------------

@router.get("/test-llm")
async def test_llm():

    response = llm.generate(
        "Explain EMI in one sentence."
    )

    return {
        "response": response
    }


@router.post(
    "/analyze-contract"
)
async def analyze_contract_complete(
    contract_text: str,
    db: Session = Depends(get_db)
):

    result = (
        FullAnalysisService.analyze(
            contract_text
        )
    )

    risk = result.get(
        "risk",
        {}
    )

    history = AnalysisHistory(
        file_name="Manual Input",

        risk_score=
        risk.get(
            "score",
            0
        ),

        risk_level=
        risk.get(
            "level",
            "LOW"
        ),

        contract_summary=
        str(
            result.get(
                "contract_summary",
                ""
            )
        )
    )

    db.add(history)

    db.commit()

    return result

