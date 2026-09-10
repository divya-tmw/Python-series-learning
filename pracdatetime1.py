import datetime

dob = datetime.date(2007,8,31)
today = datetime.date.today()

age = today.year - dob.year

print("Date of birth:",dob)
print("Age:",age)