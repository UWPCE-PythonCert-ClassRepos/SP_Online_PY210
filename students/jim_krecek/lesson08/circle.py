import math

class Circle:

    def __init__(self,rad):
        self.rad = rad
    
    @property
    def diameter(self):
        return self.rad*2
        
    @diameter.setter
    def diameter(self, dia):
        self.rad = dia/2
    
    @property
    def area(self):
        return math.pi*(self.rad**2)
    
    @classmethod
    def from_diameter(cls,diameter):
        rad = diameter/2
        return cls(rad)
        
    def __str__(self):
        return 'Circle with radius {0:.4f}'.format(self.rad)
        
    def __repr__(self):
        return 'Circle({})'.format(self.rad)
        
    def __add__(self, other):
        return self.__class__(self.rad + other.rad)
        
    def __mul__(self, other):
        return self.__class__(self.rad * other)
        
    def __lt__(self, other):
        return self.rad < other.rad
        
    def __eq__(self, other):
        return self.rad == other.rad

class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius {0:.4f}'.format(self.rad)
        
    def __repr__(self):
        return 'Sphere({})'.format(self.rad)
        
    @property
    def vol(self):
        return math.pi * (1.333333) * (self.rad**3)
    
    @property
    def area(self):
        return math.pi * 4 * (self.rad**2)