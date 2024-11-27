from fastapi import APIRouter, HTTPException
from models.user import User
from utils.auth import hash_password
from config.db import db

router = APIRouter()

@router.post("/register")
async def register(user: User):
    existing_user = db.users.find_one({"username" : user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = hash_password(user.password)
    db.users.insert_one({"username" : user.username, "email" : user.email, "password" : hashed_password})
    return {"msg" : "User created successfully"}
