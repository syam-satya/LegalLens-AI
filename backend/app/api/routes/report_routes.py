from fastapi import APIRouter

from app.services.pdf_report_service import (
    PDFReportService
)

router = APIRouter()


@router.post("/generate-report")
async def generate_report():

    sample_data = {

        "contract_summary":
        "Personal loan agreement.",

        "risk": {

            "score": 65,

            "level": "MEDIUM",

            "findings": [

                {
                    "title":
                    "Floating Interest Rate",

                    "explanation":
                    "Interest may increase."
                }
            ]
        },

        "recommendations": [

            "Negotiate charges.",
            "Ask for fixed interest."
        ],

        "simplified_contract":
        "You borrow money and repay through EMI."
    }

    pdf_path = (
        PDFReportService.generate(
            sample_data
        )
    )

    return {
        "report_path": pdf_path
    }