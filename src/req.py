from pydantic import BaseModel

class OrderDetail(BaseModel):
    symbol: str #FX symbol
    typeOrder: str # MARKET or LIMIT
    side: str # BUY or SELL
    entry: str
    amount: str