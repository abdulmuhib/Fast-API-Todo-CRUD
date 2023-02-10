from .service import *
from fastapi import APIRouter, Path
from Todo.api_models import Todo as SchemaTodo
from Todo.api_models import TodoResponse as SchemaTodoResponse
from dotenv import load_dotenv


load_dotenv('../.env')

todo_router = APIRouter()


@todo_router.post("/add", response_model=SchemaTodoResponse)
async def add_todo(todo: SchemaTodo):
    todo = add_todo_item(todo)
    return todo


@todo_router.get("/retrieve")
async def retrieve_todos():
    todos = all_todos()
    return todos


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve. ")):
    todo = single_todo(todo_id)
    return todo


@todo_router.put("/update/{todo_id}")
async def update_todo(todo_data: SchemaTodo, todo_id: int = Path(..., title="The ID of the todo to be updated")):
    todo = todo_update(todo_data, todo_id)
    return todo


@todo_router.delete("/delete/{todo_id}")
async def delete_single_todo(todo_id: int):
    todo = todo_delete(todo_id)
    return todo


@todo_router.delete("/all")
async def delete_all_todo():
    todo = todo_delete_all()
    return todo
