#inheritance example

class person:
    def show(self):
        print("I am a person")

class student(person):
    def display(self):
        print("I am a student")

s = student()
s.show()
s.display()