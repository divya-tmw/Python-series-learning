#addition 2.0

class Addition2:
    def Input(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the second number:"))

    def Process(self):
        self.ans=self.n1+self.n2

    def Display(self):
        print("Addition is:",self.ans)

obj=Addition2()
obj.Input()
obj.Process()
obj.Display()




























