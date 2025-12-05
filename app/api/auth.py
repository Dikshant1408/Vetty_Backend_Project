from fastapi import APIRouter
from pydantic import BaseModel
from app.core.auth import create_access_token

router = APIRouter()

class Login(BaseModel):
    username: str

@router.post("/token")
def login(user: Login):
    token = create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}
