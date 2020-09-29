"""
test code for Circle.py

"""

import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from Circle import *


# Step 1
def test_init():
    c = Circle(4)
    assert c.radius == 4


# Step 2
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8


# Step 3
def test_set_diameter():
    c = Circle(4)
    assert c.diameter == 8

    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


# Step 4
def test_area():
    c = Circle(2)
    assert c.area == 2**2 * math.pi

    with pytest.raises(AttributeError):
        c.area = 42


# Step 5
def test_from_diameter():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4


# Step 6
def test_str():
    c = Circle(8)
    print(c)
    print(repr(c))
    d = eval(repr(c))


# Step 7
def test_protocols():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6

    c4 = c2 * 3
    assert c4.radius == 12


# Step 8
def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c2 > c1
    assert not c1 > c2

    assert c2 == c3


def test_sort():
    circles = list()
    circles.append(Circle(6))
    circles.append(Circle(7))
    circles.append(Circle(8))
    circles.append(Circle(5))
    circles.append(Circle(0))
    circles.append(Circle(2))
    circles.append(Circle(3))
    circles.append(Circle(4))
    circles.append(Circle(9))
    circles.append(Circle(1))

    assert circles == [Circle(6), Circle(7), Circle(8),
                        Circle(5), Circle(0), Circle(2),
                        Circle(3), Circle(4), Circle(9),
                        Circle(1)]

    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2),
                        Circle(3), Circle(4), Circle(5),
                        Circle(6), Circle(7), Circle(8),
                        Circle(9)]


# Step 9
def test_sphere():
    s1 = Sphere.from_diameter(4)
    print(s1)
    print(repr(s1))
    # assert False

    assert s1.volume == (4 / 3) * 2**3 * math.pi

    with pytest.raises(NotImplementedError):
        s1.area
