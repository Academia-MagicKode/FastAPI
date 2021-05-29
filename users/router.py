from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config.database import get_db
from .queries import create, detail, get_current_user
from .schema import UserSchema, UserShowSchema

users_router= APIRouter(
    prefix="/user",
    tags=["users"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@users_router.post("/", status_code=201, response_model= UserShowSchema)
def create_user(request:UserSchema, db: Session=Depends(get_db)):
    return create(request,db)


@users_router.get("/{id}", status_code=200, response_model=UserShowSchema)
def show(id:int,db:Session=Depends(get_db)):
    return detail(id, db)

