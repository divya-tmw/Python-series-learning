#delete an element

arr = [10,20,30,40,50,60]
num=int(input("Enter the element to be deleted:"))

if num in arr:
    arr.remove(num)
    print("array after deletion:",arr)
else:
    print("element not found")

print(arr)