#armstrong number

n=int(input("Enter the number:"))
temp=n
s=0

while n>0:
    d = n % 10
    cube = d ** 3
    s = s + cube
    n = n // 10

if s == temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not a armstrong number")

#1st iteration
# 153 > 0
# d = 153 % 10 = 3
# cube = 3 ** 3---27
# s = 0 + 27 = 27
#  n = n // 10---153 // 10 = 15

#2nd iteration
#15 > 0
# d = 15 % 10 = 5
# cube = 5 ** 3 = 125
# s = 27 + 125 = 152
# n = 15 // 10 = 1

#3rd iteration
# 1 > 0
#d = 1 % 10 = 1
# cube = 1 ** 3 = 1
# s = 152 + 1 = 153
# n = 1 // 10 = 0

