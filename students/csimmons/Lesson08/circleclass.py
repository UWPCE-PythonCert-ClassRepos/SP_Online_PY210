#!/usr/bin/env python3
# Craig Simmons
# Python 210
# Lesson07 Asignment Created 01/09/2021 - csimmons
# Edited 01/13/2021 - v1.0 - csimmons

from math import pi

class Circle(object):
   
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, d):
        return cls(d/2)

    def __add__(self, c2):
        return self.__class__(self.radius + c2.radius)

    def __mul__(self, value):
        return self.__class__(self.radius * value)

    def __rmul__(self, value):   
        return self.__mul__(value)

    def __eq__(self, c2):   
        return self.radius == c2.radius

    def __lt__(self, c2):   
        return self.radius < c2.radius

    def __gt__(self, c2):   
        return self.radius > c2.radius

    def __le__(self, c2):   
        return self.radius <= c2.radius

    def __ge__(self, c2):   
        return self.radius >= c2.radius

class Sphere(Circle):

    def __str__(self):
        return f'Sphere with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    @property
    def area(self):
        return 4 * pi * self.radius ** 2
    

    