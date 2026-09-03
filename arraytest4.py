#find the smallest number in array

arr = [10,20,300,500,40,50]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i
print("smallest number is:",smallest)