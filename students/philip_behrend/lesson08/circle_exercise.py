import math
class Circle:
    """ This class is constructs a basic circle object """
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return 2*self._radius
    @property
    def area(self):
        return math.pi*self._radius**2

    @diameter.setter
    def diameter(self,value):
        self._radius = value/2

    @classmethod
    def from_diameter(cls,value):
        return cls(value/2)

    def __str__(self):
        return "Circle with radius: {}".format(str(self._radius))

    def __repr__(self):
        return 'Circle({})'.format(str(self._radius))

    def __add__(self,v):
        assert isinstance(v,Circle)
        return Circle(self._radius+v._radius)

    def __mul__(self,value):
        return Circle(value*self._radius)
    
    def __truediv__(self,v):
        return Circle(self._radius/v._radius)
    
    def __rmul__(self,value):
        return Circle(value*self._radius)
        
    def __lt__(self,v):
        return (self._radius) < (v._radius)

    def __gt__(self,v):
        return (self._radius) > (v._radius)

    def __eq__(self,v):
        return (self._radius) == (v._radius)

class Sphere(Circle):
    @property
    def volume(self):
        return 4/3*math.pi*pow(self._radius,3)
    @property
    def area(self):
        return 4*math.pi*pow(self._radius,2)
    def __str__(self):
        return "Sphere with radius: {}".format(str(self._radius))

    def __repr__(self):
        return 'Sphere({})'.format(str(self._radius))
