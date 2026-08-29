# #dictionary in python
# dx = {"name":"divya","age":18,"city":"mumbai"}
# #printing
# print(type(dx))

# #add new elements in dict
# dx["sal"] = "2500"
# print(dx)

# #delete
# del dx['age']
# print(dx)

# #edit
# dx['sal'] = 3000
# print(dx)


n = int(input("Enter the count of books:"))

book = {} #empty dictionary banai hai

for i in range(n):
    idx = int(input("Enter the book id:"))
    book_name = input("enter the name of the book:")
    cost = float(input("enter the cost of the book:"))
    page = int(input("Enter the number of the pages:"))

    dx = [book_name,cost,page]
    book[idx]=dx

    print("ID \nName \ncost \npage")
    for i in book:
        print(i,book[i])
        print(i,"\t",book[i][0],"\t",book[i][1],"\t",book[i][2])

