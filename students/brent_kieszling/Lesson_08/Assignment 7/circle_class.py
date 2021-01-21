#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: circle_class, PYTHON210 - Assignment 7
#Desc: Class that represents varried circles
#Change Log: (Who, When, What)
#Brent Kieszling, 2021-Jan-20, created file
#-------------------------------------------#
import math


class Circle(object):

    def __init__(self, r):
        if r < 0:
            raise AttributeError("Radius must be a number greaterthan or equal to 0")
        self._radius = r

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/ 2)
        return self

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
    
    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return math.pi * self._radius**2

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self._radius)

    def __repr__(self):
        return "'Circle({:.0f})'".format(self.radius)

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __sub__(self, other):
        a = self._radius - other.radius
        if a < 0:
            raise AttributeError("Can't have a negative radius")
        else:
            return Circle(a)

    def __mul__(self, val):
        return Circle(self._radius * val)

    #This with __mul__  makes it so the Circle object can be on either side of *
    def __rmul__(self, val):
        return Circle(self._radius * val)

    def __truediv__(self, val):
        return Circle(self._radius / val)

    def __rtruediv__(self, val):
        return Circle(val / self._radius)

    def __eq__(self, other):
        if self._radius == other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._radius < other.radius:
            return True
        else:
            return False


class Sphere(Circle):

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self._radius)

    def __repr__(self):
        return "'Sphere({:.0f})'".format(self.radius)

    @property
    def volume(self):
        return (math.pi * (4/3) * (self._radius)**3)

    @property
    def area(self):
        return (math.pi * 4 * (self._radius)**2)




