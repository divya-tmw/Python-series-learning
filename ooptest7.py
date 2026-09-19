#division in oop

class division():
    def divix(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the second number:"))

    def Display(self):
        self.ans=self.n1/self.n2

    def Output(self):
        print("division is:",self.ans)

obj=division()
obj.divix()
obj.Display()
obj.Output()
