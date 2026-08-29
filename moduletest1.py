#module
#sum of digits

def Sumofdigits(n):
    s=0
    while n>0:
        d=n%10
        s=s+d
        n=n//10
    return s

#reverse

def Reverse(n):
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

#is prime

def isprime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
        break
    return flag
