
import math


class Circle(object):

    #step 1
    def __init__(self, radius):
        self.radius = radius

    #step 2
    @property
    def diameter(self):
        return self.radius * 2

    #step 3
    @diameter.setter
    def diameter(self, diameter):
            self.radius = diameter / 2

    #step 4
    @property
    def area(self):
        return math.pi * self.radius ** 2

    #step 5
    @classmethod
    def from_diameter(cls, diameter):
        self = cls((diameter/2))
        return self

    #step 6
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    #step 7
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
            return Circle(self.radius * other)

    #step 8
    def  __gt__(self, other):
        return (self.radius > other.radius)

    def  __lt__(self, other):
        return (self.radius < other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)

#step 9
class Sphere(Circle):

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    def volume(self):
        return  (4/3) * math.pi * self.radius ** 3

    #Surface Area of a Sphere = 4 pi r 2
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
