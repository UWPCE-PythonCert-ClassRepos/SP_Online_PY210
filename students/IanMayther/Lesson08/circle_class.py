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

    def __str__(self):
       return f'{self.__class__.__name__} with radius: {self.radius:.4f}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    def __add__(self, other_circle):
        total = self.radius + other_circle.radius
        return Circle(total)

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __mul__(self, other_circle):
        if isinstance(other_circle, int):
            prod = self.radius * other_circle
        else:
            prod = self.radius * other_circle.radius
        return Circle(prod)

    def __rmul__(self, value):
        return self.__mul__(value)

    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

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
        cls.radius = dia / 2
        return cls

    @property
    def area(self):
        'Calculates area of circle'
        return round(math.pi * self.radius ** 2, 5)

class Sphere(Circle):
    """
    A class-based system for rendering a sphere.
    """

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    @property
    def area(self):
        return 4 * math.pi * self.radius ** 2