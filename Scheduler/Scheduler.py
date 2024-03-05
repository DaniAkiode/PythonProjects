import schedule 
import time as tm
from datetime import time, timedelta, datetime


def job():
    print("Get me outta here XD")

#schedule.every(5).seconds.do(job)
#schedule.every().day.at("11:38").do(job)

j = schedule.every(1).to(5).seconds.do(job)

counter = 0 

while True:
    schedule.run_pending()
    tm.sleep(1)
    counter += 1 
    if counter == 10:
        schedule.cancel_job(j)

