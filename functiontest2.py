#sum of digits

def sumdigit(n):
    s=0
    while n>0:#loop jab tak chalega tab tak number 0 nhi hota
        d=n%10 #last digit milti hai----12%10=2
        s=s+d #digit jo mila usko sum mai add kiya
        n=n//10 #10 se last digit remove ho jata hai----12//10=1
    return s

n=int(input("Enter the number:"))

z=sumdigit(n)

print("Sum is:",z)