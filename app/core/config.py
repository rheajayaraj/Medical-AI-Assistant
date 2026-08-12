from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Medical AI Assistant"
    VERSION: str = "1.0.0"
    SEARCH_TOP_K: int = 5
    SIMILARITY_THRESHOLD: float = 0.8
    GEMINI_API_KEY: str
    GEMINI_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()