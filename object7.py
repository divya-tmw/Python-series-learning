class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee:",self.name)
        print("salary:",self.salary)

e1=Employee("divya",255000)
e2=Employee("krishna",450000)

e1.display()
e2.display()