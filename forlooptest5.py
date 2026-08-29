#fibonnaci series

a=0
b=1
n=int(input("Enter the number:"))

for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

#iteration wise
#n=5  
#print a....0 print hoga
#c=a+b....c=0+1=1
#a=b....a=1
#b=c....b=1
#first iteration k end mai 1 1 1

#a=1....b=1
#c=a+b.....c=1+1=2
#a=1
#b=2
#........1 2 2

#a=1...b=2
#c=a+b.....c=1+2=3
#a=2
#b=3
#2 3 3

#a=2.....b=3
#c=a+b........c=2+3=5
#a=3
#b=5
#3 5 5

#a=3  b=5
#c=a+b......c=3+5=8
#a=5
#b=8
#5 8 8