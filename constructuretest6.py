#hierarchy

class first:
    def one(self):
        print("This is one of first")

class second(first):
    def two(self):
        print("This is two of second")

class third(first):
    def three(self):
        print("This is three of third")

obj1=second()
obj1.one()
obj1.two()

obj2=third()
obj2.one()
obj2.three()