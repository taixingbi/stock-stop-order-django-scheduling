import os
import robin_stocks.robinhood as rs

def login():
#     print("login")
    robin_user = os.environ.get("robinhood_username")
    robin_pass = os.environ.get("robinhood_password")
    res= rs.login(username=robin_user,
            password=robin_pass,
            expiresIn=86400,
            by_sms=True)
#     print(res)
    return rs


