"""
Christine Kim
Lesson 8
Assignment Spheres
"""
import math
from circle import Circle

class Sphere(Circle):
    
    def __init__(self, radius):
        super().__init__(radius)

    def __str__(self):
        return "Sphere with radius: {}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(self, diameter):
        return super().from_diameter(diameter)