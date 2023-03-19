
import datetime
from datetime import datetime
import time

today = '2023-03-02'
datetime_today = datetime.strptime(today + '-00:00:00', "%Y-%m-%d-%H:%M:%S") 
print(datetime_today)

ttt = '1677750165.2035372'
time_now = time.strftime("%Y/%m/%d-%H:%M:%S", time.localtime(float(ttt)))

datetime_object = datetime.strptime(time_now, "%Y/%m/%d-%H:%M:%S")

print(datetime_today, datetime_object)
if datetime_object > datetime_today:
    print("hi")