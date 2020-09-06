#!/usr/bin/env python3
import math

"""
Lesson08 assignment; creating a class to represent
a circle.  The class should be capable of the following:
- computing the circles area
- priting the circle "pretty"
- adding two circles together
- sort circles
- compare if circles are equal
"""

class Circle:
    
    def __init__(self, radius):
        self._radius = float(radius)

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
    
    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, dia):
        return cls(dia / 2)
    
    def __repr__(self):
        return f"Circle({self.radius:.3f})"

    def __str__(self):
        return f"Circle with radius: {self.radius:.3f}"
