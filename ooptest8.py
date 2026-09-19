#multiplication in oop

class multiplication:
    def multix(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the second number:"))

    def display(self):
        self.ans=self.n1*self.n2

    def output(self):
        print("multiplication is",self.ans)

obj=multiplication()
obj.multix()
obj.display()
obj.output()