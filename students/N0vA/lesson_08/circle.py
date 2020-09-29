#!/usr/bin/env python3

import math
pi = math.pi


class Circle(object):
    """a simple circle with properties likes radius, diameter, area, etc."""

    def __init__(self, radius):

        self._radius = radius


    def __repr__(self):
        
        return f'Circle({self._radius})'


    def __str__(self):
        
        return f'Circle with a radius of {self.radius}'    
     

    @property
    def radius(self):

        return self._radius

    @property
    def diameter(self):

        return self._radius * 2

    @property
    def area(self):
        
        return self._radius ** 2 * pi
    
        
    # Let user set diameter
    @diameter.setter
    def diameter(self, value):

        self._radius = value / 2
        return f'Circle set to a diameter of {value} with a radius of {self.radius}.'

    
    @classmethod
    def from_diameter(cls, diameter):
        
        return cls(diameter / 2)


    def __add__(self, val): # Add two circles

        if isinstance(val, Circle):
            # Add two circles
            return Circle(self.radius + val.radius)
        elif isinstance(val, int):
            # Add to a radius
            return Circle(self.radius + val)
        

    def __sub__(self, val): # Add two circles

        if isinstance(val, Circle):
            # Add two circles
            return Circle(self.radius - val.radius)
        elif isinstance(val, int):
            # Add to a radius
            return Circle(self.radius - val)


    def __mul__(self, val): # Add two circles

        if isinstance(val, Circle):
            # Add two circles
            return Circle(self.radius * val.radius)
        elif isinstance(val, int):
            # Add to a radius
            return Circle(self.radius * val)


    def __lt__(self, other): # Compare circles to define less than operator

        if self.radius < other.radius:
            return True
        else:
            return False


    def __le__(self, other): # Les than or equal to

        if self.radius <= other.radius:
            return True
        else:
            return False


    def __eq__(self, other): # Two circles that are equal

        if self.radius == other.radius:
            return True
        else:
            return False


    def __ne__(self, other): # Circles have different radius

        if self.radius != other.radius:
            return True
        else:
            return False


    def __gt__(self, other): # One radius is greater than another

        if self.radius > other.radius:
            return True
        else:
            return False


    def __ge__(self, other): # Greater than or equal to

        if self.radius >= other.radius:
            return True
        else:
            return False


class Sphere(Circle):
    
    def __repr__(self): # Print sphere
        
        return f'Sphere({self.radius})'

    
    def __str__(self): # Sphere string
        
        return f'Sphere with radius of {self.radius}'

    
    @property
    def volume(self): # Volume 
        
        self._volume = (4/3) * pi * (self.radius ** 3)
        return self._volume


    @property
    def area(self): 
        raise NotImplementedError

    