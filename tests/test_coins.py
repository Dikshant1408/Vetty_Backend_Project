import pytest
import httpx
import respx
from httpx import Response
from app.main import app

@pytest.mark.asyncio
@respx.mock
async def test_list_coins():
    # Mock CoinGecko response
    respx.get("https://api.coingecko.com/api/v3/coins/list").mock(
        return_value=Response(200, json=[
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
            {"id": "ethereum", "symbol": "eth", "name": "Ethereum"}
        ])
    )

    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        # Step 1: Get token
        token_resp = await ac.post("/auth/token", json={"username": "test"})
        token = token_resp.json()["access_token"]

        # Step 2: Request coins
        resp = await ac.get("/coins", headers={"Authorization": f"Bearer {token}"})

    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 2
    assert items[0]["id"] == "bitcoin"
