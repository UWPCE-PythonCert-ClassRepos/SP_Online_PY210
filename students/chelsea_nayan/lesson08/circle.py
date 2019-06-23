# Lesson08: Circle Class Exercise
"""
Create a class that represents a simple circle
"""
import math

class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # diameter = radius*2
    @property
    def diameter(self):
        return self._radius * 2

    # User able to set the radius or diameter of a circle
    @radius.setter
    def radius(self, value):
        self._radius = value
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    # Area = pi*radius^2
    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    # Let user create a circle directly with the diameter
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # Print out the radius of the circle in informal and formal string representation
    def __str__(self):
        return f'Circle with a radius of {self.radius}'
    def __repr__(self):
        return f'Circle({self._radius})'

    # Add circles
    def __add__(self, other):
        if isinstance(other, int):
            return Circle(self.radius + other)
        elif isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported.')

    # Substract circles
    def __sub__(self, other):
        if isinstance(other, int):
            result = self.radius - other
            if result <= 0:
                raise ValueError('Circle radius must be a positive value.')
            return Circle(result)
        elif isinstance(other, Circle):
            result = self.radius - other.radius
            if result <= 0:
                raise ValueError('Circle radius must be a positive value.')
            return Circle(result)
        else:
            raise TypeError('Whoops, sorry! Unsupported.')

    # Multiply circles
    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported feature.')

    # Compare circles
    def __lt__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported feature.')
    def __le__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported feature.')
    def __gt__(self, other):
        #return self.radius > other.radius
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported feature.')
    def __eq__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        elif isinstance(other, Circle):
            return Circle(self.radius * other.radius)
        else:
            raise TypeError('Whoops, sorry! Unsupported feature.')

"""
Create a class that represents a simple sphere using the circle class
"""

# Sphere class that subclassing the Circle class
class Sphere(Circle):
    @property
    # Volume = (4/3)*pi*radius^3
    def volume(self):
        return (4/3) * math.pi * ((self.radius) ** 3)

    @property
    # Surface area = 4*pi*radius^2
    def area(self):
        return 4 * math.pi * ((self._radius) ** 2)

    # Print out the radius of the sphere in informal and formal string representation
    def __str__(self):
        return f'Sphere with a radius of {self._radius}'
    def __repr__(self):
        return f'Sphere({self._radius})'
