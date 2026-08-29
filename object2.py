#employee class with user input

class employee:
    def __init__(self,name,salary,age,city):
        self.name = name
        self.salary = salary
        self.age = age
        self.city = city
    def display(self):
        print("Name:",self.name)
        print("salary:",self.salary)
        print("age:",self.age)
        print("city:",self.city)
name = input("Enter your name:")
salary = int(input("enter your salary:"))
age = int(input("enter your age:"))
city = input("enter your city:")

e1 = employee(name,salary,age,city)
e1.display()