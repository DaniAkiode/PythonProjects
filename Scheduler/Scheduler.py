import schedule 
import time as tm
from datetime import time, timedelta, datetime


def job():
    print("Get me outta here XD")

#schedule.every(5).seconds.do(job)
#schedule.every().day.at("11:38").do(job)

schedule.every().minute.at(":40").do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)
