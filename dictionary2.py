#create a dictionary of student details input from user
student = {}
student["name"] = input("Enter the name:")
student["age"] = int(input("Enter the age:"))
student["city"] = input("Enter the city:")
student["course"] = input("Enter the course:")
student["roll_no"] = int(input("Enter the roll no:"))

print(student)

#access element
print("\nname:",student["name"])

#update element
student["course"]=input("Enter updated course:")
print("after updating course:",student)

#pop method
removed = student.pop("roll_no")
print("removed roll no:",removed)
print("after pop:",student)

#keys method
print("keys:",student.keys())

#value method
print("values:",student.values())

#items method
print("items:",student.items())
