import random
from array import *
a = random.randrange(0,12)
b = random.randrange(0,12)

d1 = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
d2 = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]

x,y=d1[a],d1[b]
z=x-y
print(a,b,x,y,z)