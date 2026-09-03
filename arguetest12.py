#calculate simple interest

def interest(principle,rate,time):
    si = (principle * rate * time) / 100
    return si

p=float(input("Enter principle:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))

print("simple interest:",interest(p,r,t))