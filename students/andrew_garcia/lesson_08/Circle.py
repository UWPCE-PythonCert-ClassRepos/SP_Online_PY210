'''
Andrew Garcia
Circle
8/19/19
'''

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2), 3)

    @classmethod
    def from_diameter(cls, diameter):
        cls.radius = diameter/2

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, circle):
        return Circle(self.radius + circle.radius)

    def __mul__(self, number):
        return Circle(self.radius * number)

    def __lt__(self, circle):
        return self.radius < circle.radius

    def __gt__(self, circle):
        return self.radius > circle.radius

    def __eq__(self,circle):
        return self.radius == circle.radius


class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def area(self):
        raise NotImplementedError
    
    @property
    def volume(self):
        return round(4/3 * math.pi * (self.radius**3), 3)