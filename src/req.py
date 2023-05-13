from pydantic import BaseModel

class OrderDetail(BaseModel):
    symbol: str
    typeOrder: str
    side: str
    entry: str
    amount: str