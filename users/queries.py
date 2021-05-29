from passlib.context import CryptContext
from typing import Optional
from sqlalchemy.orm import Session
from config.database import get_db
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from datetime import timedelta , datetime
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from .schema import TokenData
from .models import User

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

#---------Hashing password---------------------------------------------------
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


#--------USER MODEL QUERIES-----------------------------------------------------------
def create(request, db:Session=Depends(get_db)):
    new_user= User(username=request.username, email=request.email,
                 password=get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def detail(id, db:Session=Depends(get_db)):
    user= db.query(User).filter(User.id== id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found id:{id}")
    return user


#-------AUTHENTICATION------------------------------------------------------------
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate(username, password, db:Session=Depends(get_db)):
    user= db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with username: {username}")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect password for username: {username}")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, 
                    expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(db:Session=Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user= db.query(User).filter(User.username== token_data.username).first()
    if not user:
        raise credentials_exception
    return user
    
    
