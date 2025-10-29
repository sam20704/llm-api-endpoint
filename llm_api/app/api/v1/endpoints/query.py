from fastapi import APIRouter, Depends
from app.services.llm_service import LLMService
from app.core.dependencies import get_llm_client, get_cache_client

router = APIRouter()

@router.post("/", response_model=dict)
async def query_llm(payload: dict, llm_client=Depends(get_llm_client), cache=Depends(get_cache_client)):
    service = LLMService(llm_client, cache)
    return await service.get_llm_response(payload['query'])
