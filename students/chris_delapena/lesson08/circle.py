# Chris Dela Pena
# Circle Assignment

import math

class Circle:
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
        return self.radius * self.radius * math.pi

    #Raise error when setting test_area
    def area(self, value):
        raise AttributeError

    @classmethod
    #alternate constructor - circle from diameter
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mult__(self, other):
        return Circle(self.radius * other.radius)

    def __greater_than__(self, other):
        return (self.radius > other.radius)

    def __less_than__(self, other):
        return self.radius < other._radius

    def __equals__(self, other):
        return self.radius == other.radius

    def sort_key(self):
        return self.radius

class Sphere(Circle):
    @property
    def area(self):
        return 4 * math.pi * self.radius * self.radius

    def volume(self):
        return (4/3) * math.pi * self.radius * self.radius * self.radius

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)
