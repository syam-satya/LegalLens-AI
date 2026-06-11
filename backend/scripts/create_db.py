from app.db.database import Base

from app.db.session import (
    engine
)

from app.models.analysis_history import (
    AnalysisHistory
)

Base.metadata.create_all(
    bind=engine
)

print(
    "Database Created"
)