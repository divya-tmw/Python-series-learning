#star pattern

# for j in range(1,6):
#     for i in range(1,j+1):
#         print("*",end =" ")
#     print()

#####reverse star pattern

# for j in range(5,0,-1):
#     for i in range(1,j+1):
#         print("*",end = " ")
#     print()


#####pyramid pattern

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("* " * i)


####inverted pyramid pattern

# n = int(input("Enter number of rows: "))

# for i in range(n, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)

####diamond pattern

# n = int(input("Enter number of rows: "))

# # Upper half
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("* " * i)

# # Lower half
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)


###hallow square pattern
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
