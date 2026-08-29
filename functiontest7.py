#lambda function

add = lambda x,y:x+y

circle = lambda rad:3.14*rad**2

v1=int(input("Enter the first number:"))
v2=int(input("Enter the second number:"))

ans=add(v1,v2)
print("addition is:",ans)

ans=circle(v1)
print("area of circle is:",ans)


