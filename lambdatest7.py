#check even odd

n = int(input("Enter the number:"))

check = lambda x: "Even" if x%2==0 else "Odd"

print(check(n))