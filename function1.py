#passing value of the same type to the function

# def addition(a,b): #define
#     ans = a + b
#     print("addition is",ans)

# n1=int(input("Enter the first number:"))
# n2=int(input("Enter the second number:"))

# addition(n1,n2)


#square pattern-------any pattern

# def pattern(n,ch):
#     for i in range(n):
#         for j in range(n):
#             print(ch,end=' ')
#         print()

# n=int(input("Enter the number:"))
# ch=input("Enter the character:")

# pattern(n,ch)

#passing list to the function

def Findmax(arr):
    n1 = max(arr)
    n2 = min(arr)
    n3 = sum(arr)

    print("sum =", n3, "max =", n1, "min =", n2)

dx=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    val=int(input("Enter the number:"))
    dx.append(val)

Findmax(dx)
