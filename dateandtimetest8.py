#find days between two dates

import datetime

d1 = datetime.date(2026,9,10)
d2 = datetime.date(2026,9,20)

difference = d2 - d1

print("Days:",difference.days)