#!/usr/bin/env python3

import pytest, math
from circle import *

def test_create_circle():
    """
    Test creation of a circle and output of its radius.

    Expected output is:
    c1 -- raises TypeError
    c2 == 8
    c3 == 3.14
    """
    # Validate getting a TypeError if we don't pass a numeric radius
    with pytest.raises(TypeError):
        c1 = Circle('boo')

    # We should be able to set the radius to an integer...
    c2 = Circle(8)

    assert c2.radius == 8

    #... or a float
    c3 = Circle(3.14)
    assert c3.radius == 3.14


def test_diameter():
    """
    Test that the diameter property is set.

    Expected output:
    c.radius == 4
    c.diameter == 8
    """

    c = Circle(4)

    assert c.radius == 4
    assert c.diameter == 8


def test_update_diameter():
    """
    Test that the diameter can be manipulated, and the radius is updated in tandem.

    Expected output:
    c.radius (initial) == 3.5
    c.diameter (initial) == 7

    c.radius (updated) == 2.25
    c.diameter(updated) = 4.5
    """

    c = Circle(3.5)

    assert c.radius == 3.5
    assert c.diameter == 7

    c.diameter = 4.5

    assert c.radius == 2.25
    assert c.diameter == 4.5


def test_update_radius():
    """
    Test that the radius can be manipulated, and the diameter is updated in tandem.

    Expected output:
    c.radius (initial) == 4.25
    c.diameter (initial) == 8.5

    c.radius (updated) == 1.8
    c.diameter(updated) = 3.6
    """

    c = Circle(4.25)

    assert c.radius == 4.25
    assert c.diameter == 8.5

    c.radius = 1.8

    assert c.radius == 1.8
    assert c.diameter == 3.6


def test_area():
    """
    Test that the area is calculated and cannot be set.

    Expected output:
    c.area == ((5)^2) * pi
    """

    c = Circle(5)

    assert c.area == math.pow(5, 2) * math.pi

    with pytest.raises(AttributeError):
        c.area = 42


def test_define_with_diameter():
    """
    Test that the class can be instantiated using the from_diameter() classmethod.

    Expected output:
    c1.diameter == 15.5
    c1.radius == 7.75
    c2 -- raises TypeError
    """

    c1 = Circle.from_diameter(15.5)

    assert c1.diameter == 15.5
    assert c1.radius == 7.75

    with pytest.raises(TypeError):
        c2 = Circle.from_diameter('test')


def test_str_repr():
    """
    Test the __str__ and __repr__ methods.

    Expected output:
    str(c) == String with radius 10.00000
    repr(c) == Circle(10)
    """

    c = Circle(10)

    assert str(c) == 'Circle with radius 10.00000'
    assert repr(c) == 'Circle(10.0)'


def test_arithmetic():
    """
    Test the ability to add, subtract, multiply and divide circle objects.

    Expected output:
    (c1 + c2).radius == 15.5
    (c1 + 5).radius == 15
    (c1 - 2.3).radius == 7.7
    (c1 * c2).radius == 55
    (c1 * 3).radius == 30
    (c1 / 4).radius == 2.5
    (8 + c2).radius == 13.5
    (9 - c2).radius == 3.5
    (4 * c1).radius == 40
    (80 / c1).radius == 8
    """
    c1 = Circle(10)
    c2 = Circle(5.5)

    assert (c1 + c2).radius == 15.5
    assert (c1 + 5).radius == 15
    assert (c1 - 2.3).radius == 7.7
    assert (c1 * c2).radius == 55
    assert (c1 * 3).radius == 30
    assert (c1 / 4).radius == 2.5
    assert (8 + c2).radius == 13.5
    assert (9 - c2).radius == 3.5
    assert (4 * c1).radius == 40
    assert (80 / c1).radius == 8


def test_comparison():
    """
    Test the ability to compare circle objects.

    Expected output:
    c1 < c2
    c2 > c4
    c1 >= c3
    c1 >= c4
    c4 <= c3
    c3 >= c1
    c1 == c3
    c1 != c4
    """
    c1 = Circle(10)
    c2 = Circle(12.5)
    c3 = Circle(10)
    c4 = Circle(3)

    assert c1 < c2
    assert c2 > c4
    assert c1 >= c3
    assert c1 >= c4
    assert c4 <= c3
    assert c3 >= c1
    assert c1 == c3
    assert c1 != c4


def test_ordering():
    """
    Test ordering Circle objects.

    Expected output:
    [Circle(1.0), Circle(1.5), Circle(3.0), Circle(4.5), Circle(5.0), Circle(5.25), Circle(8.0)]
    """
    circles = [Circle(8), Circle(4.5), Circle(3), Circle(5), Circle(1), Circle(5.25), Circle(1.5)]

    circles.sort()

    print(circles)
    assert circles == [Circle(1.0), Circle(1.5), Circle(3.0), Circle(4.5), Circle(5.0), Circle(5.25), Circle(8.0)]


def test_reflective_augmented():
    """
    Test reflected and augmented arithmetic functions.

    Expected output:
    2 + c1 == Circle(10)
    4 - c2 == Circle(1)
    9 * c2 == Circle(27)
    12 / c2 == Circle(4)

    c2 += 4, c2 == Circle(7)
    c1 += c2, c1 == Circle(15)
    c1 -= c2, c1 == Circle(8)
    c1 -= 2, c1 == Circle(6)
    c1 *= c2, c1 == Circle(42)
    c2 *= 9, c2 == Circle(63)
    c1 /= c3, c1 == Circle(21)
    c2 /= 3, c2 == Circle(21)
    """
    c1 = Circle(8)
    c2 = Circle(3)
    c3 = Circle(2)

    assert 2 + c1 == Circle(10)
    assert 4 - c2 == Circle(1)
    assert 9 * c2 == Circle(27)
    assert 12 / c2 == Circle(4)

    c2 += 4
    assert c2 == Circle(7)
    c1 += c2
    assert c1 == Circle(15)
    c1 -= c2
    assert c1 == Circle(8)
    c1 -= 2
    assert c1 == Circle(6)
    c1 *= c2
    assert c1 == Circle(42)
    c2 *= 9
    assert c2 == Circle(63)
    c1 /= c3
    assert c1 == Circle(21)
    c2 /= 3
    assert c2 == Circle(21)


def test_sphere():
    """
    Test functionality of the Sphere subclass

    Expected output:
    s1.diameter == 24
    s1.area == 4*pi*(12^2)
    s1.volume == (4/3)*pi*(12^3)
    str(s1) == Sphere with radius 12.00000
    repr(s1) == Sphere(12)
    s2.radius == 5
    """
    s1 = Sphere(12)

    assert s1.diameter == 24
    assert s1.area == 4 * math.pi * math.pow(s1.radius,2)
    # This was in a different order than the function which resulted in a different value
    # in the 12th decimal place, failing this test.  Guessing Cpython is casting to a float
    # at different points resulting in different precision?
    assert s1.volume == (4/3) * math.pow(s1.radius, 3) * math.pi
    assert str(s1) == 'Sphere with radius 12.00000'
    assert repr(s1) == 'Sphere(12.0)'

    s2 = Sphere.from_diameter(10)

    assert s2.radius == 5
