import math


class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(Circle, d):
        self = Circle(d / 2)
        return self

