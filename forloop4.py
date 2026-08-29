#GCD(greatest common divisor)
a=12
b=18
for i in range(1,min(a,b)+1): #1 se lekar min(a,b) tak ke numbers ke loop chalega
    if a%i==0 and b%i==0: #agar a aur b dono i se divide ho jaaye to
        gcd=i #gcd ki value i ho jayegi
print(gcd) #jo gcd ki value hai wo print hogi
