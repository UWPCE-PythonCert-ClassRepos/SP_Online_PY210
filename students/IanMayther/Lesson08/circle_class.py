#!/usr/bin/env python3


import math

class Circle:
    """
    A class-based system for rendering a circle.
    """

    def __init__(self, rad=None):
        if rad is None:
            raise AttributeError
        else:
            self.radius = rad

    @property
    def diameter(self):
        'Calculate diameter of circle'
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @classmethod
    def from_diameter(cls, dia):
        cls.diameter = dia
        return cls.diameter

    @property
    def area(self):
        'Calculates area of circle'
        return round(math.pi * self.radius ** 2, 5)