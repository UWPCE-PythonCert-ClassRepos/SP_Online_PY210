import math

## step 1 ##
class Circle(object):
    def __init__(self , radius):
        self.radius = radius

## step 2, 3 ##
    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self , value):
        self.radius = value/2

## step 4 ##
    @property
    def area(self):
        return math.pi*self.radius**2

    @area.setter
    def area(self , value):
        raise AttributeError('area cannot be set')

## step 5 ##
    @classmethod 
    def from_diameter(cls , value):
        return cls(value/2)

## step 6 ##
    def __str__(self):
        return 'Circle with radius: {:f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

## step 7 ##
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __mul__(self, factor): 
        return Circle(self.radius * factor)

    def __rmul__(self, factor): 
        return Circle(self.radius * factor)

## step 8 ##
    def __gt__(self, other): 
        return (self.radius > other.radius)

    def __lt__(self, other):  
        return (self.radius < other.radius)      
        
    def __eq__(self, other): 
        return (self.radius == other.radius)

## step 9 ##
class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius: {:f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self): 
        return (4/3)*math.pi*self.radius**3

    @volume.setter
    def volume(self , value):
        raise AttributeError('volume cannot be set')
        
    @property
    def area(self):
        raise NotImplementedError

    @area.setter
    def area(self , value):
        raise NotImplementedError






