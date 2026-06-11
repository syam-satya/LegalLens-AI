from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from app.schemas.upload_schema import UploadResponse

from app.services.pdf_service import PDFService
from app.services.text_cleaning_service import TextCleaningService

from app.utils.validators import validate_pdf

router = APIRouter()


RAW_FOLDER = Path("app/uploads/raw")
PROCESSED_FOLDER = Path("app/uploads/processed")

RAW_FOLDER.mkdir(parents=True, exist_ok=True)
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post(
    "/upload",
    response_model=UploadResponse
)
async def upload_document(
    file: UploadFile = File(...)
):

    if not validate_pdf(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    pdf_path = RAW_FOLDER / file.filename

    PDFService.save_uploaded_file(
        file,
        str(pdf_path)
    )

    extracted_text = PDFService.extract_text(
        str(pdf_path)
    )

    cleaned_text = TextCleaningService.clean(
        extracted_text
    )

    output_file = (
        PROCESSED_FOLDER /
        f"{pdf_path.stem}.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(cleaned_text)

    return UploadResponse(
        filename=file.filename,
        file_size=pdf_path.stat().st_size,
        extracted_characters=len(cleaned_text),
        status="success"
    )

from app.services.pdf_analysis_service import (
    PDFAnalysisService
)

from app.models.analysis_history import (
    AnalysisHistory
)

from app.db.session import (
    get_db
)

from sqlalchemy.orm import (
    Session
)

@router.post(
    "/upload-and-analyze"
)
async def upload_and_analyze(
    file: UploadFile,
    db: Session = Depends(get_db)
):

    file_path = (
        RAW_FOLDER /
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )

    result = (
        PDFAnalysisService.analyze_pdf(
            str(file_path)
        )
    )

    risk = result.get(
        "risk",
        {}
    )

    history = (
        AnalysisHistory(
            file_name=file.filename,

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
    )

    db.add(history)

    db.commit()

    return result
