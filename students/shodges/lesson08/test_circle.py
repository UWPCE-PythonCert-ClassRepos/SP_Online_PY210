#!/usr/bin/env python3

import pytest
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
