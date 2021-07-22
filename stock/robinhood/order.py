import os
import robin_stocks.robinhood as rs
from database.orm import DB_Order

# import pandas as pd
# from yahoo_fin import stock_info as si
# import cryptocompare

try:    from stock.robinhood.login import login
except: from login import login
rs = login()

def order(symbol, quantity, side, stop, limit=None):
    print("sell")
    price= stop * quantity

    # cancel previous order
    # order_pending= DB_Order().order_pending(symbol)
    # order_id= order_pending['order_id']
    # rs.orders.cancel_stock_order(order_id)

    response=rs.orders.order(symbol, 
                    quantity, 
                    side, 
                    limitPrice=limit, 
                    stopPrice=stop, 
                    timeInForce='gtc', 
                    extendedHours=False, 
                    jsonify=True)
    print(response)

    # record order 
    order_id= ""
    try:
        order_id= response['id'] 
    except:
        print("stock_order failed")

    DB_Order().updateOrder_pending(symbol, order_id, side, quantity, price, limit, stop)

if __name__ == "__main__":
    print("__name__")
    # buy_by_price_immediately("VOO", 1.0)
    # sell_fractional_by_price_immediately("VOO", 1.0)
    # order_sell_option_limit('TQQQ', 360, 1, 370)

    # order_sell_stop_loss("TQQQ", 1, 108)







# #----------------------sell-----------------------------------------
# def sell_fractional_by_price_immediately(symbol, ammountInDollars):
#     print("sell_fractional_by_price_immediately e.g. QQQ")
#     print(symbol)
#     # rs.orders.order_sell_fractional_by_price('V', 500)
#     response= rs.orders.order_sell_fractional_by_price( symbol,
#                                                         ammountInDollars)
#     print(response)
#     print("$"+str(ammountInDollars), "was sold for", symbol)
#     return response

# def order_sell_limit(symbol, quantity, price): 
#     print("order_buy_limit")
#     response= rs.orders.order_sell_limit(   symbol,
#                                             quantity,
#                                             price,
#                                             timeInForce='gtc',
#                                             extendedHours=False)
#     print(response)
#     print( str(quantity)+ " share", "will be sold for", symbol, "by limit $" + str(price) )
#     return response

# def order_sell_stop_loss(symbol, quantity, price): 
#     rs.orders.order_sell_stop_loss( symbol,
#                                     quantity,
#                                     price,
#                                     timeInForce='gtc',
#                                     extendedHours=False)



# #----------------------buy-----------------------------------------
# def buy_by_price_immediately(symbol, ammountInDollars): #
#     print("buy_by_price_immediately e.g. QQQ")
#     print(symbol)
#     response= rs.orders.order_buy_fractional_by_price(  symbol,
#                                                         ammountInDollars,
#                                                         timeInForce='gtc',
#                                                         extendedHours=False) 
#     print(response)
#     print("$"+str(ammountInDollars), "was placed for", symbol)
#     return response
    
# def order_buy_limit(symbol, quantity, price): 
#     print("order_buy_limit")
#     res= rs.orders.order_buy_limit( symbol,
#                                     quantity,
#                                     price,
#                                     timeInForce='gtc',
#                                     extendedHours=False)
#     print(res)
#     print( str(quantity)+ " share", "will be bought for", symbol, "by limit $" + str(price) )
#     return response


# def stock_order(symbol, quantity, side, stop, limit):
#     print("stock_order")
#     # symbol= 'QQQ'
#     # quantity= 1
#     # side='sell'
#     # limitPrice= 350
#     # stopPrice= 350

#     response=rs.orders.order(symbol, 
#                     quantity, 
#                     side, 
#                     limitPrice=limit, 
#                     stopPrice=stop, 
#                     timeInForce='gtc', 
#                     extendedHours=False, 
#                     jsonify=True)
#     print(response)
#     return response
