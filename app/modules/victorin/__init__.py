from fastapi import APIRouter
import httpx


URL='https://jservice.io/api/category'

quiz = APIRouter(
    prefix="/quiz",
    tags=["quiz"],
    # dependencies=[Depends(get_token_handler)],
    responses={404: {"quiz": "Not found"}},
)


async def request(client):
    # headers["count"]= '1'
    response = await client.post(URL, params={"id":1})
    print(response.url)
    print(response)
    # if response.status != 200:
    #     response = "Error"
    return response.text


async def task():
    async with httpx.AsyncClient() as client:
        tasks = await request(client)
        return tasks