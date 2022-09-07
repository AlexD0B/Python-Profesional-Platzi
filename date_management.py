from datetime import datetime


import datetime

my_datetime = datetime.datetime.now()
print(my_datetime)

"""today = datetime.date.today()
print(today)

print(f'Year: {today.year}')
print(f'Month: {today.month}')
print(f'Day: {today.day}')"""

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato Latam: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el mes %m')
print(f'Formato ramdon: {my_str}')