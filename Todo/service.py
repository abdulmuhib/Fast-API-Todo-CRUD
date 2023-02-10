from fastapi import Path, HTTPException, status
from fastapi_sqlalchemy import db
from Todo.api_models import Todo as SchemaTodo
from Todo.api_models import TodoResponse as SchemaTodoResponse
from Todo.db_models import Todo as ModelTodo
from dotenv import load_dotenv

load_dotenv('../.env')


def add_todo_item(todo: SchemaTodo):
    db_todo = ModelTodo(item=todo.item)
    db.session.add(db_todo)
    db.session.commit()
    return db_todo


def all_todos():
    todos = db.session.query(ModelTodo).all()
    todo_responses = [SchemaTodoResponse(**todo.__dict__).dict() for todo in todos]
    return todo_responses


def single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve. ")):
    todo = db.session.get(ModelTodo, todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )
    todo_response = SchemaTodoResponse(**todo.__dict__).dict()

    return todo_response


def todo_update(todo_data: SchemaTodo, todo_id: int = Path(..., title="The ID of the todo to be updated")):
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


def todo_delete(todo_id: int):
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


def todo_delete_all():
    db.session.query(ModelTodo).delete()
    db.session.commit()
    return {
        "message": "Todos deleted successfully."
    }
