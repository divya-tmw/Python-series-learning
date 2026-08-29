#call by referance

def change(dx):
    print("list in function:",dx) #
    dx[0]=100
    dx[1]=200

dx=[10,20,30,60,40] #list banaya
print("The list is:",dx) #list ko print karwaya

change(dx)

print("modified list:",dx)