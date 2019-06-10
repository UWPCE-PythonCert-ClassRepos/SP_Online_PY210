import pytest
from circle import *

# STEP 1 | Test radius
def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4


# STEP 2 | Test diameter
def test_circle_diameter():
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8
    assert c.diameter == c.radius * 2


# STEP 3 | Set diameter
def test_set_circle_diameter():
    c = Circle(4)
    c.diameter = 4

    assert c.diameter == 4
    assert c.radius == 2
    assert c.diameter == c.radius * 2


# STEP 4 | Test area
def test_area():
    c = Circle(2)
    assert c.area == math.pi * c.radius ** 2
    # c.area = 20


# STEP 5 | Test from_diameter
def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


# STEP 6 | Test str and repr
def test_str():
    c = Circle(8)
    assert str(c) == 'Circle with radius: 8'

def test_repr():
    c = Circle(8)
    assert repr(c) == 'Circle(8)'


# STEP 7 | Test numeric protocol
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(6)'
    assert (c1 + c2).radius == 6


# STEP 8 | Test compare protocol
def test_multiply():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 * 3) == 'Circle(6)'
    assert repr(3 * c2) == 'Circle(12)'

def test_compare():
    c1 = Circle(10)
    c2 = Circle(14)
    assert (c1 > c2) == False
    assert (c1 >= c2) == False
    assert (c1 < c2) == True
    assert (c1 <= c2) == True
    assert (c1 != c2) == True
    assert (c1 == c2) == False
    assert (c1*3 == 3*c1) == True

    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles_sort = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    circles.sort()

    assert (circles == circles_sort) == True


# STEP 9 | Test Sphere using the circle class
def test_sphere():
    s1 = Sphere(4)
    s2 = Sphere(8)

    assert s1.radius == 4
    assert s2.diameter == 16
    assert s1.diameter == s1.radius * 2

    assert s1.area == 4 * math.pi * s1.radius ** 2
    assert s2.volume == (4/3) * math.pi * s2.radius ** 3

    assert str(s1) == 'Sphere with radius: 4'
    assert repr(s2) == 'Sphere(8)'
    assert repr(s1 + s2) == 'Sphere(12)'

    s3 = Sphere.from_diameter(8)
    assert s3.diameter == 8
    assert s3.radius == 4

    assert (s1 > s2) == False
    assert (s1 >= s2) == False
    assert (s1 < s2) == True
    assert (s1 <= s2) == True
    assert (s1 != s2) == True
    assert (s1 == s2) == False
    assert (s1*3 == 3*s1) == True

    spheres = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    spheres_sort = [Sphere(0), Sphere(1), Sphere(2), Sphere(3), Sphere(4), Sphere(5), Sphere(6), Sphere(7), Sphere(8), Sphere(9)]
    spheres.sort()

    assert (spheres == spheres_sort) == True
