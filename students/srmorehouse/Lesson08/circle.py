#!/usr/bin/env python3

import math

####################################################
# Lesson 08
# Steve Morehouse
####################################################

class Circle (object):

    def __init__ (self, radius):
        if radius <=0:
            raise ValueError ('radius needs to be positive')
        else:
            self.radius = float (radius)


    @property
    def diameter (self):
        return self.radius * 2


    @property
    def area (self):
        return (self.radius**2) * math.pi


    @diameter.setter
    def diameter (self, diameter):
        self.radius = diameter / 2


    @classmethod
    def using_diameter (cir, diameter):
        return cir (diameter / 2)


    def __str__ (self):
        return f'Circle with radius: {self.radius}'


    def __repr__ (self):
        return f'Circle({self.radius})'


    def __add__(self, other):
        if type (other) is int:
            return Circle(self.radius + other)
        else:
            return Circle(self.radius + other.radius)


    def __iadd__(self, other):
        return self.__add__(other)


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if type (other) is int:
            return Circle(self.radius - other)
        else:
            return Circle(self.radius - other.radius)


    def __isub__(self, other):
        return self.__sub__(other)


    def __rsub__(self, other):
        if type (other) is int:
            return Circle(other - self.radius)
        else:
            return Circle(other.radius - self.radius)


    def __mul__(self, other):
        if type (other) is int:
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * other.radius)


    def __imul__(self, other):
        return self.__mul__(other)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __lt__(self, other):
        return True if self.radius < other.radius else False


    def __gt__(self, other):
        return True if self.radius > other.radius else False


    def __eq__(self, other):
        return True if self.radius == other.radius else False


    def sort_key(self):
        return self.radius       

