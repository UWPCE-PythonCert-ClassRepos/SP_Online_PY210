'''
Lesson 8 Circle class
'''
import math 

class Circle(object): 
    '''
    Circle class takes radius as a single parameter to initialize. 
    Inclues diameter, area, and an alternative constructor. 
    '''
    def __init__(self, radius):
        # populate instance with variable
        self.radius = radius

    # added diameter property
    @property
    def diameter(self):
        return self.radius * 2

    # allow radius to be set from diameter
    @diameter.setter
    def diameter(self, _diameter):
        self.radius = _diameter / 2

    # area property 
    @property
    def area(self):
        return math.pi * (self.radius ** 2.0)

    # alternative constructor
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
    
    '''
    magic methods
    '''
    # print format
    def __str__(self):
        return f"circle with radius {self.radius}"
    def __repr__(self):
        return f"Circle({self.radius})"
    # compare instances and ensure given raidus is less than
    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    # add two instances together
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    # multiply instances together
    def __mul__(self, other):
        return Circle(self.radius * other.radius)

class Sphere(Circle):
    '''
    Sphere objects inherit from the Circle class. 
    Takes radius as a single parameter to initialize. 
    '''
    @property
    def volume(self):
        return ((4/3) * math.pi) * (self.radius ** 3.0)

    @property 
    def area(self):
        raise NotImplementedError

    # print format
    def __str__(self):
        return f"sphere with a volume of {self.volume:.2f}"
    def __repr__(self):
        return f"Sphere({self.volume:.2f})"