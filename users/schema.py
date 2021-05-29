from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class UserShowSchema(BaseModel):
    id:int
    username:str
    email:str

    class Config():
        orm_mode= True
    
class TokenSchema(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: Optional[str] = None

