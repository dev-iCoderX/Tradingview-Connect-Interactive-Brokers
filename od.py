from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Forex('EURUSD')

order = MarketOrder('LONG', 10)

trade = ib.placeOrder(stock, order)

print(trade)