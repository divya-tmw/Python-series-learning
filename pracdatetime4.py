#convert date into string

import datetime

today = datetime.date.today()

d = today.strftime("%D/%M/%Y")
print(d)