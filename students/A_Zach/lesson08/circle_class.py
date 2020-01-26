"""
Create a class for circles
"""

from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius


    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"


    def __repr__(self):
        return f"Circle({self.radius})"


    @classmethod
    #Can create a circle from diameter instead
    def from_diameter(cls,diameter):
        self = cls(diameter/2)
        return self


    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, value):
        self.radius = value/2


    @property
    def area(self):
        return pi * self.radius**2


    def __add__(self, other):
        sum = self.radius + other.radius
        return Circle(sum)


    def __mul__(self,other):
        prod = self.radius * other
        return Circle(prod)


    def __rmul__(self,val):
        return self.__mul__(val)


    def __eq__(self,other_circle):
        return self.radius == other_circle.radius


    def __lt__(self,other_circle):
        return self.radius < other_circle.radius


    def __gt__(self,other_circle):
        return self.radius > other_circle.radius


class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius:.2f}'


    def __repr__(self):
        return f'Sphere({self.radius})'


    @property
    def volume(self):
        return 4/3 * pi * self.radius**3


    @property
    def area(self):
        return 4 * pi * self.radius**2