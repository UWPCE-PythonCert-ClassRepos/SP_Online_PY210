#!/usr/bin/env python3

"""
The ultimate circle.. and sphere
Circle(object) or Sphere(Circle), __init__(self,radius)
"""

import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, _diameter):
        radius = _diameter/2
        return cls(radius)

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError('You cannot have a negative radius')
        else:
            self._radius = val
    
    @property
    def diameter(self):
        return 2*self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)



    def __str__(self):
        '''For use in print()'''
        return 'This circle has a radius of {} and a diameter of {}'.format(self.radius, self.diameter)

    def __repr__(self):
        '''For use when object itself is represented'''
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)


class Sphere(Circle):
    
    def __str__(self):
        '''For use in print()'''
        return 'This sphere has a radius of {} and a diameter of {}'.format(self.radius, self.diameter)

    def __repr__(self):
        '''For use when object itself is represented'''
        return 'Sphere({})'.format(self.radius)

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)