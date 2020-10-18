"""
test code for circle_class.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle_class import *

########
# Step 1
########

def test_circle():
    with pytest.raises(AttributeError):
        c = Circle()

def test_radius():
    c = Circle(4)

    assert c.radius == 4

########
# Step 2
########

def test_diameter():
    c = Circle(4)

    assert c.diameter == 8

########
# Step 3
########

def test_dia_rad():
    c = Circle(8)

    assert c.radius == 8
    assert c.diameter == 16

    c.diameter = 8

    assert c.radius == 4
    assert c.diameter == 8