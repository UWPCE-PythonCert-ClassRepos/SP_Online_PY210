import pytest
import math
from circle_exercise import Circle, Sphere

def test_radius():
    c1 = Circle(4)
    assert c1.radius == 4

def test_diameter():
    c1 = Circle(4)
    assert c1.diameter == 8

def test_setdiameter():
    c1 = Circle(4)
    assert c1.diameter == 8
    c1.diameter = 5
    assert c1.diameter == 5
    assert c1.radius == 2.5

def test_area():
    c1 = Circle(4)
    assert c1.area == math.pi*16

def test_str():
    c1 = Circle(5)
    assert str(c1) == 'Circle with radius: 5'

def test_repr():
    c1 = Circle(5)
    assert repr(c1) == 'Circle(5)'

def test_add():
    c1 = Circle(5)
    c2 = Circle(2)
    assert c1+c2 == Circle(7)

def test_mul():
    c1 = Circle(4)
    assert c1*2 == Circle(8)
    assert 2*c1 == Circle(8)

def test_floordiv():
    c1 = Circle(9)
    c2 = Circle(4)
    assert c1/c2 == Circle(2.25)

def test_gt():
    c1 = Circle(5)
    c2 = Circle(3)
    assert c1 > c2

def test_lt():
    c1 = Circle(5)
    c2 = Circle(3)
    assert c2 < c1

def test_eq():
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2

def test_sort():
    circles = [Circle(2),Circle(5),Circle(99),Circle(10)]
    circles.sort()
    assert circles == [Circle(2), Circle(5), Circle(10), Circle(99)]

def test_sphere_volume():
    s1 = Sphere(4)
    assert s1.volume == 4/3*math.pi*pow(4,3)    

def test_sphere_area():
    s1 = Sphere(4)
    assert s1.area == 4*math.pi*pow(4,2)   

    