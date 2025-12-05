import pytest
import httpx
import respx
from httpx import Response
from app.main import app

@pytest.mark.asyncio
@respx.mock
async def test_list_categories():
    respx.get("https://api.coingecko.com/api/v3/coins/categories/list").mock(
        return_value=Response(200, json=[
            {"category_id": "defi", "name": "Decentralized Finance"},
            {"category_id": "gaming", "name": "Gaming"}
        ])
    )

    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        # get JWT token
        token_resp = await ac.post("/auth/token", json={"username": "tester"})
        token = token_resp.json()["access_token"]

        resp = await ac.get("/categories", headers={"Authorization": f"Bearer {token}"})

    assert resp.status_code == 200
    data = resp.json()
    assert len(data["items"]) == 2
