from victorin import quiz, task
from time import time


# @quiz.get("/")
# async def get_quiz(responce):
#     print(responce)
    
    # r = await requests.get(URL)
    # r.status_code
    # return r.json()

@quiz.get('/category')
async def f():
    start = time()
    responce = await task()
    return responce