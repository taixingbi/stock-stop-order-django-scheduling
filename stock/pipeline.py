from stock.updatePeak import updatePeak
from stock.trigerOrder import trigerOrder

import threading
import time

def pipeline():
    # tickers=["QQQ", "TQQQ", "BTC", "DOGE"]
    tickers=["DOGE"]
    for ticker in tickers :
        updatePeak(ticker)
        trigerOrder(ticker)

threading.Thread(target=pipeline).start()

