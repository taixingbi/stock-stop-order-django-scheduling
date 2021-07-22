from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from stock.pipeline import pipeline

def job():
    print("\n job",datetime.now())
    pipeline()

def start():
    print("apscheduler start..")
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=10)
    scheduler.start()
    