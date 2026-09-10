import datetime

today = datetime.date.today()
birthday = datetime.date(2007,8,31)

days = today - birthday

print("Days remaining:",days.days)