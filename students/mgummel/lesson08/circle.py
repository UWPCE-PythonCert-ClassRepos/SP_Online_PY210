#! /usr/bin/env python3
from math import pi
from functools import total_ordering

@total_ordering
class Circle(object):
    radius = None
    
    def __init__(self, radius):
        self.radius = radius

    
    def __str__(self):
        return f"Circle with radius: {self.radius:.5f}"


    def __repr__(self):
        return f"Circle({self.radius})"


    def __add__(self, other):  
        return Circle(self.radius + other.radius)

    
    def __mul__(self, scalar):
        return Circle(self.radius * scalar)


    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    def __lt__(self, other):
        return (self.radius < other.radius)

    
    def __eq__(self, other):
        return (self.radius == other.radius)


    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, new_value):
        self.radius = new_value / 2
        return new_value

    
    @property
    def area(self):
        return (self.radius ** 2) * pi 

    
    @classmethod
    def from_diameter(cls, diameter):
        if diameter % 2 == 0:
            return cls(int(diameter / 2))
        else:
            return cls(diameter / 2)


class Sphere(Circle):
    def __str__(self):
        return f"Sphere with radius: {self.radius:.5f}"


    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return (4 / 3) * pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * pi * self.radius ** 2