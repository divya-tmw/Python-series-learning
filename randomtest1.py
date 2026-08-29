import random
from random import sample

dx=[23,45,67,89,88,99,34,11,22,123,56,887]
print(random.choice(dx))

ans=random.random()
print("random between 0 and 1:",ans)

ans=random.randint(20,50)
print("random between 20 and 50:",ans)

dx=[6,5,3,8,22,90,21,11,60,234,111,77]
print("5 random of the list",sample(dx,5))

dx=[2,44,66,8,90,11,12,23,55,8,4]
random.shuffle(dx)
print("after shuffle",dx)