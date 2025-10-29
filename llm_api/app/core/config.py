from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME = "LLM API"
    APP_VERSION = "1.0.0"
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    REDIS_URL: str = "redis://localhost:6379"
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = False
    class Config:
        env_file = ".env"
settings = Settings()
