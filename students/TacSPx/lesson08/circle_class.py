#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: circle class
# Description: Create a class that represents a simple circle.  The circle is
#              defined by a radius or diameter.  You can query the radius/ diameter,
#              area, print details, add two circles, compare size, compare equal, and
#              list/ sort them. Create a Subclass for sphere.
#
# <07/25/2020>, Created Script
#
# ---------------------------------------------------------------------------- #
# imports
import sys
import math


# Step 1
class Circle(object):
    def __init__(self, rad):
        self._rad = rad

    @property
    def rad(self):
        return self._rad

    @rad.setter  # radius can't be zero or less
    def rad(self, val):
        if val <= 0:  # error handling
            raise ValueError("Radius can't be zero or a negative number")
        self._rad = val

    # Step 3
    @property  # diameter is 2 x radius
    def dia(self):
        return 2 * self.rad

    @dia.setter  # diameter is 1/2 the radius
    def dia(self, dia):
        self.rad = dia / 2

    # Step 4
    @property  # area is pi x r2
    def area(self):
        return math.pi * self.rad ** 2

    @area.setter
    def area(self, area):
        raise AttributeError("Circle can't be directly created with area")

    # Step 5
    @classmethod
    def from_diameter(cls, val=0):
        """Creates circle with 'alternate constructor' using diameter.
        Class methods take a 'cls' parameter that points to the class and
        not the object instance"""
        self = cls(rad=0)
        self._rad = 0.5 * val
        self._dia = val
        return self

    # Step 6
    def __str__(self):
        """ Prints a nice description of the circle with the radius and area"""
        return "Circle with the radius: {} and area: {}.".format(self.rad, self.area)

    # def __repr__(self): #This didn't work out, when you add together in the testing!
    #     """ Prints an 'ok' representation of the circle with the radius and area"""
    #     return "Circle({})({})".format(self.rad, self.area)

    def __repr__(self):
        """ Prints an 'ok' representation of the circle with only the radius"""
        return "Circle({})".format(self.rad)

    # Step 7
    def __add__(self, other):
        """ add circles radii together"""
        add_circles = self.rad + other.rad
        return Circle(add_circles)

    # def __mul__(self, other): #multiply two circles *Not used I initially read the instructions wrong*
    #     multiply_circles = self.rad * other.rad
    #     return Circle(multiply_circles)

    def __mul__(self, other):
        """ Multiply circle, left operand"""
        multiply_circle = self.rad * 3
        return Circle(multiply_circle)

    def __rmul__(self, other):
        """ Multiply circle, right operand"""
        multiply_circle = self.rad * 3
        return Circle(multiply_circle)

    # Step 8 Compare
    def __lt__(self, other):
        """ Compare, <"""
        return self.rad < other.rad

    def __gt__(self, other):
        """ Compare, >"""
        return self.rad < other.rad

    def __ne__(self, other):
        """ Compare, !="""
        return self.rad < other.rad

    def __eq__(self, other):
        """ Compare, =="""
        return self.rad == other.rad

    # extra
    def __ge__(self, other):
        """ Compare, >="""
        return self.rad >= other.rad

    def __le__(self, other):
        """ Compare, <="""
        return self.rad <= other.rad


# Step 9 Subclassing with Sphere; volume and surface area


class Sphere(Circle):

    @property
    def volume(self):
        """volume of a sphere = 4/3 * pi * r3"""
        return 4 / 3 * math.pi * self.rad ** 3

    @property
    def area(self):
        """ surface area of a sphere =  4 * pi * r2"""
        return 4 * math.pi * self.rad ** 2

    def __str__(self):
        return "Sphere with the radius {}, volume {}, and surface area {}.".format(self.rad, self.volume, self.area)

    def __repr__(self):
        """ Prints an 'ok' representation of the Sphere with only the radius"""
        return "Sphere({})".format(self.rad)
