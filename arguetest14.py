#add any numbers of values

def add(*numbers):
    total = 0

    for n in numbers:
        total = total + n
    return total
print("total:",add(10,20,30,40,20))