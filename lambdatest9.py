#area of rectangle using lambda

length = int(input("Enter the length:"))
breadth = int(input("Enter the breadth:"))

area = lambda x,y:x*y

print("area of rectangle:",area(length,breadth))