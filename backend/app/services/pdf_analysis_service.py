from app.services.pdf_service import PDFService
from app.services.full_analysis_service import FullAnalysisService


class PDFAnalysisService:

    @classmethod
    def analyze_pdf(
        cls,
        pdf_path: str
    ):

        contract_text = (
            PDFService.extract_text(
                pdf_path
            )
        )

        result = (
            FullAnalysisService.analyze(
                contract_text
            )
        )

        result["raw_text"] = (
            contract_text
        )

        return result