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
    
    def __str__(self):
        return f"A {self.__class__.__name__} of radius {self.radius}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"
    
    def __add__(self, other):
        return self.__class__(self.radius+other.radius)
        
    def __iadd__(self, other):
        return self + other
    
    #used value instead of other because I'm multiplying by a number, not another circle
    def __mul__(self, value):
        return self.__class__(self.radius*value)
    
    def __imul__(self, value):
        return self * value

    def __rmul__(self, value):
        return self * value