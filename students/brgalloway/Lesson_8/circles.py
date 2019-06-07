'''
Lesson Circle class
'''
import math 

class Circle(object): 
    
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
        return self.radius

    # area property 
    @property
    def area(self):
        return math.pi * (self.radius ** 2.0)

    # alternative constructor
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
    
    # print format
    def __str__(self):
        return f"circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"

    '''
    add, multiply, compare
    def __add__(self):
        pass
    def __multiply__(self):
        pass
    def __compare__(self):
        pass
    '''