#count character in string

text = input("Enter a string")
ch = input("Enter character to count:")

count = 0

for x in text:
    if x == ch:
        count += 1

print("characters occurs",count,"times")




























