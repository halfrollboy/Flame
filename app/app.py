# from typing import Optional
import uvicorn
from fastapi import Depends, FastAPI
# from pydantic import BaseModel
# from models.pydantic.order import Item
from .db.postgres.database import Model, engine
from .routes.employee import router_employee
from .routes.company import router_company
from fastapi.security import OAuth2PasswordBearer
import os


Model.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router_employee)
app.include_router(router_company)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=os.environ["APP_TOKEN"])


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/ping")
async def read_root():
    return {"ping": "pong!"}


@app.get("/auth")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {
        "Hello": "World",
        "token": token,
        }

# @app.get("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)