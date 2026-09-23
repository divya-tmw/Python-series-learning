#employee details

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Employee:",self.name)
        print("salary:",self.salary)

e1=employee("divya",30000)
e1.display()