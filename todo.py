from fastapi import APIRouter, Path, HTTPException, status
from fastapi_sqlalchemy import db
from schema import Todo as SchemaTodo
from schema import TodoItem as SchemaTodoItem
from schema import TodoItems as SchemaTodoItems
from model import Todo as ModelTodo
from dotenv import load_dotenv

load_dotenv('.env')

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo/", response_model=SchemaTodoItem)
async def add_todo(todo: SchemaTodo):
    db_todo = ModelTodo(item=todo.item)
    db.session.add(db_todo)
    db.session.commit()
    return db_todo


@todo_router.get("/todo/")
async def retrieve_todos():
    todo = db.session.query(ModelTodo).all()
    return todo



@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve. ")):
    todo_list = db.session.query(ModelTodo).all()
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: SchemaTodo, todo_id: int = Path(..., title="The ID of the todo to be updated")):
    todo = db.session.get(ModelTodo, todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )

    todo.item = todo_data.item
    db.session.commit()
    return {
        "message": "Todo updated successfully."
    }



@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int):

    todo = db.session.get(ModelTodo, todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )
    db.session.delete(todo)
    db.session.commit()
    return {"ok": True,
            "message": "Todo deleted Successfully"}


@todo_router.delete("/todo")
async def delete_all_todo():
    db.session.query(ModelTodo).delete()
    db.session.commit()
    return {
        "message": "Todos deleted successfully."
    }
