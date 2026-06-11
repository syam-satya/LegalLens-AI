from fastapi import FastAPI
from pathlib import Path

from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health_routes import router as health_router
from app.api.routes.upload_routes import router as upload_router

from app.api.routes.analysis_routes import router as analysis_router

from app.services.llm_service import LLMService
llm = LLMService()


app = FastAPI(
    title = "LegalLens  AI",
    version = "1.0.0",
    description = "AI-Assisted Loan & EMI Contract Risk Analyzer"
)

#CORS Configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Include Routes

@app.get("/")
def root():
    return {
        "message" : "LegalLens AI Backend running"
    }

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    upload_router,
    tags=["Upload"]
)

app.include_router(
    analysis_router,
    tags=["Analysis"]
)


# create uploads directory if it doesn't exist
UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# routers

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(analysis_router)


from app.api.routes.report_routes import (
    router as report_router
)

app.include_router(
    report_router
)

from app.api.routes.comparison_routes import (
    router as comparison_router
)

app.include_router(
    comparison_router
) 