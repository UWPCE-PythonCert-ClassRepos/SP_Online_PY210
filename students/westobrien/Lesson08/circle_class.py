import math

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius * self.radius * math.pi

    @area.setter
    def property(self, area):
        return attributeError

    @classmethod
    def from_diameter(cls, value):
        self = cls(value / 2)
        return self

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return (4 / 3) * math.pi * pow(self.radius, 2)

    @property
    def area(self):
        return 4 * math.pi * pow(self.radius, 2)

