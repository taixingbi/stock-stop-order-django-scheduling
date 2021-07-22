import os
import robin_stocks.robinhood as rs

import pandas as pd

from yahoo_fin import stock_info as si
import cryptocompare

try:    from stock.robinhood.login import login
except: from login import login
rs = login()

#----------------------sell-----------------------------------------
def sell_crypto_price_immediately(symbol, ammountInDollars):
    print("sell_crypto_price_immediately e.g. BTC DOGE ETC")
    # rs.orders.order_buy_fractional_by_price(symbol,
    response= rs.orders.order_sell_crypto_by_price(symbol, 
                                    ammountInDollars)
    print(response)
    print("$"+str(ammountInDollars), "was sold for", symbol)

#----------------------buy-----------------------------------------
def buy_crypto_price_immediately(symbol, ammountInDollars):
    print("buy_crypto_price_immediately e.g. BTC DOGE ETC")
    # rs.orders.order_buy_fractional_by_price(symbol,
    response= rs.orders.order_buy_crypto_by_price(symbol, 
                                    ammountInDollars,
                                    timeInForce='gtc'
                                    )
    print(response)
    print("$"+str(ammountInDollars), "was placed for", symbol)

# def buy_crypto_limit(symbol, share, limit):
#     print("buy_crypto_limit e.g. BTC DOGE ETC")
#     # rs.orders.order_buy_fractional_by_price(symbol,
#     response= rs.orders.order_buy_crypto_limit('BTC',     
#                                     share,
#                                     limit,
#                                     timeInForce='gtc'
#                                     )
#     print(response)
#     print("$"+str(share), "was placed for", symbol, "at limit $" + str(limit) )

if __name__ == "__main__":
    # sell_fractional_by_price_immediately("VOO", 1.0)
    order_sell_option_limit('QQQ', 360, 1, 370)



