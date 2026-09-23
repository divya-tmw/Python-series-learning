#Inheritance in python------> reusability,acquiring properties of parent class

class first:
    def one(self):
        print("This is one of first")

class second(first):
    def two(self):
        print("This is two of second")

obj=second()
obj.one()
obj.two()