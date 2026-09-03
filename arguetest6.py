#varaible length arguements

def total(*numbers):
    sum=0

    for i in numbers:
        sum = sum + i

    print("total =",sum)

total(10,20,30,40,50)