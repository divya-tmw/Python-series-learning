#bank account class

class Bank:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def display(self):
        print("balance:",self.balance)

b = Bank(1000)
b.deposit(500)
b.display()
