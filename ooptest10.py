#even or odd

class number:
    def check(self,n):
        if n % 2 == 0:
            print("Even")
        else:
            print("odd")

obj=number()
obj.check(10)