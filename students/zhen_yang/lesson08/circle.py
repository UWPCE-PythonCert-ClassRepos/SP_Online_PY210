# circle.py
from math import pi
from functools import total_ordering

# Step 1
@total_ordering
class Circle(object):
    def __init__(self, radius=1):
        self._radius = radius

    # @property' + '@setter', for get and set an attribute. (print obj.x
    # or obj.x = 5). Only @property makes the attribute read only.
    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2.0

    @property
    def area(self):
        #print(f"res:{pi*(self._radius **2)}")
        return pi * (self._radius ** 2)

    @classmethod
    def from_diameter(classobj, diameter=1):
        return classobj(diameter / 2.0)

    def __str__(self):
        return 'Circle with radius: {}'.format(self._radius)

    def __repr__(self):
        return 'Circle({})'.format(self._radius)

    def __iadd__(self, other):# for circle_1 += circle_2
        self._radius += other.radius
        return self

    def __imul__(self, other):# circle *= 2
        self._radius *= other
        return self

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle(self._radius * other._radius)
        else:
            return Circle(self._radius * other)

    def __rmul__(self, other): # circle * 2 = 2 * circle
        if isinstance(self, Circle):
            return Circle(self._radius * other)
        else:
            return Circle(self * other.radius)

    def __eq__(self, other):
        return (self._radius == other.radius)

    def __lt__(self, other):
        return (self._radius < other.radius)

    def sort_key(self):
        return self._radius

    def sort(self):
        new_list = sorted(self, key=Circle.sort_key)
        self = new_list

class Sphere(Circle):
    @property
    def area(self):
        if isinstance(self, Sphere):
            return 4 * pi * (self._radius ** 2)
        else:
            raise (NotImplementedError, 'None Sphere object.')

    @property
    def volume(self):
        return (3 / 4) * pi * (self._radius ** 3)

    def __str__(self):
        return 'Sphere with radius: {}'.format(self._radius)

    def __repr__(self):
        return 'Sphere({})'.format(self._radius)
