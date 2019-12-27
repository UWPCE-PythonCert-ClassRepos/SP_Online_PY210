"""
test code for circle.py
"""

import pytest
from math import pi
from circle import *


# Circle tests
def test_radius():
    """Make sure Circle class takes the radius attribute"""

    c = Circle(5)
    assert c.radius == 5


def test_radius_mutability():
    """Make sure each instance can set a new radius value"""

    c = Circle(5)
    c.radius = 7
    assert c.radius == 7


def test_diameter():
    """Test for correct diameter, given radius"""

    c = Circle(5)
    assert c.diameter == 10


def test_diameter_twice_radius():
    """Validate d is always twice r"""

    c = Circle(5)
    c.diameter = 8
    assert c.diameter == 8
    assert c.radius == 4


def test_area():
    """Test for correct area, given a radius"""

    c = Circle(5)
    assert round(c.area, 3) == 78.540


def test_from_diameter():
    """Validate can instantiate using diameter with from_diameter"""

    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8


def test_str():

    c = Circle(5)
    assert c.__str__() == "Circle with radius: 5"


def test_repr():

    c = Circle(5)
    assert c.__repr__() == "Circle(5)"


def test_add_circle():

    c1, c2 = Circle(5), Circle(7)
    assert c1 + c2 == Circle(12)


def test_multiply_circle():

    c = Circle(5)
    assert c * 8 == Circle(40)
    assert 8 * c == Circle(40)


def test_lt():

    c1, c2 = Circle(5), Circle(7)
    assert c1 < c2
    assert not c2 < c1


def test_ge():

    c1, c2, c3 = Circle(5), Circle(7), Circle(7)
    assert not c1 >= c2
    assert c2 >= c1
    assert c2 >= c3


def test_eq():

    c1, c2, c3 = Circle(5), Circle(7), Circle(7)
    assert not c1 == c2
    assert c2 == c3


# Sphere tests
def test_sphere_radius():
    """Make sure Sphere class takes the radius attribute"""

    s = Sphere(5)
    assert s.radius == 5


def test_sphere_radius_mutability():
    """Make sure each instance can set a new radius value"""

    s = Sphere(5)
    s.radius = 7
    assert s.radius == 7


def test_sphere_diameter():
    """Test for correct diameter, given radius"""

    s = Sphere(5)
    assert s.diameter == 10


def test_sphere_diameter_twice_radius():
    """Validate d is always twice r"""

    s = Sphere(5)
    s.diameter = 8
    assert s.diameter == 8
    assert s.radius == 4


def test_sphere_area():
    """Test for correct area, given a radius"""

    s = Sphere(5)
    assert round(s.area, 3) == 314.159


def test_sphere_from_diameter():
    """Validate can instantiate using diameter with from_diameter"""

    s = Sphere.from_diameter(8)
    assert s.radius == 4
    assert s.diameter == 8


def test_sphere_str():

    s = Sphere(5)
    assert s.__str__() == "Sphere with radius: 5"


def test_sphere_repr():

    s = Sphere(5)
    assert s.__repr__() == "Sphere(5)"


def test_add_sphere():

    s1, s2 = Sphere(5), Sphere(7)
    assert s1 + s2 == Sphere(12)


def test_multiply_sphere():

    s = Sphere(5)
    assert s * 8 == Sphere(40)
    assert 8 * s == Sphere(40)


def test_sphere_lt():

    s1, s2 = Sphere(5), Sphere(7)
    assert s1 < s2
    assert not s2 < s1


def test_sphere_ge():

    s1, s2, s3 = Sphere(5), Sphere(7), Sphere(7)
    assert not s1 >= s2
    assert s2 >= s1
    assert s2 >= s3


def test_sphere_eq():

    s1, s2, s3 = Sphere(5), Sphere(7), Sphere(7)
    assert not s1 == s2
    assert s2 == s3
