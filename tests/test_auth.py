import pytest
import httpx
from app.main import app

@pytest.mark.asyncio
async def test_auth_token():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/auth/token", json={"username": "tester"})

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
