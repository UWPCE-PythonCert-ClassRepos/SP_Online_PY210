#!/usr/bin/env python3
import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2
        
    @diameter.setter 
    def diameter(self, d): 
        self.radius = d/2 

    @property
    def area(self):
        return self.radius*self.radius*math.pi
        
    @classmethod
    def from_diameter(cls,d):
        return cls(d/2)

    def __str__(self):
       return f'Circle with radius: {self.radius:.6f}' 


    #def __repr__(self):
        return "'Circle({})'".format(self.radius)






