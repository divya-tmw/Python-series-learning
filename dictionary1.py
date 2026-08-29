#create a dictionary of student details
student = {
    "name":"divya sharma",
    "age":18,
    "city":"mumbai",
    "course":"sy bsc it",
    "marks":90,
}
print(student)

#accessing the value
print(student["name"])

#updating the value
student["marks"]=100
print("after updating marks:",student)

#pop method-----delete the element
student.pop("age")
print(student)

#keys method
print(student.keys())

#values method
print(student.values())

#items method
print(student.items())