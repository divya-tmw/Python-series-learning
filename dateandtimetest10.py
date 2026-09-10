#create date using user input

import datetime

day = int(input("Enter day:"))
month = int(input("Enter month:"))
year = int(input("Enter year:"))

d = datetime.date(year,month,day)

print("date:",d)