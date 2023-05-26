from ib_insync import *
from src.req import OrderDetail
from src.dc import SendMess


class MakeOrder:
    def __init__(self):
        util.startLoop()
        self.allOrders = []
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7497, clientId=1)
        with open("token.txt", "r") as readToken:
            self.token = readToken.read().replace("\n", '')
        with open("channel.txt", "r") as readChannel:
            self.channelID = int(readChannel.read().replace("\n", ''))

    def Order(self, item: OrderDetail):
        self.CloseAllOrders(item.symbol)
        self.CloseAllPositions(item.symbol)
        stock = Forex(item.symbol)
        if item.typeOrder == "MARKET":
            order = MarketOrder(item.side, item.amount)
        else:
            order = LimitOrder(item.side, item.amount, item.entry)
        trade = self.ib.placeOrder(stock, order)
        self.allOrders.append([item.symbol, order])
        message = f"Placed order: [{item.symbol}]: {item.side} {item.typeOrder} {item.amount} at {item.entry}\n\n\n"
        message += f"Result: {str(trade)}\n"
        SendMess(self.token, message,self.channelID)
        print(trade)
        
    def CloseAllOrders(self, symbol: str):
        for sym, order in self.allOrders:
            if sym == symbol:
                self.ib.cancelOrder(order)
                self.allOrders.remove([sym, order])
                
    def CloseAllPositions(self, symbol: str):
        ib = self.ib
        for openTrade in ib.positions():
            direction = 'BUY' if openTrade.position < 0 else 'SELL'
            if openTrade.contract.symbol == symbol:
                order = MarketOrder(direction, abs(openTrade))
                ib.placeOrder(openTrade.contract, order)