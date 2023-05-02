from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserRegister(BaseModel):
    username: EmailStr
    password: str


class Users(UserRegister):
    id: int
    created_at: Optional[datetime] = None


class UsersResponse(BaseModel):
    id: int
    username: EmailStr
    created_at: Optional[datetime] = None


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
