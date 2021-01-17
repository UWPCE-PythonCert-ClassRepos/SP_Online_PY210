
from functools import total_ordering

import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        total_radius = self.radius + other.radius
        return Circle(total_radius)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __mul__(self, other):
        return self.__rmul__(other)

    @total_ordering
    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __le__(self, other):
        return self.radius <= other.radius


    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def get_diameter(self):
        self._diameter = self.radius * 2
        return self._diameter

    def set_diameter(self, diameter):
        self._diameter = diameter
        self.radius = diameter / 2

    diameter = property(get_diameter, set_diameter)

    def get_area(self):
        self._area = math.pi * self.radius ** 2
        return self._area

    def set_area(self, value):
        raise AttributeError("Cannot set the area of the circle")

    area = property(get_area, set_area)

class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    def get_volume(self):
        self._volume = (4/3) * math.pi * self.radius ** 3
        return self._volume

    def set_volume(self, value):
        raise AttributeError("Cannot set the volume of the sphere")

    volume = property(get_volume, set_volume)

    def get_area(self):
        self._area = 4 * math.pi * self.radius ** 2
        return self._area

    def set_area(self, value):
        raise AttributeError("Cannot set the area of the sphere")

    area = property(get_area, set_area)


c1 = Circle(4)
c2 = Circle(5)
c3 = Circle(6)

circle_list = [c3, c1, c2]

print(circle_list.sort())
