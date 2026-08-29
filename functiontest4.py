#call by value

def change(n):
   print("The value in function is:",n)
   n=100

   n=int(input("Enter the number:"))
   print("The number is",n)

   change(n)
   print("New value is:",n)



