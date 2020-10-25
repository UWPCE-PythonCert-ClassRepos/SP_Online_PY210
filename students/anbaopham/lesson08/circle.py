import math
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        #self.diameter = radius * 2.0
    # @property
    # def radius(self):
    #     return self.diameter / 2.0
    # @radius.setter
    # def radius(self, radius):
    #     self.diameter = radius * 2.0

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return math.pi * self.radius ** 2.0

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        self.radius += other.radius
        return Circle(self.radius)
    def __mul__(self, other):
        if type(other) in (int, float):
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * other.radius)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

class Sphere(Circle):
    def volumn(self):
        return 4/3 * math.pi * self.radius ** 3

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)
