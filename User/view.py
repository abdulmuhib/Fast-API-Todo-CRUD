from .service import *
from fastapi import APIRouter, Path, Query
from User.api_models import User as SchemaUser
from User.api_models import UserOptional as SchemaUserPatch
from dotenv import load_dotenv

load_dotenv('../.env')

user_router = APIRouter()


@user_router.post("/add")
async def add_user(user: SchemaUser):
    user = user_add(user)
    return user


@user_router.get("/retrieve")
async def retrieve_users(
        sort: str = Query(None, alias="sort"),
        search: str = Query(None, alias="search"),
        search_fname: str = Query(None, alias="search-fname"),
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100)
):
    users = users_retrieve(sort, search, search_fname, page, page_size)
    return users


@user_router.get("/user/{user_id}")
async def get_single_user(user_id: int = Path(..., title="The ID of the user to retrieve. ")):
    user = single_user(user_id)
    return user


@user_router.patch("/patch/{id}")
async def update_user(id: int, user: SchemaUserPatch):
    response = user_update_patch(id, user)
    return response


@user_router.delete("/delete/{user_id}")
async def delete_single_user(user_id: int):
    response = single_user_delete(user_id)
    return response


@user_router.delete("/all")
async def delete_all_users():
    response = all_users_delete()
    return response
