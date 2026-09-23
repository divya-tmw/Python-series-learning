#simple interest

class interest:
    def __init__(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t

    def calculate(self):
        si=(self.p*self.r*self.t)/100
        print("simple interest:",si)

obj=interest(1000,5,2)
obj.calculate()