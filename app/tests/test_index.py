import pytest


@pytest.mark.asyncio
async def test_index(client):
    res = await client.get('/')
    res_json = res.json()
    assert res.status_code == 200
    assert res_json['message'] == "hello"
