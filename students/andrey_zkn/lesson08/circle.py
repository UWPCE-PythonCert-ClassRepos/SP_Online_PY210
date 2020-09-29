#!/usr/bin/env python3


import math
import pytest


class Circle: 

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, the_diameter):
        self.radius = the_diameter/2    

    @property
    def area(self):
        # Read only attribute
        return math.pi * (self.radius ** 2)
		
    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    def __init__(self, the_radius):
        self.radius = the_radius
			
    def __str__(self):
        return (self.__class__.__name__ + " with radius: {0:.6f}").format(self.radius)

    def __repr__(self):
        return (self.__class__.__name__ + "({})").format(self.radius)

    def __add__(self, other):
        return self.__class__(self.radius + other.radius)

    def __mul__(self, other):
        return self.__class__(self.radius * other)

    def __rmul__(self, other):
        return self.__class__(self.radius * other)

    def __truediv__(self, other):
        return self.__class__(self.radius / other)

    def __rtruediv__(self, other):
        return self.__class__(other / self.radius)

    def __floordiv__(self,other):
        return self.__class__(self.radius // other)

    def __rfloordiv__(self, other):
        return self.__class__(other // self.radius)

    def __eq__(self, other):  # Equals, defined so that comparison based off radius works
        return self.radius == other.radius

    def __lt__(self, other):  # Less than, defined so that sorting based off radius works
        return self.radius < other.radius
		
		



class Sphere(Circle):
    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)