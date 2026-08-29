#lead number program

n=int(input("Enter the number:"))

temp = n
se = 0 #sum of even
so = 0 #sum of odd

while n>0:
    d=n%10

    if d%2==0:
        se += d
    else:
        so += d
    n=n//10

if so == se:
    print(temp,"is a lead number")
else:
     print(temp,"is not a lead number")

#iteration 1
#n > 1322
# d = 1322 % 10 = 2

# 2 % 2 == 0
#se = 0 + 2 = 2
#n = 1322 // 10 = 132

#iteration 2
#n >132
#d = 132 % 10 = 2

#se = 2 + 2 = 4-----------
#n = 132 // 10 = 13

#iteration 3
#n > 13
#d = 13 % 10 = 3

#so = 0 + 3 = 3
#n = 13 // 10 = 1

#iteration 4
#n > 1
#d = 1 % 10 = 1

#so = 3 + 1 = 4---------
#n = 1 // 10 = 0