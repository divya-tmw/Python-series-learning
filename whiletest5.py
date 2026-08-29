# palindrome check program

n=int(input("Enter the number:"))
rev = 0
temp = n

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if rev == temp:
    print(temp,"is palindrome")
else:
    print(temp,"is not palindrome")


#iteration 1
# 111 > 0
# d = 111 % 10 = 1
#rev = 0 * 10 + 1 = 1
# n = 111 // 10 = 11

#iteration 2
#11 > 0
#d = 11 % 10 = 1
#rev = 1 * 10 + 1 = 11
#n = 11 // 10 = 1

#iteration 3
# 1 > 0
#d = 1 % 10 = 1
#rev = 11 * 10 + 1 = 111
#n = 1 // 10 = 0