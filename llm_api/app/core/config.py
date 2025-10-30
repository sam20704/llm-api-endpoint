from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "LLM API"
    APP_VERSION: str = "1.0.0"
    
    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str
    AZURE_OPENAI_API_VERSION: str = "2024-10-21"
    AZURE_OPENAI_MODEL: Optional[str] = "gpt-4"  # For logging/reference
    
    # Optional: Keep old OpenAI for fallback
    # OPENAI_API_KEY: Optional[str] = None
    
    REDIS_URL: str = "redis://localhost:6379"
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()
