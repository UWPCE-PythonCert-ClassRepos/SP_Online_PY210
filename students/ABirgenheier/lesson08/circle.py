import math


import numpy as np


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return self.radius * 2

    def area(self):
        return round((self.radius**2) * (math.pi), 2)

    def perimiter(self):
        return round((self.radius * 2) * (math.pi), 2)

    def circumference(self):
        return round(((self.radius * 2) * math.pi), 2)

    def __add__(self, other):
        return round(self.area() + other.area(), 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __str__(self):
        return "Circle with a radius of {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __mul__(self, other):
        return self.radius * other.radius

    @classmethod
    def from_diameter(cls, diameter):
        cls.diameter = diameter
        radius = diameter / 2
        return cls(diameter)

    @staticmethod
    def sort(array):
        return np.sort(array)


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return round((self.radius ** 2 * math.pi * 4), 2)

    def volume(self):
        return round(((4/3) * math.pi * self.radius**3), 2)

    def surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 2)

    def __str__(self):
        return "Sphere with a radius of ({})".format(self.radius)

    def __repr__(self):
        return "Sphere ({})".format(self.radius)


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return round((math.pi * (self.radius ** 2) * self.height), 2)

    def area(self):
        return round((2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2), 2)

    def perimiter(self):
        return round(2 * math.pi * self.radius, 2)
