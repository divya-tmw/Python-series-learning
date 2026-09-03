#find maximum of two numbers

def maximum(a,b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

print("maximum:",maximum(x,y))