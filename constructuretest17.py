#bank account-deposit & withdraw

class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance + amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
        else:
            print("insufficient balance")

    def display(self):
        print("account holder:",self.name)
        print("balance:",self.balance)

obj=bankaccount("divya",5000)
obj.deposit(2000)
obj.withdraw(1500)
obj.display()
