#multi-level inheritance

class first:
    def one(self):
        print("This is one of first")

class second(first):
    def two(self):
        print("This is two of second")

class third(second):
    def three(self):
        print("This is three of third")

obj=third()
obj.one()
obj.two()
obj.three()