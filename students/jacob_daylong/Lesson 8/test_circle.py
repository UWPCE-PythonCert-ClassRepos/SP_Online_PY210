from circle import *
import pytest

def test_radius():
    #  Test Radius
    c = Circle(5)
    assert c.radius == 5
    c.radius = 5
    assert c.radius == 5

def test_diameter():
    # Test diameter
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 20
    assert c.radius == 10
    assert c.diameter == 20

def test_area():
    # Test Area
    c = Circle(5)
    assert c.area == 78.539816339744830961566084581988
    
def test_str():
    c = Circle(5)
    assert str(c) == "Circle with a radius of 5.00"

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"

def test_add():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(7)"

def test_multi():
    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 * c2
    assert repr(c3) == "Circle(12)"

def test_compare():
    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(3)

    assert c1 < c2
    assert c2 > c1
    assert c1 == c3
    assert c1 != c2
    
def test_sort():
    c1 = Circle(3)
    c2 = Circle(5)
    c4 = Circle(2)

    circles = [c1, c2, c4]
    circles.sort()
    assert circles == [Circle(2), Circle(3), Circle(5)]

def test_sphere():
    s = Sphere(5)
    assert s.area == 314.15926535897932384626433832795
    assert s.volume == 523.59877559829887307710723054658
    assert str(s) == "Sphere with a radius of 5.00"
    assert repr(s) == "Sphere(5)"