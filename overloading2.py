#different types

class student:
    def show(self,name,age=None):
        if age is None:
            print("Name:",name)
        else:
            print("Name:",name)
            print("Age:",age)

s = student()

s.show("Divya")
s.show("Divya",19)