#!/usr/bin/env python
import math
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def __setitem__(self, radius, value):
        self.radius = value
    @classmethod
    def from_diameter(obj, value):
        radius = value/2
        return obj(radius)
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2
    @property
    def area(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return 'Circle with radius: {:.4f}'.format(self.radius)

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, obj):
        return repr(Circle(self.radius + obj.radius))

    def __mul__(self, obj):
        return repr(Circle(self.radius * obj))

    def __lt__(self, obj):
        return self.radius < obj.radius
    def __le__(self, obj):
        return self.radius <= obj.radius
    def __eq__(self, obj):
        return self.radius == obj.radius
    def __gt__(self, obj):
        return self.radius > obj.radius

class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius: {:.4f}'.format(self.volume)

    def __repr__(self):
        return f'Sphere({self.volume})'

    @property
    def area(self):
        raise NotImplementedError

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

if __name__ == "__main__":
    c1 = Circle(4)
    print(c1.radius)
    print(c1.diameter)
    c1.radius = 2
    print(c1.radius)
    print(c1.diameter)
    c1.diameter = 16
    print(c1.radius)
    print(c1.diameter)
    print(c1)
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    print(c3)
    circles = [Circle(1), Circle(9), Circle(4)]
    circles.sort()
    print(circles)