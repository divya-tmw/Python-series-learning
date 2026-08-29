#age message

age=int(input("Enter the age:"))

if age>=1 and age<=12:
    print("you are minor")
elif age>=13 and age<=17:
    print("you are teenager")
elif age>=18 and age<=60:
    print("you are adult")
elif age>=61 and age<=120:
    print("you are senior citizen")
else:
    print("invalid age entered")