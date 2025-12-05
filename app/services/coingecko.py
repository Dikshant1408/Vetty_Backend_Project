import httpx
from app.core.config import settings

class CoinGeckoClient:
    def __init__(self):
        self.client = httpx.AsyncClient(base_url=settings.COINGECKO_BASE_URL)

    async def list_coins(self):
        resp = await self.client.get("/coins/list")
        resp.raise_for_status()
        return resp.json()

    async def list_categories(self):
        resp = await self.client.get("/coins/categories/list")
        resp.raise_for_status()
        return resp.json()

    async def coin_market(self, coin_id):
        resp = await self.client.get("/simple/price", params={
            "ids": coin_id,
            "vs_currencies": "inr,cad"
        })
        resp.raise_for_status()
        return resp.json()
