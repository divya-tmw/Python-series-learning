#call by value
# def change(x):
#     x = 20

# a = 10
# change(a)

# print(a)

#call by reference

def change(lst):
    lst.append(20)

a = [10,15]
change(a)

print(a)