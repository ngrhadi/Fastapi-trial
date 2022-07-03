from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class geo_data(BaseModel):
    type: str
    coordinates: list


class sample(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    geografi: geo_data | None = None


@app.put("/sample/{sample_id}")
async def update_sample(sample_id: int, sample: sample):
    data = {
        "id": sample_id,
        #   "sample": sample # This will make parent of each child
        "name": sample.name,
        "description": sample.description,
        "price": sample.price,
        "tax": sample.tax,
        "geografi": sample.geografi
    }
    return data


# print(sample.__annotations__)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
