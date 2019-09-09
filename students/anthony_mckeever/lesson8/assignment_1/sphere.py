"""
Programming In Python - Lesson 8 Assignment 1: Spheres
Code Poet: Anthony McKeever
Start Date: 09/06/2019
End Date: 09/06/2019
"""

import math

from circle import Circle


class Sphere(Circle):
    """
    An object representing a Sphere.
    """

    def __init__(self, radius):
        """
        Initializes a Sphere object

        :self:      The class
        :radius:    The desired radius of the Sphere.
        """
        super().__init__(radius)


    @classmethod
    def from_diameter(self, diameter):
        """
        Instantiates a Sphere from a diameter value.

        :self:      The class
        :diameter:  The desired diameter of the Sphere.
        """
        return super().from_diameter(diameter)

    @property
    def volume(self):
        """
        Return the sphere's volume.
        Formula: 4/3 * pi * r^3
        """
        return (4 / 3) * math.pi * (self.radius ** 3)


    @property
    def area(self):
        """
        Return the sphere's area
        Formula: 4 * pi * r^2
        """
        return 4 * math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Sphere with radius: {self.radius}"


    def __repr__(self):
        return f"Sphere({self.radius})"
