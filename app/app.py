# from typing import Optional
import uvicorn
from fastapi import FastAPI

# from pydantic import BaseModel
# from models.pydantic.order import Item
from .db.postgres.database import Model, engine
from .routes.employee import router_employee
from .routes.company import router_company
from .routes.user import router_user
from .modules.auth.auth import get_auth
from starlette_exporter import PrometheusMiddleware, handle_metrics

# import os
from loguru import logger

Model.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router_employee)
app.include_router(router_company)
app.include_router(router_user)
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

logger.add("logs/logs.log", level="DEBUG", retention="10 days", rotation="00:00")


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.get("/ping")
async def read_root():
    return {"ping": "pong!"}


@router_user.get("/token")
async def get_token():
    return f"{get_auth()}"


# @app.get("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
