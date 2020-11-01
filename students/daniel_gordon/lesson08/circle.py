from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        self = cls()
        self.diameter = diameter
    
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
        return f"A circle of radius {self.radius}"