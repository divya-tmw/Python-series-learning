#tuple program
numbers = (10,20,30,40,40,50)

print("tuple:",numbers)

print("first element:",numbers[0])
print("last element:",numbers[-1])

print("sliced tuple:",numbers[1:4])

print("length:",len(numbers))

print("count of 40:",numbers.count(40))

print("index of 30:",numbers.index(30))

print("maximum:",max(numbers))
print("minimum:",min(numbers))

print("sum:",sum(numbers))

print("tuple elements:")
for i in numbers:
    print(i)

number = (60,70)
print("concatenated tuple:",numbers+number)

print("repetition of tuple:",numbers*3)

if 20 in numbers:
    print("found")
else:
    print("not found")