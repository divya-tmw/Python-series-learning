###check if element exit or not

s = {10, 20, 30}

num = int(input("Enter a number: "))

if num in s:
     print("Element Found")
else:
     print("Element Not Found")

####remove duplicate elements

numbers = [10, 20, 20, 30, 40, 40, 50]

unique = set(numbers)

print(unique)