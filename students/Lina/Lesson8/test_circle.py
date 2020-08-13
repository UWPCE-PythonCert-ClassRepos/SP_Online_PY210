"""
test code for circle.py
"""

import pytest
import math
import random

# import * is often bad form, but makes it easier to test everything in a module.
from circle import *


#########
# Step 1 - Initialze the radius
#########
def test_init():
    c = Circle(4)
    assert c.radius == 4

########
# Step 2 - Get the diameter
########
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

########
# Step 3 - Set the diameter
########
def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1
    c.diameter = 12.5
    assert c.diameter == 12.5
    assert c.radius == 6.25

########
# Step 4 - Get the area
########
def test_area():
    c = Circle(2)
    assert pytest.approx(c.area) == 12.566370

    #test that exception is raised if the user tries to set the area
    with pytest.raises(Exception):
        c.area = 42

########
# Step 5 - Alternate constructor: let the user create a Circle directly with
#          the diameter
########
def test_from_diameter():
   c = Circle.from_diameter(8)
   assert c.diameter == 8
   assert c.radius == 4

########
# Step 6 - Test str and repr
########
def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"

    d = eval(repr(c))
    assert d == c

########
# Step 7 - Test numeric protocols, add and multiply two circles
########
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 + c2) == Circle(6)

def test_mul():
    c2 = Circle(4)
    assert (c2 * 3) == Circle(12)

def test_rmul():
    c2 = Circle(4)
    assert (3 * c2) == (c2 * 3)

########
# Step 8 - Compare two circles, sort the circles
########
def test_gt():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 > c2) == False
    assert(c2 > c1) == True
    assert(c2 > c3) == False

def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 < c2) == True
    assert(c2 < c1) == False
    assert(c2 < c3) == False

def test_eq():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 == c2) == False
    assert(c2 == c3) == True

def test_sort_1():
    Circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2),
               Circle(3), Circle(5), Circle(9), Circle(1)]
    Circles.sort()
    assert Circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5),
                       Circle(6), Circle(7), Circle(8), Circle(9)]

def test_sort_2():
    Circles1 = [Circle(i) for i in random.sample(range(50), 50)]   #random order
    Circles2 = [Circle(i) for i in range(50)]                      #sequential order
    #make sure the list for sorting is not yet in sequential order
    assert Circles1 != Circles2

    Circles1.sort()
    assert Circles1 == Circles2

########
# Step 8 - Optional features
########
def test_idd():
    c1 = Circle(2)
    c2 = Circle(3)
    c1 += c2
    assert c1 == Circle(5)

def test_imul():
    c = Circle(5)
    c *= 2
    assert c == Circle(10)

def test_truediv():
    c = Circle(8)
    c = c / 2
    assert c == Circle(4)
    c = Circle(20.5)
    c = c / 5
    assert c == Circle(4.1)

def test_itruediv():
    c = Circle(15)
    c /= 3
    assert c == Circle(5)
    c = Circle(20)
    c /= 7
    assert round(c.radius, 6)  == pytest.approx(2.857143)

def test_ge():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 >= c2) == False
    assert(c2 >= c1) == True
    assert(c2 >= c3) == True

def test_le():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 <= c2) == True
    assert(c2 <= c1) == False
    assert(c2 <= c3) == True

def test_ne():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert(c1 != c2) == True
    assert(c2 != c3) == False

def test_circumference():
    c = Circle(3)
    assert pytest.approx(c.circumference) == 18.84954

    #test that exception is raised if the user tries to set the circumference
    with pytest.raises(Exception):
        c.circumference = 25

########
# Step 9 - Sphere
########
def test_sphere_str():
    s = Sphere(4)
    assert str(s) == "Sphere with radius: 4.000000"

def test_sphere_repr():
    s = Sphere(4)
    assert repr(s) == "Sphere(4)"

    d = eval(repr(s))
    assert d == s

def test_sphere_volume():
    s= Sphere(2)
    assert pytest.approx(s.volume) == 33.510291

    #test that exception is raised if the user tries to set the volume
    with pytest.raises(Exception):
        s.volume = 42

def test_sphere_area():
    s= Sphere(2)
    assert pytest.approx(s.area) == 50.26544

    #test that exception is raised if the user tries to set the sufrace area
    with pytest.raises(Exception):
        s.area = 45

#Test some of the methods and properties that do not need overrides, all
#should work for a sphere
def test_sphere_diameter():     #get diameter
    s = Sphere(4)
    assert s.diameter == 8

def test_sphere_set_diameter():
    s = Sphere(4)
    s.diameter = 2
    assert s.diameter == 2
    assert s.radius == 1
    s.diameter = 12.5
    assert s.diameter == 12.5
    assert s.radius == 6.25

def test_sphere_sort():
    Spheres1 = [Sphere(i) for i in random.sample(range(50), 50)]   #random order
    Spheres2 = [Sphere(i) for i in range(50)]                      #sequential order
    #make sure the list for sorting is not yet in sequential order
    assert Spheres1 != Spheres2

    Spheres1.sort()
    assert Spheres1 == Spheres2

def test_sphere_from_diameter():
   s = Sphere.from_diameter(8)
   assert s.diameter == 8
   assert s.radius == 4

def test_sphere_add():                #add two spheres
    s1 = Sphere(2)
    s2 = Sphere(4)
    assert (s1 + s2) == Sphere(6)

#The circumference property for the sphere is enabled in circle.py, so the
#codes below need to be commented out.
"""
def test_sphere_circumference():
    s = Sphere(4)
    with pytest.raises(NotImplementedError):
        s.circumference
"""
def test_sphere_circumference():
    s = Sphere(3)
    assert pytest.approx(s.circumference) == 18.84954
