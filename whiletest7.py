#count the digits

n=int(input("Enter the number:"))
temp=n
count=0

while n>0:
    count=count+1
    n=n//10

print(temp,"is",count,"digit number")


#iteration 1
# 233 > 0
#count = 0 + 1 = 1
# n = 233 // 10 = 23

#iteration 2
# 223 > 0
# count = 1 + 1 = 2
# n = 23 // 10 = 2

#iteration 3
# 2 > 0
#count = 2 + 1 = 3
# n = 3 // 10 = 0