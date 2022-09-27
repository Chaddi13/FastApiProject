from bson.objectid import ObjectId
from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from src.config.db import collection
from src.models.lamoda import Sneakers
from src.schemas.lamoda_schema import sneakers_list_entity, sneakers_entity

lamoda_router = APIRouter()

"""CRUD for lamoda items"""


@lamoda_router.get('/')
async def show_all_items():
    return sneakers_list_entity(collection.find())


@lamoda_router.get('/{id}')
async def find_item(id):
    item = collection.find_one({"_id": ObjectId(id)})
    return sneakers_entity(item)


@lamoda_router.post("/", status_code=HTTP_201_CREATED, response_description="New item added")
async def create_item(body: Sneakers):
    collection.insert_one(dict(body))
    return dict(body)


@lamoda_router.put("/{id)", response_description="Item updated")
async def update_item(id, body: Sneakers):
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(body)})
    return sneakers_entity(collection.find_one({"_id": ObjectId(id)}))


@lamoda_router.delete('/{id}', response_description="Item deleted")
async def update_item(id):
    return sneakers_entity(collection.find_one_and_delete({"_id": ObjectId(id)}))
