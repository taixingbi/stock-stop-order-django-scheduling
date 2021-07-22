from django.conf import settings
from .models import Peak, Valley
from .serializers import PeakSerializer, ValleySerializer, Order_placed

#from .models import Teleconference_transcribe
#from .serializers import Teleconference_transcribeSerializer
from django.http import Http404

import pandas as pd 

class DB_Hill():
    def __init__(self):
        self.print= None
     
    def peak(self, ticker):
        # print("peak")
        e= Peak.objects.filter(symbol= ticker).distinct()
        peak= e.values()[0]
        # print( peak )
        return peak
        #{'id': 1, 'ticker': 'QQQ', 'peak': 253.0, 'timestamp': datetime.datetime(2021, 7, 19, 14, 17, 48, tzinfo=<UTC>)}

    def valley(self, ticker):
        # print("peak")
        e= Valley.objects.filter(symbol= ticker).distinct()
        valley= e.values()[0]
        # print( valley )
        return valley
        #{'id': 1, 'ticker': 'QQQ', 'valley': 253.0, 'timestamp': datetime.datetime(2021, 7, 19, 14, 17, 48, tzinfo=<UTC>)}

    def updatePeak(self, ticker, peak):
        print("updatePeak")   
        e= Peak.objects.filter(symbol=ticker).update(peak=peak)
        print(ticker, "peak go to $", peak, "successfully")

    def updateValley(self, ticker, valley):
        print("updateValley")   
        e= Valley.objects.filter(symbol=ticker).update(valley=valley)
        print(ticker, "valley go to $", valley, "successfully")

class DB_Order():
    def __init__(self):
        print("DB_Order")

    def updateOrder_placed(self, symbol, order_id, side, quantity, price, limit, stop):
        print("updateOrder_placed")
        Order_placed.objects.filter(symbol=symbol).update(
            symbol= symbol,
            order_id= order_id,
            side= side,
            quantity= quantity,
            price= price,
            limit= limit,
            stop= stop)

        print("Order_placed", id, "successfully")

    def order_placed(self, symbol):
        print("updateOrder_placed")
        e= Order_placed.objects.filter(symbol=symbol).distinct()
        order_placed= e.values()[0]
        print( order_placed )
        return order_placed



    # def update(self, filename=None, transcription=None):
    #     try:
    #         e= Teleconference_transcribe.objects.filter( filename= filename )
    #     except:
    #         raise Http404("can not access to mysql")

    #     serializer = Teleconference_transcribeSerializer( e, many=True)
        
    #     if not serializer.data:
    #         raise Http404("filename can not found in table")

    #     row= e.update(transcription_baseline= transcription)
    #     print("successfully update db ")

    #     return serializer.data
     








         
 #print(timeslot)

        # today= datetime.date.today() 
        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)

        # minute = datetime.timedelta(minutes=500)
        # today= datetime.date.today() 
        # now= datetime.datetime.now()
     

        # print("st    ", datetime.datetime(2019, 11, 15, 15, 30) )
        # x=              datetime.datetime.utcnow()
        # x=              datetime.datetime(2019, 11, 15, 16, 30) 
        # x= now
        # print("xx    ", x )
        # print("ed    ", datetime.datetime(2019, 11, 15, 17, 30))

     
        #inSlot_ = Timeslot.objects.filter(start_date__lt= x, end_date__gt= x)

        #inSlot= Timeslot.objects.filter( start_date__lt= now + minute ).filter( end_date__gt= now - minute )

        #inSlot= Timeslot.objects.filter( start_date__lt= now ).filter( end_date__gt= now ) # utc

        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)
        #2019-11-15 15:30:00  -  2019-11-15 16:30:00