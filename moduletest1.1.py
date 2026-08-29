from moduletest1 import*

n=int(input("Enter the number:"))

ans=Sumofdigits(n)
print("sum of digits=",ans)

ans=Reverse(n)
print("Reverse is",ans)

if isprime(n)==True:
    print(n,"is not prime")
else:
    print(n,"is not prime")