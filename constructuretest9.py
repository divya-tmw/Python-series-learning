#area of rectangle

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print("Area:",self.length*self.breadth)

r1=rectangle(10,5)
r1.area()