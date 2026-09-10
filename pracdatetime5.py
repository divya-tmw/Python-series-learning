#yesterday's date

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

print("Today:",today)
print("Yesterday:",yesterday)