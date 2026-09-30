class sample:
    def __init__(self,a=0):
        self.num = a

    def set(self):
        self.n1=100
        self.n2=200
        self.n3=300
        self.n4=400
        self.n5=500
        self.n6=600

    def display(self):
        print("first:",self.n1)
        print("second:",self.n2)
        print("third:",self.n3)
        print("fourth:",self.n4)
        print("fifth:",self.n5)
        print("sixth:",self.n6)

    def __iadd__(self,num):
        self.n1+=num
        self.n2+=num
        self.n3+=num
        self.n4+=num
        self.n5+=num
        self.n6+=num
        return self

val=int(input("Enter the number:"))
obj=sample(val)
obj.set()
print("assigned values are...")
obj.display()
obj+=val
print("updated values are..")
obj.display()