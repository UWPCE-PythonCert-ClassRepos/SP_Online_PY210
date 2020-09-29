# circle.py
# opcode6502: SP_Online_PY210


import math


class Circle():

    def __init__(self, radius):
        self._area = None
        self._diameter = None
        self.radius = radius

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        raise AttributeError

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def sort_key(self):
        return self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle: Radius: {}'.format(self.radius)


class Sphere(Circle):

    @property
    def area(self):
        return (4 * math.pi * self.radius ** 2)

    @property
    def volume(self):
        return (4 / 3 * math.pi * self.radius ** 3)

    def __add__(self, other):
        return Sphere(self.radius + other.radius)

    def __mul__(self, other):
        return Sphere(self.radius * other)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    def __str__(self):
        return 'Sphere: Radius: {}'.format(self.radius)
