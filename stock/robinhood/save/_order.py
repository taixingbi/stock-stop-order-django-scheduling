import os
import robin_stocks.robinhood as rs

import pandas as pd

from yahoo_fin import stock_info as si
import cryptocompare

try:    from stock.robinhood.login import login
except: from login import login
rs = login()

#----------------------sell-----------------------------------------
def sell_fractional_by_price_immediately(symbol, ammountInDollars):
    print("sell_fractional_by_price_immediately e.g. QQQ")
    print(symbol)
    # rs.orders.order_sell_fractional_by_price('V', 500)
    response= rs.orders.order_sell_fractional_by_price( symbol,
                                                        ammountInDollars)
    print(response)
    print("$"+str(ammountInDollars), "was sold for", symbol)


def order_sell_option_limit(symbol, ask_price, quantity, strike):
    print("order_sell_option_limit")
    # rs.orders.order_sell_option_limit('open',
    #                                 'credit',
    #                                 ask_price, #The limit price to trigger a sell of the option.
    #                                 symbol,
    #                                 quantity,
    #                                 '2021-07-25',
    #                                 strike, #The strike price of the option.
    #                                 optionType='call',
    #                                 timeInForce='gtc')
    rs.orders.order_sell_option_limit(  'open',
                                        'credit',
                                        '350',
                                        'QQQ',
                                        1,
                                        '2021-07-25',
                                        345,
                                        optionType='call',
                                        timeInForce='gtc')


def sell_crypto_price_immediately(symbol, ammountInDollars):
    print("sell_crypto_price_immediately e.g. BTC DOGE ETC")
    # rs.orders.order_buy_fractional_by_price(symbol,
    response= rs.orders.order_sell_crypto_by_price(symbol, 
                                    ammountInDollars)
    print(response)
    print("$"+str(ammountInDollars), "was sold for", symbol)

#----------------------buy-----------------------------------------
def buy_by_price_immediately(symbol, ammountInDollars): #
    print("buy_by_price_immediately e.g. QQQ")
    print(symbol)
    response= rs.orders.order_buy_fractional_by_price(symbol,
                                       ammountInDollars,
                                    #    timeInForce='gtc',
                                       extendedHours=False) 
    print(response)
    print("$"+str(ammountInDollars), "was placed for", symbol)
    return response
    
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



# print( rs.account.get_all_positions() )

# orders= rs.get_all_open_crypto_orders()
# for order in orders:
#     print( order)


# print(rs.export_completed_stock_orders)

# price = rs.stocks.get_latest_price('TELA', includeExtendedHours=True)
# orders= rs.get_all_open_stock_orders()
# for order in orders:
#     print( order )


if __name__ == "__main__":
    # sell_fractional_by_price_immediately("VOO", 1.0)
    order_sell_option_limit('QQQ', 360, 1, 370)



