#area of circle

class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area:",3.14*self.radius*self.radius)

obj=circle(8)
obj.area()