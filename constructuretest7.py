#hybrid

#student
#  |
# test     sports
#   |_________|
#        |
#      result

class student:
    def sinput(self):
        self.roll=int(input("Enter the roll number:"))
        self.name=input("Enter the name:")

class test(student):
    def tinput(self):
        self.eng=int(input("Enter the marks of english:"))
        self.math=int(input("Enter the marks of maths:"))
        self.sci=int(input("Enter the marks of science:"))

class sports:
    def spinput(self):
        self.grade=input("Enter the grade in sports:")

class result(test,sports):
    def calc(self):
        self.total=self.eng+self.math+self.sci
        self.avg=self.total/3

    def Display(self):
        print("roll number:",self.roll,"\nname:",self.name)
        print("english:",self.eng,"\nmaths:",self.math,"\nscience:",self.sci)
        print("total:",self.total,"\naverage:",self.avg)
        print("sports grade:",self.grade)

obj=result()
obj.sinput()
obj.tinput()
obj.spinput()
obj.calc()
obj.Display()