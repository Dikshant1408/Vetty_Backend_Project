from fastapi import APIRouter, Depends
from app.core.auth import verify_token
from app.services.coingecko import CoinGeckoClient

router = APIRouter()
client = CoinGeckoClient()

@router.get("/")
async def list_categories(user=Depends(verify_token)):
    data = await client.list_categories()
    return {"items": data}
