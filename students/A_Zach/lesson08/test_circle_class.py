import pytest
from math import pi

from circle_class import *

def test_radius():

    c = Circle(4)
    assert c.radius == 4
    
def test_diameter():

    c = Circle(4)
    assert c.diameter == 4 * 2

def test_set_diamter():

    c = Circle(4)
    c.diameter = 6
    assert c.diameter == 6
    assert c.radius == 3

def test_area():
    
    c = Circle(4)
    assert c.area == pi * 4**2

def test_area_read_only():

    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 42

def test_from_diameter():
    
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_str():
    
    c = Circle(4)
    assert str(c) == "Circle with radius: 4.000000"
    
def test_repr():
    
    c = Circle(4)
    assert repr(c) == "Circle(4)"
    assert eval(repr(c)) == Circle(4)

def test_sum():
    
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)
    
def test_mul():
    
    c2 = Circle(4)
    assert c2 * 3 == Circle(12)
    assert 3 * c2 == Circle(12)

def test_eq():
    
    c1 = Circle(2)
    c2 = Circle(2)
    c3 = Circle(4)
    assert c1 == c2
    assert c1 < c3
    assert c3 > c2

def test_sort():
    
    circles =  [Circle(6), Circle(7), Circle(8), Circle(4)]
    circles.sort()
    assert circles == [Circle(4), Circle(6), Circle(7), Circle(8)]
    
def test_sphere():
    
    s1 = Sphere(2)
    assert s1.radius == 2
    assert s1.diameter == 2 * 2
    assert s1.area == 4 * pi * 2**2
    assert s1.volume == 4/3 * pi * 2**3
    
    #try to test combos
    s2 = Sphere(3)
    
    assert s1 + s2 == Sphere(5)
    assert s1 * 5 == Sphere(10)
    assert s2 > s1
    
def test_sphere_from_diameter():
    
    s1 = Sphere.from_diameter(4)
    assert s1.radius == 2