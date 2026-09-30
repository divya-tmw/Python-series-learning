#student marks calculator

class student:

    def calculator(self,marks1,marks2=0,marks3=0,marks4=0):
        total = marks1 + marks2 + marks3 + marks4
        return total

s = student()

print("Marks of student 1:")
total1 = s.calculator(80)
print("total marks:",total1)


print("Marks of student 2:")
total2 = s.calculator(80,75)
print("total marks:",total2)


print("Marks of student 3:")
total3 = s.calculator(80,75,90)
print("total marks:",total3)


print("Marks of student 4:")
total4 = s.calculator(80,75,90,85)
print("total marks:",total4)