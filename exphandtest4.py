try:
    numbers = [10,20,30,40,50]
    result = numbers + 5

    print(result)

except TypeError:
    print("list and integer cannot be added")