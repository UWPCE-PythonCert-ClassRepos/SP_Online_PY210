#!/usr/bin/env python3

import math
#Step 1:Create class called Circle:
class Circle:
    def __init__(self, r):
        self.radius = r


    #Step 2:Add a “diameter” property, so the user can get the diameter of the circle:
    @property
    def diameter(self):
        return self.radius * 2
    #Step 3: Set up the diameter property so that the user can set the diameter of the circle:
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    #Step 4:Add an area property so the user can get the area of the circle:    
    @property
    def area(self):
        return math.pow(self.radius, 2)*math.pi

    #Step 5:Add an “alternate constructor” that lets the user create a Circle directly with the diameter:
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)

    #Step 6:Every class should have a nice way to print it out… Add __str__ and __repr__ methods to your Circle class:
    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({:.0f})".format(self.radius)

    #Step 7:Add some of the numeric protocol to your Circle ,You should be able to add two circles:
    def __add__(self, c2):
        return Circle(self.radius + c2.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    #Step 8:Add the ability to compare two circles:

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __gt__(self, other):
        return (self.radius > other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)

    #Sort Circle List
    def sort(self, circles):
        return sorted(circles, key = self.radius)



class Sphere(Circle):
    #   Simple sphere class that subclasses from circle.

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({:.0f})".format(self.radius)

    @property
    def area(self):
        return 4*math.pi*math.pow(self.radius, 2)

    @property
    def volume(self):
        return 4/3*math.pi*math.pow(self.radius, 3)

