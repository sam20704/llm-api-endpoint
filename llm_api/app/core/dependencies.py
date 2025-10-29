import httpx, aioredis
from openai import AsyncOpenAI
from app.core.config import settings

http_client = httpx.AsyncClient(limits=httpx.Limits(max_connections=1000, max_keepalive_connections=100))
llm_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY, http_client=http_client)
redis_client = aioredis.from_url(settings.REDIS_URL, decode_responses=True)

def get_llm_client():
    return llm_client

def get_cache_client():
    return redis_client
