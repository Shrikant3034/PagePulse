from fastapi import FastAPI

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.routes import router
from app.limiter import limiter

app = FastAPI(
    title="Page Pulse API",
    version="1.0.0",
    description="Production-ready URL Audit Service"
)

app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
)

app.include_router(router)