from pydantic import BaseModel
from typing import List


class Todo(BaseModel):

    item: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "item": "Example schema!"
            }
        }


class TodoItem(BaseModel):

    id: int
    item: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "item": "Example Schema!"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
