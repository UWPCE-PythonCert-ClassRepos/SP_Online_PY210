#!/usr/bin/env python3
"""
A Class to create a circle
"""
import math

class Circle():

    def __init__(self, radius):
        self.radius = radius


    @property
    def diameter(self):
       return self.radius * 2


    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


    @property
    def area(self):
        return math.pi * (self.radius ** 2)


    @classmethod
    def from_diameter(cls,diameter):
        '''
        Call as c = Cirle.from_diameter(diameter)
        '''
        self =cls(diameter / 2)
        return self


    def __str__(self):
        return "Circle with radius: " + str(self.radius)


    def __repr__(self):
        return f"'{self.__class__.__name__}({self.radius})'"


    def __add__(self,other):
        try:
            new_radius = self.radius + other.radius
        except(AttributeError):
            new_radius = self.radius + other
        return Circle(new_radius)


    def __radd__(self,other):
        new_radius = self.radius + other
        return Circle(new_radius)


    def __mul__(self, other):
        try:
            new_radius = self.radius * other.radius
        except(AttributeError):
            new_radius = self.radius * other
        return Circle(new_radius)


    def __rmul__(self, other):
        new_radius = self.radius * other
        return Circle(new_radius)


    def __eg__(self, other):
        return self.radius == other.radius


    def __lt__(self, other):
        return self.radius < other.radius

class Sphere(Circle):

    def __str__(self):
        return "Sphere with radius: " + str(self.radius)


    @property
    def volume(self):
        return 4 / 3 * math.pi * self.radius ** 3


    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)






















