try:
    students = {
        101:"Divya",
        102:"krishna",
        103 : "radha"
     }

    roll_no = int(input("Enter the roll no:"))
    print("Student Name:",students[roll_no])

except KeyError:
    print("invalid roll no entered")
