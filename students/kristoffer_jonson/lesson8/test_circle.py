import pytest
import math
import random
from circle import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_dimater_setter():
    c=Circle(4)
    c.diameter = 4
    assert c.radius == 2

def test_area():
    c=Circle(4)
    assert c.area == math.pi * 4 * 4

def test_from_Diameter():
    c=Circle.from_diameter(8)
    c2 = Circle(4)
    assert c.area == c2.area
    assert c.radius == c2.radius
    assert c.diameter == c2.diameter

def test_add():
    c = Circle(4)
    c2 = Circle(2)
    c3 = Circle(4) + Circle(2)
    assert c3.radius == 6

def test_sub():
    c = Circle(4)
    c2 = Circle(2)
    c3 = Circle(4) - Circle(2)
    assert c3.radius == 2

def test_mul():
    c = Circle(4)
    c2 = Circle(2)
    c3 = Circle(4) * Circle(2)
    assert c3.radius == 8
    c3 = c * 10
    assert c3.radius == 40

def test_rmul():
    c= Circle(4)
    c= 2*c
    assert c.radius == 8

def test_gt():
    assert Circle(4) > Circle(2)

def test_lt():
    assert Circle(2) < Circle(4)

def test_eq():
    assert Circle(2) == Circle(2)

def test_sort():
    circles = list()
    for i in range(10):
        circles.append(Circle(i+1))
    random.shuffle(circles)
    print(circles)
    circles.sort()
    print(circles)
    # assert False
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9), Circle(10)]

def test_iadd():
    c = Circle(4)
    c += Circle(2)
    assert c.radius == 6

def test_imul():
    c = Circle(4)
    c *= Circle(2)
    assert c.radius == 8
    c *= 2
    assert c.radius == 16

def test_sphere_area():
    s = Sphere(2)
    assert s.radius == 2
    assert s.area == math.pi * 4 * 2 * 2

def test_sphere_volume():
    s = Sphere(2)
    assert s.volume == math.pi * 4/3 * 2 * 2 * 2