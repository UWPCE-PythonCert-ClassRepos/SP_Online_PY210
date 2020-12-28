
from math import pi

class Circle(object):
    

    def __init__(self, the_radius):
        self.radius = the_radius
        self._diameter = self.radius * 2
        
    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter / 2
        

    @property
    def area(self):
        area = round(self.radius ** 2 * pi, 2)
        return area
        
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Circle(radius)
        
    def __str__(self):
        return ('Circle with radius: ' + str(self.radius))

    def __repr__(self):
        return ('Circle({})'.format(self.radius))

    def grow(self, factor=2):
        self._diameter = self._diameter * factor

    def __len__(self):
        return len(self)

    def __add__(self, other):
        total_radius = self.radius + other.radius
        return Circle(total_radius)

    def __mul__(self, other):
        total_radius = self.radius * other
        return Circle(total_radius)

    def __lt__(self, other):
        return self.radius < other.radius

    
    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    def __str__(self):
        return ('Sphere with radius: ' + str(self.radius))

    def __repr__(self):
        return ('Sphere({})'.format(self.radius))
    @property
    def volume(self):
        volume = round(((4/3)* pi * self.radius ** 3), 2)
        return volume

    def area(self):
        raise NotImplementedError