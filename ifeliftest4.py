#character check program

ch=input("Enter the character:")

if ch>='a' and ch<='z':
    print(ch,"is small alphabet")
elif ch>='A' and ch<='Z':
    print(ch,"is capital alphabet")
elif ch>='0' and ch<='9':
    print(ch,"is digits")
else:
    print(ch,"is special character")