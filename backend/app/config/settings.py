from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    LLM_PROVIDER: str
    LLM_API_KEY: str
    LLM_MODEL: str

    CHROMA_DB_PATH: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


settings = Settings()