#!/usr/bin/env python

"""Sphere class unit tests"""

import pytest
import math
import random
import circle


def test_Sphere_creation():
    s = circle.Sphere(radius=10)

    #  Check that the new item is a Sphere object
    assert isinstance(s, circle.Sphere)

    # check that radius initialized correctly
    assert s.radius == 10

    # set a new radius and check that it was set correctly
    s.radius = 15
    assert s.radius == 15

    # try to assign a negative radius (should raise Value)
    with pytest.raises(ValueError):
        s.radius = -10


def test_Sphere_diameter():
    s = circle.Sphere(radius=10)

    #  Check that the new item is a Sphere object
    assert isinstance(s, circle.Sphere)

    # check that diameter was correctly calculated
    assert s.diameter == 20

    # set a new diameter and check that it was set correctly
    s.diameter = 30
    assert s.diameter == 30
    assert s.radius == 15

    # try to assign a negative diameter (should raise Value)
    with pytest.raises(ValueError):
        s.diameter = -10


def test_Sphere_area():
    s = circle.Sphere(radius=10)

    # check area math, should be pi*r^2
    assert s.area == 4 * math.pi * (10 ** 2)

    with pytest.raises(AttributeError):
        s.area = 100


def test_Sphere_volume():
    s = circle.Sphere(radius=10)

    # check area math, should be pi*r^2
    assert s.volume == (4 / 3) * math.pi * (10 ** 3)

    with pytest.raises(AttributeError):
        s.volume = 100


def test_Sphere_from_diameter_creation():
    s = circle.Sphere.from_diameter(diameter=10)

    #  Check that the new item is a Sphere object
    assert isinstance(s, circle.Sphere)

    # check that radius initialized correctly
    assert s.radius == 5

    assert s.diameter == 10

    # try to instantiate a negative diameter (should raise Value)
    with pytest.raises(ValueError):
        s = circle.Sphere.from_diameter(diameter=-10)


def test_Sphere_string_representation():
    s = circle.Sphere(radius=10)
    # check that the string is created properly
    assert str(s) == "Sphere with radius 10"


def test_Sphere_representation():
    s = circle.Sphere(radius=10)
    # check that the repr is created properly
    assert repr(s) == "Sphere(10)"


def test_add_Spheres():
    s1 = circle.Sphere(2)
    s2 = circle.Sphere(4)

    s3 = s1 + s2
    # Test that 2 Sphere objects add properly
    assert isinstance(s3, circle.Sphere)
    assert s3.radius == 6
    # Test that a Sphere object can add a number properly
    s4 = s1 + 4

    assert s4.radius == 6
    assert isinstance(s4, circle.Sphere)

    assert s1 + 4 == 4 + s1

    # would result in a negative radius
    with pytest.raises(ValueError):
        s5 = s1 + -50


def test_subtract_Spheres():
    s1 = circle.Sphere(4)
    s2 = circle.Sphere(2)

    s3 = s1 - s2
    # test that spheres subtract properly
    assert s3.radius == 2
    assert isinstance(s3, circle.Sphere)

    s4 = s1 - 2

    assert s4.radius == 2
    assert isinstance(s4, circle.Sphere)

    # would result in a negative radius
    with pytest.raises(ValueError):
        s5 = s1 - 50


def test_multiply_Spheres():
    s1 = circle.Sphere(2)

    s2 = s1 * 3

    # test that spheres multiply properly
    assert s2.radius == 6
    assert isinstance(s2, circle.Sphere)

    s3 = 3 * s1

    assert s3.radius == 6
    assert isinstance(s3, circle.Sphere)

    assert 3 * s1 == s1 * 3

    # would result in a negative radius
    with pytest.raises(ValueError):
        s5 = s1 * -50


def test_divide_Spheres():
    s1 = circle.Sphere(6)

    s2 = s1 / 3

    # test that spheres divide properly
    assert s2.radius == 2
    assert isinstance(s2, circle.Sphere)

    s3 = 6 / s1

    assert s3.radius == 1
    assert isinstance(s3, circle.Sphere)

    s4 = 12 / s1

    assert s4.radius == 2
    assert isinstance(s4, circle.Sphere)

    # would result in a negative radius
    with pytest.raises(ValueError):
        s5 = s1 / -50


def test_Sphere_equality():
    s1 = circle.Sphere(2)
    s2 = circle.Sphere(4)

    assert s1 < s2
    assert s2 > s1

    s3 = circle.Sphere(4)

    assert s2 == s3

    assert s2 <= s3

    assert s2 >= s3

    assert s1 != s2


def test_Sphere_sorting():
    spheres = [circle.Sphere(i) for i in range(1, 11)]

    original_spheres = [circle.Sphere(i) for i in range(1, 11)]

    random.shuffle(spheres)

    spheres.sort()

    assert spheres == original_spheres


def test_Sphere_iadd():
    s1 = circle.Sphere(5)

    s1 += 5

    assert s1.radius == 10
    assert isinstance(s1, circle.Sphere)

    with pytest.raises(ValueError):
        s1 += -15

    s2 = circle.Sphere(5)
    s3 = circle.Sphere(5)

    s2 += s3
    assert s2.radius == 10
    assert isinstance(s2, circle.Sphere)


def test_Sphere_isub():
    s1 = circle.Sphere(10)

    s1 -= 5

    assert s1.radius == 5
    assert isinstance(s1, circle.Sphere)

    with pytest.raises(ValueError):
        s1 -= 15

    s2 = circle.Sphere(15)
    s3 = circle.Sphere(5)

    s2 -= s3
    assert s2.radius == 10
    assert isinstance(s2, circle.Sphere)
