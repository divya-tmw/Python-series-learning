# neon number program

n=int(input("Enter the number:"))

sq = n * n #square of the number
s = 0

while sq > 0:
    d = sq % 10
    s = s + d
    sq = sq // 10

if n == s:
    print(n,"is a neon number")
else:
    print(n,"is not a neon number")


# starting 
# num = 9 ------- sq = 9 * 9 = 81-------sum = 0

#1st  iteration               #1st iteration
# 81 > 0                      1 > 0
# d = 81 % 10 = 1             d = 1 % 10 = 1
# s = 0 + 1 = 1               s = 0 + 1 = 1
# 81 // 10 = 8                1 // 10 = 0


#2nd iteration
# 8 > 0
# d = 8 % 10 = 8
# s = 0 + 8 = 8
# sq = 8 // 10 = 0


