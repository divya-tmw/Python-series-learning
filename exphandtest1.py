
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

try:
    ans=n1/n2
    print("division is",ans)

except ZeroDivisionError:
    print("cannot divid by zero")