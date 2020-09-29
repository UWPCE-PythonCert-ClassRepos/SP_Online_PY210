import math as m

class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    # DIAMETER PROPERTY
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    # AREA PROPERTY
    @property
    def area(self):
        return self.radius * self.radius * m.pi

    @area.setter
    def area(self, area):
        raise AttributeError('The area could not be set')

    # initializes with diameter instead of radius
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # sets the string property of circle
    def __str__(self):
        return ('Circle with radius: {}'.format(self.radius))

    # sets repr property
    def __repr__(self):
        return ('Circle({})'.format(self.radius))

    # enables greater than comparision of Circle objects
    def __gt__(self, other):
        return self.radius > other.radius

    # enables less than comparision of Circle objects
    def __lt__(self, other):
        return self.radius < other.radius

    # enables equal comparision of Circle objects
    def __eq__(self, other):
        return self.radius == other.radius

    # enables adding of Circle objects
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # enables multiplying of Circle objects
    def __mul__(self, other):
        return Circle(self.radius * other)

    # Multiply circle objects in reverse order
    def __rmul__(self, other):
        return Circle(self.radius * other)


class Sphere(Circle):

    @property
    def volume(self):
        return self.radius * self.radius * self.radius * m.pi * (4 / 3)

    @property
    def area(self):
        return self.radius * self.radius * m.pi * 4

    # sets string property of Sphere
    def __str__(self):
        return ('Sphere with radius: {}'.format(self.radius))

    # sets repr property of Sphere
    def __repr__(self):
        return ('Sphere({})'.format(self.radius))