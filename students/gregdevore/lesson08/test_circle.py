#!/usr/bin/env python3

# Test suite for Circle

import pytest, math
from circle import *

def test_init():
    # Test that initializer works
    c = Circle(4)
    # Test that initializer fails without radius
    with pytest.raises(TypeError):
        c = Circle()

def test_radius():
    # Initialize with value
    c = Circle(2)
    # Test that radius can be get and set
    assert c.radius == 2
    c.radius = 4
    assert c.radius == 4

def test_diameter():
    # Initialize with value
    c = Circle(3)
    # Test that diameter is computed properly
    assert c.diameter == 6
    # Test that changing diameter also changes radius
    c.diameter = 10
    assert c.radius == 5

def test_area():
    # Initialize with simple radius
    c = Circle(2)
    assert c.area == 4 * math.pi
    # Test that area cannot be set
    with pytest.raises(AttributeError):
        c.area = 5

def test_diameter_init():
    # Initialize with diameter
    c = Circle.from_diameter(8)
    # Make sure radius and diameter are computed properly
    assert c.radius == 4
    assert c.diameter == 8

def test_repr():
    # Test that repr properly creates a circle object
    c = Circle(4)
    d = eval(repr(c))
    assert d.radius == 4

def test_add():
    # Test that two circles can be added together
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 5
    # Test that a constant can be added to a circle
    c4 = c1 + 2
    assert c4.radius == 4
    # Test that addition works both ways
    c5 = 4 + c1
    assert c5.radius == 6
    # Test that adding another type fails
    with pytest.raises(TypeError):
        assert c1 + '5'

def test_mul():
    # Test that two circles can be added together
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 * c2
    assert c3.radius == 6
    # Test that a constant can be added to a circle
    c4 = c1 * 2
    assert c4.radius == 4
    # Test that multiplication works both ways
    c5 = 4 * c1
    assert c5.radius == 8
    # Test that multiplying by another type fails
    with pytest.raises(TypeError):
        assert c1 * '5'
