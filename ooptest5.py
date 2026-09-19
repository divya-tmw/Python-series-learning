#greater than 2 numbers

class greater:
    def Input(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the second number:"))

    def Display(self):
        if self.n1>self.n2:
            print(self.n1,"is greater")
        else:
            print(self.n2,"is greater")

obj=greater()
obj.Input()
obj.Display()