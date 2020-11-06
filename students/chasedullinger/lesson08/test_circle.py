#!/usr/bin/env python

"""Circle class unit tests"""

import pytest
import math
import random
import circle


def test_circle_creation():
    c = circle.Circle(radius=10)

    #  Check that the new item is a circle object
    assert isinstance(c, circle.Circle)

    # check that radius initialized correctly
    assert c.radius == 10

    # set a new radius and check that it was set correctly
    c.radius = 15
    assert c.radius == 15

    # try to assign a negative radius (should raise ValueError)
    with pytest.raises(ValueError):
        c.radius = -10


def test_circle_diameter():
    c = circle.Circle(radius=10)

    #  Check that the new item is a circle object
    assert isinstance(c, circle.Circle)

    # check that diameter was correctly calculated
    assert c.diameter == 20

    # set a new diameter and check that it was set correctly
    c.diameter = 30
    assert c.diameter == 30
    assert c.radius == 15

    # try to assign a negative diameter (should raise ValueError)
    with pytest.raises(ValueError):
        c.diameter = -10


def test_circle_area():
    c = circle.Circle(radius=10)

    # check area math, should be pi*r^2
    assert c.area == math.pi * (10 ** 2)

    with pytest.raises(AttributeError):
        c.area = 100


def test_circle_from_diameter_creation():
    c = circle.Circle.from_diameter(diameter=10)

    #  Check that the new item is a circle object
    assert isinstance(c, circle.Circle)

    # check that radius initialized correctly
    assert c.radius == 5

    assert c.diameter == 10

    # try to instantiate a negative diameter (should raise ValueError)
    with pytest.raises(ValueError):
        c = circle.Circle.from_diameter(diameter=-10)


def test_circle_string_representation():
    c = circle.Circle(radius=10)
    # check that the string is created properly
    assert str(c) == "Circle with radius 10"


def test_circle_representation():
    c = circle.Circle(radius=10)
    # check that the repr is created properly
    assert repr(c) == "Circle(10)"


def test_add_circles():
    c1 = circle.Circle(2)
    c2 = circle.Circle(4)

    c3 = c1 + c2
    # Test that 2 circle objects add properly
    assert repr(c3) == "Circle(6)"
    # Test that a circle object can add a number properly
    c4 = c1 + 4

    assert repr(c4) == "Circle(6)"

    assert c1 + 4 == 4 + c1

    # would result in a negative radius
    with pytest.raises(ValueError):
        c5 = c1 + -50


def test_subtract_circles():
    c1 = circle.Circle(4)
    c2 = circle.Circle(2)

    c3 = c1 - c2

    assert repr(c3) == "Circle(2)"

    c4 = c1 - 2

    assert repr(c4) == "Circle(2)"


    # would result in a negative radius
    with pytest.raises(ValueError):
        c5 = c1 - 50


def test_multiply_circles():
    c1 = circle.Circle(2)

    c2 = c1 * 3

    assert repr(c2) == "Circle(6)"

    c3 = 3 * c1

    assert repr(c3) == "Circle(6)"

    assert 3 * c1 == c1 * 3

    # would result in a negative radius
    with pytest.raises(ValueError):
        c5 = c1 * -50


def test_divide_circles():
    c1 = circle.Circle(6)

    c2 = c1 / 3

    assert c2.radius == 2

    c3 = 6 / c1

    assert c3.radius == 1

    c4 = 12 / c1

    assert c4.radius == 2

    # would result in a negative radius
    with pytest.raises(ValueError):
        c5 = c1 / -50

def test_circle_equality():
    c1 = circle.Circle(2)
    c2 = circle.Circle(4)

    assert c1 < c2
    assert c2 > c1

    c3 = circle.Circle(4)

    assert c2 == c3

    assert c2 <= c3

    assert c2 >= c3

    assert c1 != c2


def test_circle_sorting():
    circles = [circle.Circle(i) for i in range(1, 11)]

    original_circles = [circle.Circle(i) for i in range(1, 11)]

    random.shuffle(circles)

    circles.sort()

    assert circles == original_circles


def test_circle_iadd():
    c1 = circle.Circle(5)

    c1 += 5

    assert c1.radius == 10

    with pytest.raises(ValueError):
        c1 += -15

    c2 = circle.Circle(5)
    c3 = circle.Circle(5)

    c2 += c3
    assert c2.radius == 10


def test_circle_isub():
    c1 = circle.Circle(10)

    c1 -= 5

    assert c1.radius == 5

    with pytest.raises(ValueError):
        c1 -= 15

    c2 = circle.Circle(15)
    c3 = circle.Circle(5)

    c2 -= c3
    assert c2.radius == 10
