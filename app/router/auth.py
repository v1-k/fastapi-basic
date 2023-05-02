from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import uuid
from datetime import datetime
from .. import schema,  util, oauth2, database

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schema.UsersResponse)
def register(user: schema.UserRegister):
    db = database.users
    if user.username in db.get():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"User already registered")
    hashed_password = util.hash(user.password)
    id = uuid.uuid4().int
    created_at = datetime.now()
    new_user = schema.Users(username=user.username,
                            password=hashed_password,
                            id=id,
                            created_at=created_at)
    db.set(new_user)
    return new_user


@router.post('/login', response_model=schema.AccessToken)
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    db = database.users.get()
    if user_credentials.username not in db or not util.verify(user_credentials.password, db[user_credentials.username]['password']):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    access_token = oauth2.create_access_token(
        data={"username": user_credentials.username})
    new_token = schema.AccessToken(
        access_token=access_token, token_type="bearer")
    return new_token
