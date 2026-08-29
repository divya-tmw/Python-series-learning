#sum digits of a number

n=int(input("Enter the number:"))
s=0 #----sum=0

while n>0: #----n is greater than 0
    d=n%10 
    s=s+d
    n=n//10

print("sum of digits:",s)

#1st iteration
# 12 > 0
# d = 12 % 10 = 2 ---- last digit
# s = 0 + 2 = 2
# n = 12 // 10 = 1-----first digit

#2nd iteration
#d = 1 % 10 = 1
#s = 2 + 1 = 3
#n = 1 // 10 = 0