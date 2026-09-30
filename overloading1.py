class calculator:
    def add(self,a,b=0,c=0):
        return a + b + c

obj = calculator()

print(obj.add(5))
print(obj.add(5,10))
print(obj.add(5,10,15))