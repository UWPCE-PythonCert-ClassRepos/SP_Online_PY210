"""
test code for circle_cass.py
"""

import io, math
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle_class import *

########
# Base Point Class Tests
########

# Constructor
def test_point_init_def(): 
    p = Point()
    assert p.x == 0
    assert p.y == 0

def test_point_init(): 
    p = Point(100, 200)
    assert p.x == 100
    assert p.y == 200

# Setter
def test_point_set(): 
    p = Point()
    p.set(15,25)
    assert p.x == 15
    assert p.y == 25

# default setter moves to the origin
def test_point_set_def(): 
    p = Point() 
    p.set()
    assert p.x == 0
    assert p.y == 0

# Getter x and y
def test_point_getxy(): 
    p = Point(1000, 2500)
    assert p.getx() == 1000
    assert p.gety() == 2500

# coord getter 
def test_point_get(): 
    p = Point(777, 999)
    coords = p.get()
    assert coords["x"] == 777
    assert coords["y"] == 999
    assert coords == {"x":777, "y":999}


########
# Step 1 - Circle constructor
########

def test_circle_init(): 
    c = Circle()
    assert c.radius == 1

    c = Circle(5)
    assert c.radius == 5

    getc = c.get()
    assert getc == {"x":0, "y":0, "radius":5}

def test_circle_set(): 
    c = Circle()
    c.set(15,20,7)
    
    getc = c.get()
    assert getc == {"x":15, "y":20, "radius":7}

def test_circle_move(): 
    c = Circle()
    c.set(15,20,7)
    c.move(-5,7)
    getc = c.get()
    assert getc == {"x":10, "y":27, "radius":7}

########
# Step 2 - Circle diameter
########

def test_circle_diameter(): 
    c = Circle(3)    
    assert c.diameter == 6
########
# Step 3 - Circle diameter getter
########

def test_circle_diameter_getter(): 
    c = Circle(3)    
    c.diameter = 16
    assert c.radius == 8

########
# Step 4 - Circle area
########

def test_circle_area(): 
    c = Circle(2)    
    assert (c.area - 12.566370) < 1e-6
    
def test_circle_area_set():
    with pytest.raises(AttributeError):
        c = Circle(2)    
        c.area = 42

########
# Step 5 - alt constructor
########

def test_circle_alt_constructor():
    c = Circle.from_diameter(32)    
    assert c.diameter == 32
    assert c.radius == 16
        
########
# Step 6 - Special Methods
########
def test_circle_str():
    c = Circle.from_diameter(32)    
    c.move(15, 20)
    # print(c.__str__)
    assert c.__str__() == 'Circle Object at: x=15, y=20; with: Radus=16.0, Diameter=32.0, and Area=804.247719318987'

def test_circle_repr():
    c = Circle.from_diameter(32)    
    c.move(15, 20)
    # print(c.__str__)
    assert c.__repr__() == 'Circle(15, 20, 16.0)'
 
########
# Step 7 - Numeric Protocols
########
 
def test_circle_add():
    c1 = Circle(2)
    c1.move(3, 5)
    c2 = Circle(4)
    c2.move(4, 3)
    nc = c1 + c2
    assert nc.__repr__() == 'Circle(7, 8, 6.0)'
    
def test_circle_mult():
    c1 = Circle(2)
    c1.move(3, 5)
    nc = c1 * 5    
    assert nc.__repr__() == 'Circle(3, 5, 10.0)'
        
def test_circle_reverse_mult():
    c1 = Circle(2)
    c1.move(3, 5)
    nc = 7.5 * c1
    assert nc.__repr__() == 'Circle(3, 5, 15.0)'
        
########
# Step 8 - Comparisons
########        

def test_circle_comparisons():
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = Circle(5)

    assert (c1 < c2) == True
    assert (c1 > c3) == False
    assert (c3 > c2) == False
    assert (c3 < c2) == False
    assert (c3 >= c2) == True
    assert (c3 <= c2) == True
    assert (c3 == c2) == True
    assert (c3 != c2) == False
    
def test_circle_sort():
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = Circle(15)
    circles = [c3, c1 , c2]
    
    cr = str(circles.__repr__())
    print(cr)
    
    assert circles.__repr__() == '[Circle(0, 0, 15.0), Circle(0, 0, 2.0), Circle(0, 0, 5.0)]'
    circles.sort()
    assert circles.__repr__() == '[Circle(0, 0, 2.0), Circle(0, 0, 5.0), Circle(0, 0, 15.0)]'

        
########
# Step 9 - Subclassing Sphere
########        

def test_sphere():
    sph = Sphere(7)
    print(sph.get())
    coords = sph.get() 
    assert coords == {'x': 0, 'y': 0, 'z': 0, 'radius': 7.0}
    print(sph.move(3,5,11))    
    assert sph.x == 3
    assert sph.y == 5
    assert sph.z == 11
    assert sph.radius == 7.0
    assert sph.diameter == 14.0
    

def test_sphere_surf_area():
    sph = Sphere(7)
    assert (sph.area - 615.75164) < 1e-2

def test_sphere_volume():
    sph = Sphere(7)
    assert (sph.volume - 1436.7538) < 1e-2
        
def test_sphere_str():
    c = Sphere.from_diameter(14)    
    c.move(15, 20)
    # print(c.__str__)
    assert c.__str__() == 'Sphere Object at: x=15, y=20, z=1; with: Radus=7.0, Diameter=14.0, Surface Area=615.7521601035994, and Volume=1436.755040241732'
    assert c.__repr__() == 'Sphere(15, 20, 1, 7.0)'        
       