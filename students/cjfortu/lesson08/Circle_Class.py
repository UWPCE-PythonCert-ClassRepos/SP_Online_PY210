#!/usr/bin/env python

from math import *


class Circle:
    """Class that allows creation and manipulation of circle data."""
    def __init__(self, values=None):
        """Initiate a circle by radius."""
        self.radius = values
        
    @classmethod
    def from_diameter(cls, value):
        """Initiate a circle by diameter, and change the radius."""
        radius = value / 2
        return cls(radius)
        
    @property
    def diameter(self):
        """Diameter is the formal definition."""
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """Set diameter of an existing circle."""
        self.radius = value / 2
        
    @property
    def area(self):
        """Area is the formal definition."""
        return pi * self.radius**2
        
    def __str__(self):
        """String response is a statement."""
        return 'Circle with radius: {:f}'.format(self.radius)
    
    def __repr__(self):
        """Repr response depicts an object."""
        return 'Circle({})'.format(self.radius)
        
    def __add__(self, other):
        """Circles can be combined based on radii."""
        new_rad = self.radius + other.radius
        return Circle(new_rad)
        
    def __mul__(self, other):
        """A circle can be multiplied with a  number in one direction."""
        new_rad = self.radius * other
        return Circle(new_rad)
        
    def __rmul__(self, other):
        """A circle can be multiplied with a  number in the opposite direction."""
        new_rad = self.radius * other
        return Circle(new_rad)
        
    def __lt__(self, other):
        """Circle radii can be compared less than."""
        return self.radius < other.radius
        
    def __gt__(self, other):
        """Circle radii can be compared greater than."""
        return self.radius > other.radius
        
    def __eq__(self, other):
        """Circle radii can be equal."""
        return self.radius == other.radius
        
    def __ne__(self, other):
        """Circle radii can be not equal."""
        return self.radius != other.radius
        

class Sphere(Circle):
    """Sphere subclass based on Circle class."""
    def __str__(self):
        """Override the string response."""
        return 'Sphere with radius: {:f}'.format(self.radius)
        
    def __repr__(self):
        """Override the repr response."""
        return 'Sphere({})'.format(self.radius)
        
    @property
    def volume(self):
        """Volume is the formal definition."""
        return (4 / 3) * pi * self.radius**3
        
    @property
    def area(self):
        """
        Override the area definition.
        
        Surface area is the formal definition.
        """
        return 4 * pi * self.radius**2