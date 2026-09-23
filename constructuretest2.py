#Passing value to the constructure

class sample:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def Display(self):
        print("Name is:",self.name)
        print("roll number:",self.roll)

roll=int(input("Enter the roll number:"))
name=input("Enter the name:")

obj=sample(roll,name)
obj.Display()