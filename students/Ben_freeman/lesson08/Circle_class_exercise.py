import math


class Circle(object):

    def __init__(self,radius_value):
        self.radius = radius_value

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        new_radius=self.radius + other.radius
        return Circle(new_radius)

    def __mul__(self, other):
        new_radius=self.radius*other
        return Circle(new_radius)

    def __rmul__(self, other):
        new_radius=self.radius*other
        return Circle(new_radius)

    def __eq__(self, other):
        return self.radius==other.radius

    def __le__(self, other):
        return self.radius<=other.radius

    def __ge__(self, other):
        return self.radius>=other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @property
    def diameter(self):
        return 2*self.radius

    @diameter.setter
    def diameter(self,value):
        self.radius = value/2
    
    @property
    def area(self):
        return self.radius**2*math.pi

    @area.setter
    def area(selfs,value):
        raise AttributeError

    @classmethod
    def from_diameter(cls,value):
        return Circle(value/2)



class Sphere(Circle):

    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere with radius: {self.radius}"

    @property
    def volume(self):
        return 4/3 * self.radius ** 3 * math.pi

    @property
    def area(self):
        return 4 * self.radius**2*math.pi
