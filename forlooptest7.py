#prime check
n=int(input("Enter the number:"))
c=0

for i in range(1,n+1):
    if n%i==0:
        print(i)
        c=c+1

print("count:",c)

#iteration wise
#i=1.....7%1==0  count=1 fcator
#i=2.....7%2==1  count=1
#i=3.....7%3==1  count=1
#i=4.....7%4==1  
#i=5.....7%5==1 
#i=6......7%6==1 
#i=7......7%7=0 factor count=2