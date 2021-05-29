from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.database import Base, engine
from sqlalchemy.orm import Session
from config.database import get_db
from users.router import users_router
from users.queries import authenticate
from cryptos.router import crypto_router

app = FastAPI()
app.include_router(users_router)
app.include_router(crypto_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

Base.metadata.create_all(engine)


@app.post("/token", tags=["authentication"])
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    return authenticate(request.username, request.password, db)


