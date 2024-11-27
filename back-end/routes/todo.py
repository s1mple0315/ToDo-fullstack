from fastapi import APIRouter, Depends, HTTPException
from utils.auth import verify_token
from models.todos import Todo
from config.db import collection_name
from bson import ObjectId

router = APIRouter()

def get_current_user(token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@router.get("/")
async def get_todos(current_user: dict = Depends(get_current_user)):
    todos = collection_name.find({"user_id": current_user["sub"]})
    return list(todos)

@router.post("/")
async def create_todo(todo: Todo, current_user: dict = Depends(get_current_user)):
    todo_data = dict(todo)
    todo_data["user_id"] = current_user["sub"]
    collection_name.insert_one(todo_data)
    return {"msg": "Todo created"}

@router.put("/{id}")
async def update_todo(id: str, todo: Todo, current_user: dict = Depends(get_current_user)):
    todo_data = collection_name.find_one({"_id": ObjectId(id)})
    if not todo_data or todo_data["user_id"] != current_user["sub"]:
        raise HTTPException(status_code=404, detail="Todo not found or unauthorized")
    
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"msg": "Todo updated"}

@router.delete("/{id}")
async def delete_todo(id: str, current_user: dict = Depends(get_current_user)):
    todo_data = collection_name.find_one({"_id": ObjectId(id)})
    if not todo_data or todo_data["user_id"] != current_user["sub"]:
        raise HTTPException(status_code=404, detail="Todo not found or unauthorized")
    
    collection_name.delete_one({"_id": ObjectId(id)})
    return {"msg": "Todo deleted"}
