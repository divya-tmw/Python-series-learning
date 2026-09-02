#find bigger number

n=int(input("Enter the number:"))
m=int(input("Enter the number:"))

bigger = lambda x,y: x if x>y else y

print("bigger number is:",bigger(n,m))
