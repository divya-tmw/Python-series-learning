#string format time
from datetime import datetime
from datetime import date

curr = datetime.now()
print(curr)

fn = curr.strftime("Day & Date:%A,%B,%D,%Y")
print(fn)

fn = curr.strftime("Time:%I:%M%p")
print(fn)
