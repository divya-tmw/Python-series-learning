#discount program
# 1000-10000 5
#10k-50k 10
#50k-1lac 15
#above 1lac 20

bill=float(input("Enter the bill amount:"))

if bill>=1000 and bill<=10000:
    dis=5
elif bill>=10000 and bill<=50000:
    dis=10
elif bill>=50000 and bill<=100000:
    dis=15
elif bill>=100000:
    dis=20
else:
    dis=0

damt=bill*dis/100
fnl=bill-damt

print("bill amount:",bill)
print(" discount is:",damt)
print("final bill",fnl)