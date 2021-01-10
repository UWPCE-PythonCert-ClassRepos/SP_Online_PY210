import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) * math.pi

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def __str__(self):
        return "Circle with a radius of {0:.2f}".format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return self.__class__(self.radius + other.radius)

    def __mul__(self, other):
        return self.__class__(self.radius * other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

class Sphere(Circle):
    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def __str__(self):
        return "Sphere with a radius of {0:.2f}".format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)