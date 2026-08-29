#program to display all 3 digits prime-palinj numbrs 131

from moduletest1 import*

for i in range(100,1000):
    if isprime(i)==True and i==Reverse(i):
        print(i)