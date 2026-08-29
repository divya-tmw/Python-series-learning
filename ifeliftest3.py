#result extended program

eng=int(input("Enter the marks of english:"))
sci=int(input("Enter the marks of science:"))
math=int(input("Enter the marks of maths:"))

if eng<=0 or eng>=100 or  sci<=0 or sci>=100 or math<=0 or math>=100:
    print("invalid number entered:")
elif eng<=40 or sci<=40 or math<=40:
    print("better luck next time")
else:
    total=eng+sci+math
    avg=total/3
    print("test is cleared")
    print("total is:",total)
    print("average is:",avg)

    if avg<60:
        print("class:passclass")
    elif avg<75:
        print("class:firstclass")
    else:
        print("class:distinction")