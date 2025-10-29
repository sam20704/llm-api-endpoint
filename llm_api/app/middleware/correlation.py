import uuid, structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class CorrelationIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        structlog.contextvars.bind_contextvars(request_id=request_id)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        structlog.contextvars.clear_contextvars()
        return response
