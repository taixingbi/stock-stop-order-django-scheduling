from datetime import datetime
import time

from database.orm import DB_Hill
from stock.livePrice import livePrice


def updatePeak(ticker):
    # print("updatePeak")
    price= livePrice(ticker)
    peak= DB_Hill().peak(ticker)["peak"]
    valley= DB_Hill().valley(ticker)["valley"]

    if peak < price : # for float, "==" is impossible
        DB_Hill().updatePeak(ticker, price)
        DB_Hill().updateValley(ticker, price)
    
    elif valley > price :
        DB_Hill().updateValley(ticker, price)


if __name__ == "__main__":
    updatePeak("DOGE")
    # livePrice("DOGE") 

    
 