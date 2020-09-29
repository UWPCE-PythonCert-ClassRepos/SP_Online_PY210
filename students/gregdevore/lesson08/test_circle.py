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
    assert isinstance(c,Circle)

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

def test_comp():
    # Test that circles compare correctly
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(1)
    assert c1 < c2
    assert not c1 > c2
    assert c2 > c1
    assert c1 == c3
    assert c1 != c2

def test_sort():
    # Test that circles can be sorted
    circles = [Circle(6), Circle(2), Circle(4), Circle(1)]
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(4), Circle(6)]

def test_augmented_assignment():
    # Test that augmented assignment works
    c = Circle(2)
    # Add
    c += 4
    assert c.radius == 6
    # Multiply
    c *= 2
    assert c.radius == 12
    # Divide
    c /= 3
    assert c.radius == 4
    # Raise to power
    c **= 2
    assert c.radius == 16
    # Subtract
    c -= 6
    assert c.radius == 10

def test_truediv():
    # Test that two circles can be added together
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 / c2
    assert c3.radius == 0.5
    # Test that a constant can be divided into a circle
    c4 = c1 / 2
    assert c4.radius == 1
    # Division should NOT work both ways
    with pytest.raises(TypeError):
        c5 = 4 / c1
    # Test that dividing by another type fails
    with pytest.raises(TypeError):
        assert c1 / '5'

def test_sub():
    # Test that two circles can be subtracted together
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = c2 - c1
    assert c3.radius == 3
    # Test that a constant can be subtracted from a circle
    c4 = c2 - 1
    assert c4.radius == 4
    # Subtraction should NOT work both ways
    with pytest.raises(TypeError):
        c5 = 5 - c1
    # Test that creating a circle with a negative radius fails
    with pytest.raises(ValueError):
        assert c1 - c2
    # Test that subtracting another type fails
    with pytest.raises(TypeError):
        assert c1 + '5'

def test_pow():
    # Test that a circle can be raised to a power
    c1 = Circle(4)
    c2 = c1 ** 2
    assert c2.radius == 16
    # Test that other power operations fail
    with pytest.raises(TypeError):
        assert 2 ** c1
    with pytest.raises(TypeError):
        assert c1 ** c2
