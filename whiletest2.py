#reverse number program 

n=int(input("Enter the number:"))
r=0 #reverse=0

while n>0:
    d=n%10
    r=r*10+d
    n=n//10

print("reverse of number:",r)

# 1st iteration

# 234 > 0
# d = 234 % 10 =4-----last digit
#r = 0 * 10 + 4 = 4
# 234 // 10 = 23

#2nd iteration
# d = 23 % 10 = 3
#r = 4 *10 + 3 = 43
# 23 // 10 = 2

#3rd iteration
# d = 2 % 10 = 2
#r = 43 * 10 + 2 = 432
# 2 // 10 = 0

