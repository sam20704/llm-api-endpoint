import httpx
import aioredis
from openai import AsyncAzureOpenAI  # ← Changed import
from app.core.config import settings

http_client = httpx.AsyncClient(
    limits=httpx.Limits(max_connections=1000, max_keepalive_connections=100),
    timeout=httpx.Timeout(60.0, connect=5.0)
)

# Azure OpenAI Client
llm_client = AsyncAzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    http_client=http_client
)

redis_client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)

def get_llm_client():
    return llm_client

def get_cache_client():
    return redis_client
