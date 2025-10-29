from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints.query import router as query_router
from app.middleware.correlation import CorrelationIDMiddleware

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
app.add_middleware(CorrelationIDMiddleware)

# Mount routers
app.include_router(query_router, prefix="/api/v1/query")

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
