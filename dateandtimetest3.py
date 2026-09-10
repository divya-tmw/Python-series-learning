#program to demo date time related function

from datetime import date
from datetime import datetime

t = date.today()
print(t)

a = t.year
b = t.month
c = t.day

print(c,"-",b,"-",a)
