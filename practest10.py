#armstrong number

num = int(input("Enter the number:"))

original = num
total = 0

while num > 0:
    digit = num % 10
    total +=  digit ** 3
    num //= 10

if total == original:
    print("Armstrong number")
else:
    print("not an Armstrong number")