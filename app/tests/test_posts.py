import pytest

from app.schema import PostCreate


@pytest.mark.asyncio
async def test_get_post(client):
    res = await client.get('/posts/1')
    post = res.json()
    assert res.status_code == 200
    assert post['id'] == 1


@pytest.mark.asyncio
async def test_write_post(client):
    post_data = PostCreate(email="test@test.com", title="글쓰기 테스트", content="글쓰기 내용")
    write_res = await client.post('/posts', json=post_data.dict())
    res = await client.get('/posts/2')
    res_post = res.json()
    assert write_res.status_code == 201
    assert res.status_code == 200
    assert res_post['title'] == "글쓰기 테스트"

