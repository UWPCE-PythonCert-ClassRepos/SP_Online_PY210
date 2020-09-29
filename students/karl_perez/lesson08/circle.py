from math import pi

class Circle:
    def __init__(self, val):
        self.radius = val

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @classmethod
    def from_diameter(cls, val):
        return cls(val/2)

    @property
    def area(self):
        return round(self.radius ** 2 * pi, 5)

    def __str__(self):
        return f'Circle with radius: {self.radius:.5f}'

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __le__(self, other):
        return (self.radius <= other.radius)

    def __gt__(self, other):
        return (self.radius > other.radius)

    def __ge__(self, other):
        return (self.radius >= other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)

class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius:.5f}'

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return round(self.radius**3 * 4/3 * pi, 5)

    @property
    def area(self):
        return round(self.radius**2 * 4 * pi, 5)