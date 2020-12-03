#!/usr/bin/env python3
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.ask_diameter()
        self.calculate_area()
        
    def ask_diameter(self):
        value = input("Do you wish to provide the diameter of the cirlce? Enter 'Yes' or 'No': ")
        if value == "YES" or value == "Yes" or value == "yes":
            self.get_diameter()
        elif value == "NO" or value == "No" or value == "no":
            self.diameter = 2*self.radius
        else:
            self.ask_diameter()
            
    def get_diameter(self):
        diameter = input("Please enter the value of the circle's diameter: ")
        if str.isnumeric(diameter):
            self.diameter = int(diameter)
            self.radius = self.diameter/2
        else:
            print("The value you have entered is non-numeric. Please enter a numeric value.")
            self.get_diameter()

    def calculate_area(self):
        self.area = pi*self.radius*self.radius

    def add_circles(self, circle2):
        new_circle = Circle(self.radius + circle2.radius)
        return new_circle
    
    def multiply_circle(self, factor):
        new_circle = Circle(self.radius*factor)
        return new_circle

    def equal_circle(self, circle2):
        return self.radius == circle2.radius

    def greater_circle(self, circle2):
        return self.radius > circle2.radius

    def less_circle(self, circle2):
        return self.radius < circle2.radius

    def sort_cirles(self, circles):
        sorted_circles = sorted(circles, key=lambda c: c.radius)
        return sorted_circles

    @classmethod 
    def from_diameter(cls, diameter):
        """
        docstring
        """
        self = cls(diameter/2)
        return self

    def __repr__(self):
        return {'radius':self.radius, 'diameter':self.diameter, 'area':self.area}

    def __str__(self):
        return 'Circle(radius='+str(self.radius)+', diamter='+str(self.diameter)+', area='+str(self.area)+')'

class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.calculate_volume()

    def calculate_area(self):
        self.area = 4*pi*self.radius*self.radius
    
    def calculate_volume(self): 
        self.volume = (4/3)*pi*self.radius*self.radius*self.radius

    def __repr__(self):
        return {'radius':self.radius, 'diameter':self.diameter, 'area':self.area, 'volume':self.volume}

    def __str__(self):
        return 'Sphere(radius='+str(self.radius)+', diamter='+str(self.diameter)+', area='+str(self.area)+', volume='+str(self.volume)+')'