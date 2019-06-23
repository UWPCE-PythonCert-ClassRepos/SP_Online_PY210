"""
Testing circle.py for CIRCLES!
"""
from circle import *
import math

def test_radius():
    a, b = Circle(10), Circle(4)

    assert a.radius == 10
    assert b.radius == 4

def test_diameter():
    a, b, c = Circle(10), Circle(4), Circle(1)

    assert a.diameter == 20
    assert b.diameter == 8
    assert c.diameter == 2

    d = Circle(5)
    d.diameter = 5

    assert d.diameter == 5
    assert d.radius == 2.5

    e = Circle(400000)
    e.diameter = 9

    assert e.diameter == 9
    assert e.radius == 4.5

def test_area():
    a = Circle(7)
    assert a.area == math.pi * a.radius * a.radius
    assert a.area == math.pi * a.radius * (a.diameter/2)
    assert a.area == math.pi * (a.diameter/2) * (a.diameter/2)

def test_str():
    a = Circle(50)
    assert a.__str__() == 'Circle with a radius of 50'

    b = Circle(0)
    assert b.__str__() == 'Circle with a radius of 0'

def test_repr():
    a = Circle(9869876)
    assert a.__repr__() == 'Circle(9869876)'

def test_add():
    a, b = Circle(67), Circle(33)
    assert a + b == 100

def test_sub():
    a, b = Circle(3), Circle(1)
    assert a - b == 2

def test_mult():
    a = Circle(3)
    assert a * 8 == 24
    b = Circle(2)
    assert a * b == 6

def test_lt():
    a, b = Circle(0), Circle(4)
    b.diameter = 1
    c = Circle(2)
    assert b > a
    assert c > b

def test_sort():
    a = [Circle(78), Circle(0), Circle(-6), Circle(9), Circle(2323)]
    a.sort()
    assert a == [Circle(-6), Circle(0), Circle(9), Circle(78), Circle(2323)]

"""
Testing circle.py for SPHERES!
"""

def test_radius_sph():
    a, b = Sphere(1), Sphere(3)
    assert a == 1
    assert b == 3

def test_diameter_sph():
    a, b = Sphere(1), Sphere(3)
    assert a.diameter == 2
    assert b.diameter == 6

def test_area_sph():
    a, b = Sphere(1), Sphere(3)
    assert a.area == 4 * math.pi * (a.radius ** 2)
    assert a.area == 4 * math.pi * ((a.diameter / 2) ** 2)
    assert b.area == 4 * math.pi * (b.radius ** 2)
    assert b.area == 4 * math.pi * ((b.diameter / 2) ** 2)

def test_vol_sph():
    a, b = Sphere(1), Sphere(3)
    assert a.volume == (4/3) * math.pi * ((a.radius) ** 3)
    assert a.volume == (4/3) * math.pi * ((a.diameter / 2) ** 3)
    assert b.volume == (4/3) * math.pi * ((b.radius) ** 3)
    assert b.volume == (4/3) * math.pi * ((b.diameter / 2) ** 3)

def test_str_sph():
    a = Sphere(50)
    assert a.__str__() == 'Sphere with a radius of 50'

def test_repr_sph():
    a = Sphere(9869876)
    assert a.__repr__() == 'Sphere(9869876)'
