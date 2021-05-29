from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

VS_CURRENCIRES="usd"
ID_CRYPTOS=[
    "bitcoin",
    "ethereum",
    "litecoin",
    "cardano",
    "ripple",
]

async def get_price(id):
    coin= cg.get_price(id, vs_currencies=VS_CURRENCIRES)
    return coin

async def get_marcketcap(id):
    coin= cg.get_price(id, vs_currencies=VS_CURRENCIRES, include_market_cap=True)
    return coin

async def get_market_data(id, days):
    data= cg.get_coin_market_chart_by_id(id, vs_currency=VS_CURRENCIRES, days=days)
    return data