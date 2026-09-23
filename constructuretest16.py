#students marks

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def Display(self):
        print("Name:",self.name)
        print("marks:",self.marks)

s1=student("Divya",85)
s1.Display()