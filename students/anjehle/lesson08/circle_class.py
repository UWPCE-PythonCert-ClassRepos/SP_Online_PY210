from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def dia(self):
        return 2 * self.radius

    @dia.setter
    def dia(self, value):
        self.radius = value/2

    @property
    def area(self):
        return pi*self.radius**2

    @classmethod
    def from_dia(cls, dia):
        return cls(dia/2)

    def __add__(self, c2):
        return self.__class__(self.radius + c2.radius)

    def __mul__(self, val):
        return self.__class__(self.radius * val)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __eq__(self, c2):
        return self.radius == c2.radius

    def __lt__(self, c2):
        return self.radius < c2.radius

    def __gt__(self, c2):
        return self.radius > c2.radius


class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius:.2f}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        return 4 / 3 * pi * self.radius**3

    @property
    def area(self):
        return 4*pi*self.radius**2
