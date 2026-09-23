#simple calculator

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def calculate(self):
        print("Addition:",self.a+self.b)
        print("subraction:",self.a-self.b)
        print("multiplication:",self.a*self.b)

obj=Calculator(10,5)
obj.calculate()