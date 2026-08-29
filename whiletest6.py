#perfect number program

n=int(input("Enter the number:"))
s=0 #sum=0
p=1 #product=1
temp=n 

while n>0:
    d=n%10
    s=s+d
    p=p*d
    n=n//10

if s+p == temp:
    print(temp,"is perfect number")
else:
    print(temp,"is not perfect number")

#iteration 1
# 59 > 0
# d = 59 % 10 = 9
# s = 0 + 9 = 9
# p = 1 * 9 = 9
# n = 59 // 10 = 5

#iteration 2
# 5 > 0
# d = 5 % 10 = 5
# s = 9 + 5 = 14
# p = 9 * 5 = 45
# n = 5 // 10 = 0