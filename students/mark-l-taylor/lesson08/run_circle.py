#!/usr/bin/env python

from circle import Circle

####
# Step 1
####

print('Step 1, create a circle object, print radius')
c = Circle(4)
print(c.radius)

####
# Step 2
####

print('\nStep 2, print the diameter')
print('Diameter: {}'.format(c.diameter))

####
# Step 3
####

print('\nStep 3, update diameter value to 2')
c.diameter = 2
print('Diameter: {}'.format(c.diameter))
print('Radius: {}'.format(c.radius))

####
# Step 4
####

print('\nStep 4, area for circle(2)')
c = Circle(2)
print('Area: {}'.format(c.area))

####
# Step 5
####

print('\nStep 5, alternate constructor for circle, from_diameter')
c = Circle.from_diameter(8)
print('Diameter: {}'.format(c.diameter))
print('Radius: {}'.format(c.radius))

####
# Step 6
####

print('\nStep 6, print the str and repr for the circle object')
c = Circle(4)
print(c)
print(repr(c))

####
# Step 7
####

print('\nStep 7, add circle objects')
c1 = Circle(2)
c2 = Circle(4)
c3 = c1 + c2
print(c3)

c4 = c1 + 5
print(c4)

c5 = 5 + c2
print(c5)

print('\nStep 7b, multiply circle objects')
c6 = c2 *3
print(c6)

####
# Step 8
####


print('\nStep 8, compare circle objects')
c1 = Circle(2)
c2 = Circle(4)
c3 = Circle(4)
print('Is c1 > c2?  {}'.format(c1 > c2))
print('Is c1 < c2?  {}'.format(c1 < c2))
print('Is c1 == c2?  {}'.format(c1 == c2))
print('Is c2 == c3?  {}'.format(c2 == c3))

print('\nStep 8a, sort circle objects')
circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
print(circles)
circles.sort()
print('sorted:')
print(circles)

print('\nStep 8b, subtracting of circles')
c1 = Circle(2)
c2 = Circle(4)
c3 = c2 - c1
print(c3)

c4 = c2 - 1
print(c4)

