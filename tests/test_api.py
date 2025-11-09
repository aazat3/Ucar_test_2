import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_and_get_incident(async_client: AsyncClient):
   response = await async_client.post("/incidents/", json={"text": "Test issue", "source": "operator"})
   assert response.status_code == 201
   data = response.json()
   assert data["text"] == "Test issue"

   response = await async_client.get("/incidents/")
   assert response.status_code == 200
   assert len(response.json()) == 1

@pytest.mark.asyncio
async def test_update_status(async_client: AsyncClient):
      response = await async_client.patch("/incidents/1", json={"status": "resolved"})
      assert response.status_code == 200
      assert response.json()["status"] == "resolved"
