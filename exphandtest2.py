dx=[12,3,45,78,76,44,33,67,99,70]

try:
    pos=int(input("Enter the position:"))
    value=int(input("Enter the value:"))

    dx[pos]=value
    print("updated list:",dx)

    ans=pos/value
    print("division is",ans)

except ZeroDivisionError:
    print("cannot divid by zero")

except IndexError:
    print("invalid index entered")

except ValueError:
    print("invalid number entered")

finally:
    print("program execute successfully")
