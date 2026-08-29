#GCD
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

gcd=1
m=min(n1,n2)

for i in range(1,m+1):
    if n1%i==0 and n2%i==0:
        gcd=i

print("GCD:",gcd)

#iteration wise
#n=1
#12%1==0  true    18%1==0 true
#gcd=1
#n=2
#12%2==0 true 18%2==0 true
#gcd=2
#n=3
#12%3==0 true 18%3==0 true
#gcd=3
#n=4
#12%4==0 true 18%4==2 false
#gcd=3
#n=5
#12%5==2 false 18%5==3 false
#gcd=3
#n=6
#12%6==0 true 18%6==0 true
#gcd=6
