from datetime import datetime
import time
from database.orm import DB_Hill, DB_Order
from stock.robinhood import order
from stock.livePrice import livePrice

PERCENTAGE= 0.9  

class Price:
    def __init__(self, symbol):
        self.peak= DB_Hill().peak(symbol)['peak']
        self.valley= DB_Hill().valley(symbol)['valley']

    def peak(self):
        return self.peak

    def valley(self):
        return self.valley

    def high(self):
        # print("high")
        high= self.peak * PERCENTAGE - 0.001 # 0.9 + 0.01 = 0.901
        return high

    def middle(self):
        # print("middle")
        middle= self.peak * PERCENTAGE
        return middle

    def low(self):
        # print("low")
        low= self.peak * PERCENTAGE - 0.001 # 0.9 - 0.01 = 0.899
        return low

# ----------------high--------------- 90.1%

# ................................... 90%

# ----------------low---------------- 89.9%

def trigerOrder(symbol):
    print("trigerOrder")

    symbol= 'DOGE'
    liveprice= livePrice(symbol)
    price= Price(symbol)

    order_placed= DB_Order().order_placed(symbol)
    last_side= order_placed['side'] # buy/sell
    quantity= order_placed['quantity'] # buy/sell

    # sell
    # last side is buy
    if last_side =='buy' or last_side =='init':
        if price.middle() < liveprice and liveprice < price.high() : # e.g. 0.9
            print("order.order(symbol, quantity, 'sell', price.midlle() )")
            # order.order(symbol, quantity, 'sell', price.midlle() )

    # buy
    # last side is sell
    if last_side =='sell':
        if price.low() < liveprice  and liveprice < price.middle()  : # e.g. 0.9
            print("order.order(symbol, quantity, 'buy', price.midlle() )")
            # order.order(symbol, quantity, 'buy', price.midlle() )

        if price.low() < price.valley() and price.high() < liveprice   : # e.g. 0.9
            print("order.order(symbol, quantity, 'buy', price.peak() ) # buy live price ")
            # order.order(symbol, quantity, 'buy', price.peak() ) # buy live price 


if __name__ == "__main__":
    updatePeak("DOGE")
    # livePrice("DOGE") 

    
 
# def sellFailToStopPrice(symbol):
#     sellStopPrice= updatePeak(symbol) * (1 - PERCENTAGE)
#     print("sellStopPrice", sellStopPrice)
#     return stopPrice

# def buyRaiseToStopPrice(symbol):
#     buyStopPrice= updatePeak(symbol) * (1 - PERCENTAGE)
#     print("buyStopPrice", buyStopPrice)
#     return buyStopPrice