#result program

math=int(input("Enter the marks of maths:"))
sci=int(input("Enter the marks of science:"))
eng=int(input("Enter the marks of english:"))

if eng<40 or math<40 or sci<40:
    print("better luck next time")
else:
    print("test is cleared")

    Total = eng+math+sci
    avg=Total*100/300

    print("Total=",Total)
    print("average=",avg)

    #agar marks less than 40n hai toh print karna hai better luck next time
    #agar if condition false hai toh else part mai jayega then wo print karega
    #then sare marks ka total and avg nikalege and wo print karege