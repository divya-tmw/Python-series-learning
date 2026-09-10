#greeting according to time

import datetime

now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour < 12:
    print("good afternoon")
else:
    print("good evening")