#subtraction using lambda

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

sub = lambda x,y:x-y

print("subtraction:",sub(a,b))