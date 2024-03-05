import schedule 
from schedule import every, repeat
import time as tm
from datetime import time, timedelta, datetime

@repeat(every(5).seconds, message="Subscibe")
@repeat(every(2).seconds, message="Hey")
def job(message):
    print("Hello the message is:", message)

schedule.every().seconds.do(job, message="HELLO")


while True:
    schedule.run_pending()
    tm.sleep(1)


