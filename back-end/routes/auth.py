# In routes/auth.py
from fastapi import APIRouter, HTTPException
from models.user import User
from utils.auth import verify_password, create_access_token
from config.db import db

router = APIRouter()

@router.post("/login")
async def login(user: User):
    db_user = db.users.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
