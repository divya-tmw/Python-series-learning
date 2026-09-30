class sample:
    def __init__(self,a=0,b=0):
        self.n1=a
        self.n2=b

    def Display(self):
        print("n1=",self.n1)
        print("n2=",self.n2)

    def __add__(self,objx):
        ans=sample()
        ans.n1=self.n1+objx.n1
        ans.n2=self.n2+objx.n2
        return ans
o1 = sample(100,200)
o2 = sample(55,77)
o3 = sample()

o3 = o1 + o2

o3.Display()
