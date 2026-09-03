#count even and odd numbers in array

arr = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("even numbers:",even)
print("odd numbers:",odd)
