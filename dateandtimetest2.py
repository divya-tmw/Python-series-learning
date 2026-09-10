#calculate days between dates

from datetime import date

date1 = date.today()
date2 = date(2027,8,21)

ans = date2 - date1

print("Difference in days:",ans.days)