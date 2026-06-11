from app.models.analysis_history import (
    AnalysisHistory
)


class HistoryService:

    @staticmethod
    def save(
        db,
        analysis
    ):

        record = AnalysisHistory(

            risk_score=
            analysis["risk"]["score"],

            risk_level=
            analysis["risk"]["level"],

            contract_summary=
            analysis["contract_summary"],

            borrower_explanation=
            analysis["borrower_explanation"],

            recommendations=
            analysis["recommendations"],

            compliance_issues=
            analysis["compliance"]
        )

        db.add(record)

        db.commit()

        db.refresh(record)

        return record