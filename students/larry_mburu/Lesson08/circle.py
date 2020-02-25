import math 
from functools import total_ordering

@total_ordering
class Circle: 
    def __init__(self, radius):
        self.radius = radius 
    @property 
    def diameter(self): 
        return self.radius + self.radius 
    @diameter.setter
    def diameter(self, d): 
        self._diameter = d
        self.radius = self._diameter / 2 
    @property
    def area(self): 
        return math.pi * (self.radius ** self.radius)
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"
    def __repr__(self): 
        return f"Circle({self.radius})"
    def __add__(self, other): 
        return Circle(self.radius + other.radius)
    def __iadd__(self, other): 
        """
        handle cases where object expression is object += object
        """
        if isinstance(other, Circle):
            self.radius += other.radius
            return self 
        else: 
            self.radius += other # other is a numeric val ie. object += intval 
            return self   
    def __mul__(self, val): 
        return Circle(self.radius * val)
    def __rmul__(self, val): 
        """
        handles reflected(swapped) operands. 
        ie. val * obj vs. obj * val
        """
        return Circle(self.radius * val)
    def __lt__(self, other): 
        return self.radius < other.radius
    def __eq__(self, other): 
        return self.radius == other.radius
    def __itruediv__(self, other): 
        """
        produces half a circle.
        """
        if isinstance(other, Circle) and (other.radius < self.radius): 
            self.radius /= other.radius
            return self

    def sort_key(self):
        """
        use as a sort key when sorting collections
        """
        return self.radius

class Sphere(Circle): 
    def __str__(self): 
        return f"Sphere with radius: {self.radius:.6f}"
    def __repr__(self): 
        return f"Sphere({self.radius})"
    @property
    def volume(self): 
        vol = (4/3) * math.pi * (self.radius ** 3)
        return f"{vol:.1f}"
    @property
    def area(self): 
        raise NotImplementedError

if __name__ == '__main__': 
    c = Circle(4)
    print(f"radius is: {c.radius}")
    print(f"diameter is: {c.diameter}")
    c.diameter = 10 
    print(f"diameter is now: {c.diameter}")
    print(f"radius is {c.radius}")
    c = Circle.from_diameter(100)
    print(f"radius is now: {c.radius}")