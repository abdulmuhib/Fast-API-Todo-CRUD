from fastapi import FastAPI
from Todo.view import todo_router
from User.view import user_router

import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router, prefix="/todos", tags=["todos"])
app.include_router(user_router, prefix="/users", tags=["users"])

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)