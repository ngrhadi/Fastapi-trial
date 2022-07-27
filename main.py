from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/sample/")
def get_sample():
    return sample(name="sample",
                  description="sample",
                  price=1.0,
                  tax=1.0,
                  geografi=geo_data(type="Point", coordinates=[1.0, 1.0]))


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
async def read_item(item_id: int, item: Item | None = None):
    return {"item_id": item_id, "item": "item"}


@app.get("/items/")
async def read_items():
    return [{"item_id": "item1"}, {"item_id": "item2"}]
