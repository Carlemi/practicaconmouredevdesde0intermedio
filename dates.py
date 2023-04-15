## Dates

from datetime import datetime   #capaz de agrupar los dos tipos de datos

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023, 5, 1) #si no le damos más parametros el los arroja como 0 

print_date(year_2023)

from datetime import time  #solo agrupa la parte de hora

current_time = time(21, 6, 0)  #time no es igual a datatime

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date  #solo agrupa la parte de fecha 

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 5, 10)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date #si los objetos son del mismo tipo, se pueden restar
print(diff)

print(year_2023.time())

from datetime import timedelta ## trabajar con franjas de fechas

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 15)

print(end_timedelta -start_timedelta)
print(end_timedelta + start_timedelta)
