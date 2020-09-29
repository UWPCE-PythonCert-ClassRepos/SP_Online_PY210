#!/usr/bin/env python3

import math
import functools

""" A circle class that can be queried for its:
    radius
    diameter
    area
    
    You can also print the circle, add 2 circles together, compare the size of 2 circles (which is bigger
    or are they equal), and list and sort circles.
    """

@functools.total_ordering
class Circle:
    radius = 0
    
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def diameter(self):
        _diameter = self.radius * 2
        return _diameter
    
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = round((self._diameter / 2), 2)
    
    @property
    def area(self):
        _area = (math.pi * (math.pow(self.radius, 2)))
        return round(_area, 2)
    
    @classmethod
    def from_diameter(cls, diam_value):
        cls.diameter = diam_value
        cls.radius = round((cls.diameter / 2), 2)
        return cls
    
    def __str__(self):
        return f"Circle with radius: {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        """
        add two circle objects together
        """
        new_radius = self.radius + other.radius
        return Circle(new_radius)
    
    def __mul__(self, other):
        """
        multiply a circle object by a number
        """
        return Circle(self.radius * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def sort_key(self):
        return self.radius

class Sphere(Circle):
    def __str__(self):
        return f"Sphere with radius: {self.radius}"
    
    def __repr__(self):
        return f"Sphere({self.radius})"
    
    @property
    def volume(self):
        _volume = ((4/3) * math.pi * (math.pow(self.radius, 3)))
        return round(_volume, 2)
    
    @property
    def area(self):
        """
        Calculate the surface area of a sphere
        """
        _area = (4 * math.pi * (math.pow(self.radius, 2)))
        return round(_area, 2)