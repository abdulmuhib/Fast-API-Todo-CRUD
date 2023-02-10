from pydantic import BaseModel


class Todo(BaseModel):

    item: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "item": "Example schema!"
            }
        }


class TodoResponse(BaseModel):

    id: int
    item: str

    class Config:
        orm_mode = True
