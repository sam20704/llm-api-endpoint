from tenacity import retry, wait_random_exponential, stop_after_attempt, retry_if_exception_type
from openai import RateLimitError, APITimeoutError

class LLMService:
    def __init__(self, client, cache):
        self.client = client
        self.cache = cache

    @retry(wait=wait_random_exponential(min=1, max=10), stop=stop_after_attempt(5), retry=retry_if_exception_type((RateLimitError, APITimeoutError)))
    async def get_llm_response(self, prompt):
        cached = await self.cache.get(prompt)
        if cached:
            return {"result": cached, "cached": True}
        response = await self.client.chat.completions.create(model="gpt-4-turbo-preview", messages=[{"role": "user", "content": prompt}], max_tokens=512)
        await self.cache.set(prompt, response.choices[0].message.content, ex=600)
        return {"result": response.choices[0].message.content, "cached": False}
