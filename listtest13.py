#bubble sort alogo

n=int(input("Enter the size of list:"))
dx=[]

for j in range(n):
    for i in range(n-1):
        if dx[i]<dx[i+1]:
            dx[i],dx[i+1]=dx[i+1],dx[i]

print("list after sort:",dx)