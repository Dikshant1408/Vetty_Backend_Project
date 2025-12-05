from fastapi import FastAPI
from app.api import auth, coins, categories, health
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(auth.router, prefix="/auth")
app.include_router(coins.router, prefix="/coins")
app.include_router(categories.router, prefix="/categories")
app.include_router(health.router)
