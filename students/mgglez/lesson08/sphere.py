# ------------------------------------------------------------------------------ #
# Title: Lesson08 - Circle Class Exercise
# Description: Assignment from Lesson08 - Circle Class Exercise
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-05-2021, Created Sphere Class
# ------------------------------------------------------------------------------ #
import math
from circle import Circle


class Sphere(Circle):
    """
    Class that implements a Sphere behaviour
    """

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius**3

    @property
    def area(self):
        return 4 * math.pi * self.radius**2

    def __str__(self):
        return f"Sphere with radius: {self.radius:.3f}"

    def __repr__(self):
        return f"Sphere({self.radius})"

