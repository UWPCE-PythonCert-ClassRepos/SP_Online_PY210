#!/usr/bin/env python3
import math

class Circle(object):
#step1
    def __init__(self,radius_value):
        self.radius = radius_value
#step6
    def __str__(self):
        return(self.__class__.__name__ + ' with radius: {}'.format(self.radius))

    def __repr__(self):
        return (self.__class__.__name__ + '({})'.format(self.radius))

#step7
    def __add__(self, other):
        return self.__class__(self.radius + other.radius)

    def __mul__(self, other):
        return self.__class__(self.radius * other)
#step8
    #def __eq__(self, other):
    #    return self.radius==other.radius
    def __eq__(self, other):
        return self.__class__(self.radius==other)

    def __le__(self, other):
        return self.__class__(self.radius<=other.radius)

    def __ge__(self, other):
        return self.__class__(self.radius>=other.radius)

    def __gt__(self, other):
        return self.__class__(self.radius > other.radius)

    def __lt__(self, other):
        return self.__class__(self.radius < other.radius)

    def __rmul__(self, other):
        return self.__class__(self.radius * other)

    def __floordiv__(self, other):
        return self.__class__(self.radius // other)

    def __ne__(self, other):
        return self.__class__(self.radius != other.radius)

#step2
    @property
    def diameter(self):
        return 2*self.radius
#step3
    @diameter.setter
    def diameter(self,value):
        self.radius = value/2
#step4
    @property
    def area(self):
        return math.pi * (self.radius**2)
#step5
    @classmethod
    def from_diameter(cls,value):
        return cls(value/2)

#step9
class Sphere(Circle):

    @property
    def volume(self):
        return math.pi * (4 / 3) * (self.radius ** 3)

    @property
    def area(self):
        return ((self.radius ** 2) * (4 * math.pi))
