from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    ENV: str = Field("local", description="Environment: local|dev|prod")
    DEBUG: bool = Field(True, description="Debug mode: affects logging and reload")
    PROJECT_NAME: str = "fastapi-starter"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"

    SECRET_KEY: str = Field(..., description="JWT signing key (use RS256 in prod)")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    ALLOWED_ORIGINS: List[str] = Field(default_factory=list, description="CORS origins")

    @property
    def is_prod(self) -> bool:
        return self.ENV.lower() == "prod"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
