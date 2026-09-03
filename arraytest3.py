#find the largest number in array

arr = [10,20,300,500,40,50]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i
print("largest number is:",largest)