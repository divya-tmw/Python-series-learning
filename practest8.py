#remove duplicate elements

number = [10,20,30,30,10,40,50,60,70,80,10]

unique = []

for num in number:
    if num not in unique:
        unique.append(num)

print("Original:",number)
print("Without duplicates:",unique)