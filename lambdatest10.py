#check positive negative

n=int(input("Enter the number:"))

check = lambda x: "Positive" if x>0 else "Negative"

print(check(n))