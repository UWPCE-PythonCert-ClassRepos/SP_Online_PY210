#!/usr/bin/env python3
#-----------------------------------------------------------
# Lesson 8 - Assignment 7: The Circle Class
#            A class that represents a simple circle.
#-----------------------------------------------------------

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):           #getter
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius **2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
       return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        #Augmented addition assignment.
        return self.__add__(other)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Circle(self.radius / other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
       return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.radius **3

    @property
    #surface area
    def area(self):
        return 4 * math.pi * self.radius **2

    #A sphere does not have a circumference, but a great circle of the
    #sphere (where the plane contains the sphere's center) has a circumference
    #of 2*pi*R (R is the radius of a sphere), so I just let the Sphere class
    #have the same circumference property as well and commented out the codes below.
    """
    @property
    def circumference(self):
        raise(NotImplementedError)
    """
