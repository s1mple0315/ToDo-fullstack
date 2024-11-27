from fastapi import FastAPI
from routes.todo import router as todo_router
from routes.auth import router as auth_router
from routes.user import router as user_router

app = FastAPI()

app.include_router(todo_router, prefix="/todos", tags=["Todos"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])