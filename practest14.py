#count uppercase and lower case

text = input("Enter a string:")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("uppercase:",upper)
print("Lowercase:",lower)