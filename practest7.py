#check prime number

num = int(input("Enter the number:"))

if num < 2:
    print("Not prime")
else:
    prime = True

    for i in range(2,num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("not Prime")