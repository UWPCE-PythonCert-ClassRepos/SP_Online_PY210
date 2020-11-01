from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)
    
    @property
    def diameter(self):
        return self.radius*2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2
    
    @property
    def area(self):
        return pi*(self.radius**2)
    
    def __repr__(self):
        return f"A {self.__class__.__name__} of radius {self.radius}"