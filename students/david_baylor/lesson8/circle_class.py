#!/usr/bin/env python3

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return (self.radius == other.radius)

    def __lt__(self, other):
        return (self.radius < other.radius)
    
    def __le__(self, other):
        return (self.radius <= other.radius)

    def __ge__(self, other):
        return (self.radius >= other.radius)

    def __gt__(self, other):
        return (self.radius > other.radius)

    def __ne__(self, other):
        return (self.radius != other.radius)


    def __add__(self, other):
        try:
            return f"Circle({(self.radius + other.radius)})"
        except AttributeError:
            return f"Circle({(self.radius + int(other))})"
            

    def __sub__(self, other):
        try:
            return f"Circle({(self.radius - other.radius)})"
        except AttributeError:
            return f"Circle({(self.radius - int(other))})"

    def __mul__(self, other):
        try:
            return f"Circle({(self.radius * other.radius)})"
        except AttributeError:
            return f"Circle({(self.radius * int(other))})"

    def __truediv__(self, other):
        try:
            return f"Circle({(self.radius / other.radius)})"
        except AttributeError:
            return f"Circle({(self.radius / int(other))})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return math.pi*(self.radius**2)
    
    @classmethod
    def from_diameter(cls, val):
        return cls(val/2)

class Sphere(Circle):
    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volum(self):
        return (4/3)*math.pi*(self.radius**3)

    @property
    def area(self):
        return 4*math.pi*(self.radius**2)
