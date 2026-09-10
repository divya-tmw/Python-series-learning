from datetime import datetime
from datetime import date

curr = datetime.now()
print(curr)

hr = datetime.now().hour
mn = datetime.now().minute
dx = datetime.now().day
yr = datetime.now().year

print("Hour:",hr,"\nminute:",mn,"\nday:",dx,"\nyear:",yr)