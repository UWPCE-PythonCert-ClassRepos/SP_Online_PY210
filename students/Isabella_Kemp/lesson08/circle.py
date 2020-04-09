# Isabella Kemp
# Circle Class Exercise

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
    # Add a diameter property so the user can get diameter of circle
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        raise AttributeError

    # Allows user to set diameter of circle
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


    @classmethod
    def from_diameter(cls, diam):
        radius = diam / 2
        return cls(radius)
    
    def __str__(self):
        return f"Circle with radius of {self.radius}"
    
    def __repr__(self):
        return 'Circle({})'.format(self.radius)
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        new_radius = self.radius * other.radius
        return Circle(new_radius)
    
    def __rmul__(self, other):
        new_radius = self.radius * other.radius
        return Circle(new_radius)
   
    def __eq__(self, other):
        return self.radius == other.radius

    def __le__(self, other):
        return self.radius <= other.radius
   
    def __ge__(self, other):
        return self.radius >= other.radius
       
    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius


class Sphere(Circle):

    def __repr__(self):  # prints sphere
        return f'Sphere({self.radius})'
    
    def __str__(self):
        return f'Sphere with radius of {self.radius}'
    
    @property
    def area(self):
        return round(4 * math.pi * self.radius ** 2, 5)
        
    @property
    def volume(self):
        return round(4 / 3 * math.pi * self.radius ** 3, 5)
