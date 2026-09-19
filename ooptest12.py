#find smaller number

class smaller:
    def Input(self):
        self.n1=int(input("Enter the first number:"))
        self.n2=int(input("Enter the second number:"))

    def Display(self):
        if self.n1<self.n2:
            print(self.n1,"is smaller")
        else:
            print(self.n2,"is smaller")

obj=smaller()
obj.Input()
obj.Display()