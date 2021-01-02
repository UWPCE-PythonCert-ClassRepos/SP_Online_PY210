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