try:    from stock.robinhood.login import login
except: from login import login

# robin_user = os.environ.get("robinhood_username")
# robin_pass = os.environ.get("robinhood_password")
# rs.login(username=robin_user,
#         password=robin_pass,
#         expiresIn=86400,
#         by_sms=True)

rs = login()

def buyingPower():
    print("buyingPower")
    account=  rs.account.load_phoenix_account()
    amount=  account['account_buying_power']['amount'] 
    print(amount)
    return amount

def tickerInfo(ticker):
    print( "tickerInfo",  ticker)
    Ticker= rs.account.build_holdings()[ticker]  
    print(Ticker)
    return Ticker

def completed_stock_orders():
    rs.export.export_completed_stock_orders("","order_history")


if __name__ == "__main__":
    # buyingPower()
    # tickerInfo("VOO") # .["price"] .["quantity"] .["equity"]
    # completed_stock_orders()

    res = rs.stocks.get_stock_historicals("TQQQ", interval="day", span="week")
    print(res[0])