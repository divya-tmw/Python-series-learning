#menu driven program

print("11:hindi \n22:english \n33:marathi \n44:gujrati")

ch=int(input("enter your choice:"))

match ch:
    case 11: print("hindi selected")
    case 22: print("english selected")
    case 33: print("marathi selected")
    case 44: print("gujrati selected")
    case _: print("invalid choice")
