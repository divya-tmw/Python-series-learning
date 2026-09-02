#largest using list

n=int(input("Enter the size of list:"))
dx=[]

for i in range(n):
    val=int(input("Enter the value:"))
    dx.append(val)
max=dx[0]
min=dx[0]

for i in range(n):
    if dx[i]>max:
        max=dx[i]
    if dx[i]<min:
        min=dx[i]

print("maximum element:",max)
print("minimum element:",min)
    