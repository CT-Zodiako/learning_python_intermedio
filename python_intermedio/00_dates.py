#dates
from datetime import datetime

now = datetime.now()

timestap = now.timestamp()



year_2023 = datetime(2023,1,1)



def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.timestamp())

print_date(year_2023)


from datetime import time
curren_time = time(13,34,0)

print(curren_time.hour)
print(curren_time.minute)
print(curren_time.second)

from datetime import date

curren_date = date(23,1,1)

print(curren_date.day)
print(curren_date.isoweekday())
print(curren_date.weekday())


