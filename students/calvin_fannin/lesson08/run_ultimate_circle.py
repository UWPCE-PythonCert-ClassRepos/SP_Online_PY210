#!/usr/bin/env python3
import ultimate_circle as uc

#set first pass
print("------------------------first pass")
c = uc.Circle(7)

print(c.radius)
print(c.diameter)

#set diameter
print("------------------------set diameter")
c = uc.Circle(7)
c.diameter =20
print(c.radius)
print(c.diameter)

c = uc.Circle(7)
print(c.area)

print("------------------------from diameter")
c = uc.Circle.from_diameter(30)
print(c.area)
print(c.diameter)
print(c.radius)

#step 6
print("------------------------step six")
c = uc.Circle(7)
print(repr(c))
print(c)
d = eval(repr(c))
print(d)


#do some adding
print("------------------------step 7")
c = uc.Circle(7)
c2 = uc.Circle(7)
csum = c + c2
print(c)
print(c2)

print(csum)
print(repr(csum))

print(3 + csum)
print(csum * 3)
print(3 * csum)











