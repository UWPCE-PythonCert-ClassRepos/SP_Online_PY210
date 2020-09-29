# test code for simple_circle.py


import io
import pytest

from simple_circle import *


#def result(element, var=""):
#    outfile = io.StringIO()
#    if var:
#        element.Circle


def test_class():

    c = Circle(3)
    s = Sphere(5)

def test_diameter():
    c = Circle(4)
    s = Sphere(3)
    assert c.diameter == 8
    assert s.diameter == 6
#    print"for c = Circle(4) diamter = 8"

def test_radius():
    c = Circle(3)
    s = Sphere(5)
    assert c.radius == 3
    assert s.radius == (5)
#    print"for c = Circle(3) radius = 3"

def test_reverse():
    c = Circle(4)
    c.diameter = 4
    assert c.radius == 2

def test_area():
    c = Circle(2)
    s = Sphere(2)
    assert c.area == 12.56
    assert s.area == 50.24

def test_area_er():
    with pytest.raises(AttributeError):
        c = Circle(2)
        c.area = 2

def test_string():
    c = Circle(4)
    s = Sphere(5)
    print(c)
    assert "Circle with radius: 4.000000"
    print(s)
    assert "Sphere with radius: 5.000000"

def test_repr_circle():
    c = Circle(4)
    repr(c)
    assert "'Circle(4)'"
    d = eval(repr(c))
    d
    assert "Circle(4)"


def test_repr_sphere():
    s = Sphere(5)
    repr(s)
    assert "'Sphere(5)'"
    d = eval(repr(s))
    d
    assert "Sphere(5)"

def test_sum():
    c1 = Circle(2)
    c2 = Circle(3)
    s1 = Sphere(4)
    s2 = Sphere(7)
    s3 = s1 + s2
    assert "Circle(5)"
    c3 = c1 + c2
    assert "Sphere(11)"

def test_mult():
    c1 = Circle(2)
    s1 = Sphere(4)
    c1 * 2
    assert "Circle(4)"
    s1 * 2
    assert "Sphere(6)"

def test_comp():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = Circle(2)
    s1 = Sphere(4)
    s2 = Sphere(7)
    s3 = Sphere(4)
    assert c2 > c1
    assert s2 > s1
    assert c1.radius == c3.radius
    assert s1.radius == s3.radius

def test_list():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = Circle(1)
    circles = [c1, c2, c3]
    print(circles)
    assert [Circle(2), Circle(3), Circle(1)]
    circles.sort()
    print(circles)
    assert [Circle(5), Circle(2), Circle(3)]


