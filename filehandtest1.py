fp = open("sample.txt","a")

roll = int(input("Enter the roll number:"))
name = input("Enter your name:")
marks = int(input("Enter your marks:"))

st = "\n" + str(roll) + "\t" + name + "\t" + str(marks)

fp.write(st)
print("data transferred")

fp.close()