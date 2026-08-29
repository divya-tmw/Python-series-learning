#factorial......5x4x3x2x1=120

fact=1
n=int(input("Enter the number:"))

for i in range(n,0,-1):
    fact=fact*i

print("factorial is:",fact)


#iteration wise
#n=5
#n=1....1x1=1
#n=2.....1x2=2
#n=3.....2x3=6
#n=4....6x4=24
#n=5....24x5=120.....loop stop