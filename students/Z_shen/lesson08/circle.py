import math


class Circle:

    def __init__(self, the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, the_diameter):
        self.radius = the_diameter / 2

    @property
    def area(self):
        return (self.radius ** 2) * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return self.__class__.__name__ + ' with radius: {}'.format(self.radius)

    def __repr__(self):
        return self.__class__.__name__ + '({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):

    def __str__(self):
        return 'Sphere with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):

        return 4/3 * math.pi * (self.radius**3)

    @property
    def area(self):

        return 4 * math.pi * (self.radius**2)
