#Mark McDuffie
#6/9/20
#circle & sphere classes

import math

class Circle:

    def __init__(self, the_radius):
        self.radius = the_radius

    def __str__(self):
        return ('Circle with radius: {0:.6f}').format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return self.__class__(self.radius + other.radius)

    def __mul__(self, other):
        return self.__class__(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, x):
        self.radius = x / 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2)
        return self

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2), 6)

class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius {0:.6f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)