from fastapi import APIRouter, Depends, Query
from app.core.auth import verify_token
from app.services.coingecko import CoinGeckoClient

router = APIRouter()
client = CoinGeckoClient()

@router.get("/", summary="List all coins with pagination")
async def list_coins(
    page_num: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=250),
    user=Depends(verify_token)
):
    data = await client.list_coins()
    start = (page_num - 1) * per_page
    end = start + per_page
    return {
        "page_num": page_num,
        "per_page": per_page,
        "items": data[start:end]
    }

@router.get("/{coin_id}", summary="Market data for a specific coin")
async def get_coin(
    coin_id: str,
    user=Depends(verify_token)
):
    market = await client.coin_market(coin_id)
    return {coin_id: market.get(coin_id)}
