#rectangle class

class rectangle:
    def __init__(self,length,breadth):  
        self.length = length
        self.breadth = breadth
    def area(self):
        print("Area:",self.length*self.breadth)

r = rectangle(10,2)
r.area()