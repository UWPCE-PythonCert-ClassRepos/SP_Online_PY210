'''
#----------------------------------#
# Testing for Circle
#----------------------------------#
'''
from Circle import *
import math

def test_init():

    c1 = Circle(4)

def test_dia_prop():
    c1 = Circle(4)
    assert c1.radius == 4
    assert c1.diameter == 8
def test_area_prop():
    c1 = Circle(4)
    assert c1.area == math.pi * c1.radius * c1.radius

def test_alt_construct():
    c1 = Circle(4)
    c2 = Circle.from_diameter(8)
    print(c1.radius)
    print(c1.diameter)
    c1.diameter = 2
    assert c1.radius == 1
    assert c2.radius == 4

def test_arith():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    c4 = c2 * 3
    assert c3 == 'Circle(6)'
    assert c4 == 'Circle(12)'
def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 < c2) == True
    assert (c1 <= c2) == True
    assert (c1 == c2) == False
    assert (c1 > c2) == False
def test_sort():
    circles = [Circle(1), Circle(9), Circle(4)]
    circles.sort()
    assert circles == [Circle(1), Circle(4), Circle(9)]

#----------------------------------#
# Testing for Sphere
#----------------------------------#
def test_vol():
    s1 = Sphere(4)
    assert s1.volume == (4/3) * math.pi * (4 ** 3)

def test_compare():
    c1 = Sphere(2)
    c2 = Sphere(4)
    assert (c1 < c2) == True
    assert (c1 <= c2) == True
    assert (c1 == c2) == False
    assert (c1 > c2) == False