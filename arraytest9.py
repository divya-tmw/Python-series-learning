#insert an element

arr = [10,20,30,40,50]

num=int(input("enter element:"))
pos=int(input("enter position:"))

arr.insert(pos,num)
print("array after insertion:",arr)