from math import pi

class Circle():
    def __init__(self,radius):
        self.radius = radius

    def __str__(self):
        return 'Circle with radius: {:.2f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    @classmethod
    #Can create a circle from diameter instead
    def from_diameter(cls,diameter):
        return cls(diameter/2)

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self,value):
        self.radius = value/2

    @property
    def area(self):
        return pi*(self.radius)**2

    def __add__(self,c1):
        sum = self.radius + c1.radius
        return self.__class__(sum)

    def __mul__(self,val):
        prod = self.radius * val
        return self.__class__(prod)

    def __rmul__(self,val):
        return self.__mul__(val)

    def __eq__(self,other_circle):
        return self.radius == other_circle.radius

    def __lt__(self,other_circle):
        return self.radius < other_circle.radius

    def __gt__(self,other_circle):
        return self.radius > other_circle.radius


class Sphere(Circle):
    def __str__(self):
        return 'Sphere with radius: {:.2f}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        return (4/3)*pi*self.radius**3

    @property
    def area(self):
        return 4*pi*self.radius**2
