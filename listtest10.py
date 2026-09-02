#array search
n=int(input("Enter the size of the list:"))
dx=[]
x=0
for i in range(n):
    val=int(input("Enter the value:"))
    dx.append(val)

val=int(input("Enter the value to be searched:"))

for i in range(n):
    if val==dx[i]:
        print(val,"found at position",i)
        x=i
        break
if x==0:
    print(val,"not found")