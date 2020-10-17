#!/usr/bin/env python3
"""
A Circle class library
"""
import math

# Point
class Point(object):
    x = 0
    y = 0
    
    def __init__(self, x=0, y=0): # constructor in the origin
        self.x = x
        self.y = y
    
    def set(self, x=0, y=0): # setter
        self.x = x
        self.y = y
        
    def get(self): # getter
        return {"x":self.x, "y":self.y}
        
    def getx(self): # getter
        return self.x
    
    def gety(self): # getter
        return self.y

    def move(self, dx = 1, dy = 1):        
        self.x += dx
        self.y += dy
        return {"x":self.x, "y":self.y}
   
# Circle

class Circle(Point):
    radius = 1
    # Step 3: properties - diameter
    _diameter = None
    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter        
    def diameter(self, value):
        self.radius = value /2
        
    # Step 4: properties - area    
    _area = None
    @property
    def area(self):
        return self.radius ** 2 * math.pi
    
    # Step 5: alt constructor
    @classmethod
    def from_diameter(cls, diameter=None):
        self = cls()
        if diameter:
            self.radius = diameter / 2
        return self
    
    # Step 6: Special Methods
    
    def __str__(self):
        return f"Circle Object at: x={self.x}, y={self.y}; with: Radus={self.radius}, Diameter={self.diameter}, and Area={self.area}"
        

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.radius})"

    # Step 7: numeric protocols
    def __add__(self, other):
        """ Numeric addition of 2 Circles:
            - centers follow vector addition
            - radiuses add
            Resulting Circle is the circle with R = r1 + r2
            at coordinates: X = x1 + x2, Y = y1 + y2 """
        nc = Circle()    
        nc.x = self.x + other.x
        nc.y = self.y + other.y
        nc.radius = self.radius + other.radius
        return nc

    def __mul__(self, val): # make it order independent - only use 1st 2
        """ Numeric multiplication of a Circle:            
            - only radius gets multiplied
            Resulting Circle is the circle with R = r1 * val
            at same coordinates"""
        # if isinstance(self, (int, float)): # 1st argument is a number
            # self, val = val, self #swap arguments 
        
        nc = Circle()             # need to return a new object
        nc.x = self.x
        nc.y = self.y
        nc.radius = self.radius * val
        return nc
   
    def __rmul__(self, val): # reverse argument order
        return self.__mul__(val)
        
    # Step 8: comparisons

    def __lt__(self, other): #<  (less than)
        if self.radius < other.radius:
            return True
        else:
            return False
            
    def __gt__(self,other): # > (greater than)    
        if self.radius > other.radius:
            return True
        else:
            return False
            
    def __eq__(self,other): # == (equal)
        if self.radius == other.radius:
            return True
        else:
            return False
    def __ne__(self,other): # != (not equal)
        if self.radius != other.radius:
            return True
        else:
            return False
          
# __le__ : <= (less than or equal)
    def __le__(self, other): 
        if self.radius <= other.radius:
            return True
        else:
            return False

# __ge__ : >= (greater than or equal)
    def __ge__(self, other): 
        if self.radius >= other.radius:
            return True
        else:
            return False

    #======= regular stuff =============
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = radius*2
    
    def get(self): # getter
        return {"x":self.x, "y":self.y, "radius":self.radius}
        
    def set(self, x=0, y=0, radius=1): # setter
        self.x = x
        self.y = y
        self.radius = radius
        self.diameter = radius * 2

########
# Step 9 - Subclassing
########     

# Sphere

class Sphere(Circle):
    z = 0
    
    def set(self, x=0, y=0, z=0): # setter
        self.x = x
        self.y = y
        self.z = z
    def get(self): # getter
        return {"x":self.x, "y":self.y, "z":self.z, "radius":self.radius}
        
    def move(self, dx = 1, dy = 1, dz=1):        
        self.x += dx
        self.y += dy
        self.z += dz
        return {"x":self.x, "y":self.y,  "z":self.z}        
    
    _area = None
    @property
    def area(self):
        return self.radius ** 2 * math.pi * 4
    
    _volume = None
    @property
    def volume(self):
        return (self.radius ** 3 * math.pi * 4) / 3
    
    def __str__(self):
        return f"Sphere Object at: x={self.x}, y={self.y}, z={self.z}; with: Radus={self.radius}, Diameter={self.diameter}, Surface Area={self.area}, and Volume={self.volume}"
        

    def __repr__(self):
        return f"Sphere({self.x}, {self.y}, {self.z}, {self.radius})"
    
# Main and Sanity Checks   
if __name__ == "__main__":
    # init
    point = Point();
    print(point.x)
    print(point.y)
        
    print(point.getx())
    print(point.gety())
    print(point.get())
    
    point.set(15, 77)
    print(point.getx())
    print(point.gety())
    print(point.get())
    
    point.move(-5, 3)
    coords = point.get()
    
    print(point.getx())
    print(coords["x"])
    print(coords["y"])
    print(point.gety())
    print(point.get())
    
    point = Point(100, 200);
    print(point.x)
    print(point.y)
    
    c = Circle()
    print(c.x, c.y, c.radius)
    
    c = Circle(5)
    print(c.x, c.y, c.radius)
    
    print(c.get())
    print(c.diameter)
    c.diameter = 30
    print(c.radius)
    print(c.diameter)
    print(c.area)
    
    c = Circle(2)
    print(c.area)
    
    num = 1e-6
    
    print(num)
    
    try:
        c.area = 42
    except AttributeError:
        print("Attribute Error raised on Area property setter")
   # Step 5     
    cd = Circle.from_diameter(8)
    print(cd.diameter)
    print(cd.radius)
    
    # Step 6 - Special Methods
    
    c = Circle.from_diameter(32)    
    c.move(15, 20)
    print(c)
    
    print(repr(c))
    
    rs = c.__str__()
    print(rs)
    
    rp = c.__repr__()
    print(rp)
    
    c1 = Circle(2)
    c1.move(3, 5)
    c2 = Circle(4)
    c2.move(4, 3)
    
    
    print("Before =========================")
    print(c1)
    print(c2)
    cd = c1 + c2
    print("After =========================")
    print(c1)
    print(c2)    
    print(cd)
    
    c1 = Circle(2)
    c1.move(3, 5)
    nc = c1 * 5    
    print("mult 2 by 5:")
    print(nc)
    
    # todo
    print("referse arg order")
    nc = 5 * c1 
    print(nc)
    
    print("=== Comparisons: =============")
    less = c1 < c2
    print(c1,c2)
    print(less)
    more = c1 > c2
    print(c1 > c2)
    print(c1 != c2)
    
    
    c3 = Circle(15)
    print(c3)
    
    circles = [c3, c1 , c2]
    
    print(circles)
    circles.sort()
    print(circles)
    
    print("Sphere====================")
    sph = Sphere(7)
    print(sph.get())
    print(sph.move(3,5,11))
    
    
    print("Sphere Area: ", sph.area)
    print("Sphere Volume: ", sph.volume)
    
    
    sphn = Sphere.from_diameter(14)
    sphn.move(15, 20)
    print(sphn)
    print(repr(sphn))