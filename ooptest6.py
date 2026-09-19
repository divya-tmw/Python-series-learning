#subraction in oop

class subraction:
    def subx(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the scond number:"))

    def Process(self):
        self.ans=self.n1-self.n2

    def Display(self):
        print("subraction is:",self.ans)

obj=subraction()
obj.subx()
obj.Process()
obj.Display()