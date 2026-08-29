#even odd using function

# def evenOdd(x):
#     if (x % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"

# print(evenOdd(16))
# print(evenOdd(7))


#default function

# def fun(x,y=50):
#     print("x:",x)
#     print("y:",y)

# fun(40)


#####function without arguements

# def greet():
#     print("hello,welcome")

# greet()


#####function with arguments

# def add(a,b):
#     print("sum",a+b)

# add(10,20)


######function with return value

# def add(a, b):
#     return a + b

# result = add(15, 25)
# print("Sum =", result)

####find maximum number

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

print("Maximum =", maximum(n1,n2))
