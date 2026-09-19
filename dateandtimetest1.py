#calculate date and time

from datetime import timedelta
from datetime import datetime

now = datetime.now()
print("current date and time:",now)

ans = now + timedelta(days=84)
print("New date is",ans)

ans = now - timedelta(days=45)
print("new date is:",ans)