#!/usr/bin/env python3

'''
A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.
'''

import math

class Circle:

    def __init__(self, radius=1):
        self.radius = radius
        self._diameter = None
        self._area = None
         
    @property 
    def diameter(self):
        self._diameter = self.radius*2
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value/2           

    @property
    def area(self):
        self._area = math.pi * (self.radius**2)
        return self._area    

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
        
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(repr(self.radius))

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, num):
        return Circle(self.radius * num)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius

#sphere subclass
class Sphere(Circle):
    
    @property
    def volume(self):
        self._volume = ((4/3)*math.pi*self.radius**3)
        return self._volume

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(repr(self.radius))

    def __add__(self, other):
        return Sphere(self.radius + other.radius)

    def __mul__(self, num):
        return Sphere(self.radius * num)



    @property
    def surface_area(self):
        self._surface_area = 4 * math.pi * (self.radius**2)
        return self._surface_area 

