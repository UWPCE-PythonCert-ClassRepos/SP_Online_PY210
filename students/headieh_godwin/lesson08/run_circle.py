#!/usr/bin/env python3

from circle import Circle, Sphere
import math

c = Circle(4)
########
# Step 1
########
print(c.radius)

########
# Step 2
########
print(c.diameter)

########
# Step 3
########
c.diameter = 2
print(c.diameter)
print(c.radius)

########
# Step 4
########
c = Circle(2)
print(c.area)

########
# Step 5
########
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)

########
# Step 6
########

c = Circle(4)
print(c)
print(repr(c))
d = eval(repr(c))
print(d)

########
# Step 7
########

c1 = Circle(2)
c2 = Circle(4)
c = c1 + c2
print(c)
c3 = c2 * 3
print(c3)

########
# Step 8
########

c1 = Circle(2)
c2 = Circle(4)
print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
c3 = Circle(4)
print(c2 == c3)
print(c1 * 3)
print(3 * c1)

########
# Step 9
########

s1 = Sphere(2)
s2 = Sphere(4)
s = s1 + s2
print(s)

#r=2
print((2 ** 2) * (4 * math.pi))#sa
print(math.pi * (4 / 3) * (2 ** 3))#v

#r=4
print((4 ** 2) * (4 * math.pi))#sa
print(math.pi * (4 / 3) * (4 ** 3))#v
