#student class

class student:
    def __init__(self,name,rollno,cource): 
        self.name = name
        self.rollno = rollno
        self.cource = cource
    def display(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("cource:",self.cource)

s1=student("divya",50,"BSCit")
s1.display()