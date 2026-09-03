#array - insert and display elements

arr = []

n=int(input("Enter the number of elements:"))

for i in range(0,n):
    element=int(input("Enter element:"))
    arr.append(element)

print("array elements are:")

for i in range(n):
    print(arr[i],end=" ")