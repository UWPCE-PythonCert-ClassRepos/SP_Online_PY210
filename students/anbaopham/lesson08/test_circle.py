import pytest
import math

from circle import *

def test_radius():
  c = Circle(4)
  assert c.radius == 4
  c.radius = 2
  assert c.radius == 2

def test_diameter():
  c = Circle(4)
  c.diameter = 2
  assert c.diameter == 2
  assert c.radius == 1

def test_area():
    c = Circle(2)
    print(c.area)
    try:
        c.area = 42
    except AttributeError:
        print("not good")

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_comparing():
    c = Circle(2)
    assert c*3 == Circle(6)
    assert 3*c == Circle(6)
    c1 = c * 3
    assert (c1 < c) == False
    assert (c1 > c) == True
    assert (c1 == c) == False

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    circles.sort()
    print(circles)
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

def test_sphere_volumn():
    s = Sphere(4)
    assert s.volumn() == 4/3 * math.pi * 4 ** 3

def test_sphere_area():
    s = Sphere(4)
    assert s.area() == 4 * math.pi * 4 ** 2

def test_sphere_area_from_diameter():
    s = Sphere.from_diameter(8)
    assert s.area() == 4 * math.pi * 4 ** 2
