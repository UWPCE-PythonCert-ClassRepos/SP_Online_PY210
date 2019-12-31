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
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)

        
