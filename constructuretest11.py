#addition using constructure

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("Addition:",self.a+self.b)

obj=Addition(20,60)
obj.add()