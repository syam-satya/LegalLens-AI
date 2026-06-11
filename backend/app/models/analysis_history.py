from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text
)

from app.db.database import Base


class AnalysisHistory(
    Base
):

    __tablename__ = (
        "analysis_history"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    file_name = Column(
        String
    )

    risk_score = Column(
        Float
    )

    risk_level = Column(
        String
    )

    contract_summary = Column(
        Text
    )