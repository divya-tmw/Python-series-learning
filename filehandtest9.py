name = input("Enter your name:")
age = input("Enter your age:")

file = open("student.txt","w")

file.write("Name: " + name + "\n")
file.write("Age: " + age)

file.close()

print("Student details saved successfully")