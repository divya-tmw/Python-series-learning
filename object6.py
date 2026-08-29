class student: #class create ki
    def __init__(self,name,age,course): #init----constructor hai---object create hote hi automatically call ho jata hai
        self.name = name 
        self.age = age
        self.course = course

    def display(self): #object ka display method call hota hai
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)

s1=student("Divya",18,"BSc IT")
s2=student("radha",19,"cs")

s1.display()
s2.display()
