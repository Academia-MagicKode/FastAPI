from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from users.queries import get_current_user
from .queries import *


crypto_router= APIRouter(
    prefix="/cryptocurrency",
    tags=["cryptocurrencies"]
)

@crypto_router.get("/list", status_code=200)
def list_symbols(token:str=Depends(get_current_user)):
    return {"ids":ID_CRYPTOS}

@crypto_router.get("/{id}", status_code=200)
async def get_coin_price_by_id(id:str, token:str=Depends(get_current_user)):
    coin= await get_price(id)
    return coin

@crypto_router.get("/{id}/market_cap", status_code=200)
async def get_all_coin_prices(id:str, token:str=Depends(get_current_user)):
    coins= await get_marcketcap(id)
    return coins

@crypto_router.get("/{id}/{days}", status_code=200)
async def get_coin_market_price_data(id:str,date:int, token:str=Depends(get_current_user)):
    coins= await get_market_data(id, date)
    return coins

