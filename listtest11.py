#count the occurence of array elements

n=int(input("Enter the size of the list:"))
dx=[]
x=0
c=0
for i in range(n):
    val=int(input("Enter the value:"))
    dx.append(val)

val=int(input("Enter the value to be searched:"))

for i in range(n):
    if val==dx[i]:
        c=c+1
        x=1

if x==0:
    print(val,"not found")
else:
    print(val,"found",c,"times")