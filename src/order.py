from ib_insync import *
from src.req import OrderDetail

def Order(item: OrderDetail):
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    stock = Forex(item.symbol)
    if item.typeOrder == "MARKET":
        order = MarketOrder(item.side, item.amount)
    else:
        order = LimitOrder(item.side, item.amount, item.entry)
    trade = ib.placeOrder(stock, order)
    print(trade)