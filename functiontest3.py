#return with multiple values

def FindMax(arr):
    a1=max(arr)
    a2=min(arr)
    a3=sum(arr)

    return a1,a2,a3

n=int(input("Enter the number:"))

dx=[]

for i in range(n):
    val=int(input("Enter the value:"))
    dx.append(val)

z=FindMax(dx)

print("largest is:",z[0])
print("smallest is:",z[1])
print("sum is:",z[2])