import math

from functools import total_ordering


@total_ordering
class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius**2


    def __str__(self):
        return f"A circle with radius: {self.radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, val):
        return Circle(self.radius*val)

    def __rmul__(self, val):
        return Circle(self.radius*val)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __iadd__(self, other):
        return Circle(self.radius + other.radius)

    def __isub__(self, val):
        return Circle(self.radius*val)


class Sphere(Circle):

    def __str__(self):
        return f"A sphere with radius: {self.radius}"

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3

    @property
    def area(self):
        return 4 * math.pi * self.radius**2