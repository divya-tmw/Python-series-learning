#perimeter of rectangle

class Rectangle:
    def perimeter(self,length,breadth):
        return 2 * (length * breadth)

obj=Rectangle()
print(obj.perimeter(10,5))