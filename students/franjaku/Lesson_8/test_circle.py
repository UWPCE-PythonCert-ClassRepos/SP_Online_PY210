"""
Test code for circle.py
"""

import pytest
import math

from circle import *

########
# Step 1
########
"""
Create a circle class that has c = Circle(5) as the signature
Ensure radius is a required attribute
"""


def test_init():
    """
    Test that we pass the
    """
    # check for missing radius intput
    with pytest.raises(TypeError):
        c = Circle()

    c = Circle(5)
    assert c.radius == 5


########
# Step 2
########
"""
Add a diameter property so the user can get the diameter of the circle
"""


def test_diameter():
    """Test that diameter attribute exists and twice the radius"""
    c = Circle(5)

    assert c.diameter == 10


########
# Step 3
########
"""
Allow the user to set the diameter of the circle.
Ensure that the radius and diameter are always in sync.
Make the diameter and radius both properties.
"""


def test_diameter_radius_property():
    c = Circle(5)

    assert c.radius == 5
    assert c.diameter == 10

    # check that diameter change works and updates radius
    c.diameter = 20

    assert c.diameter == 20
    assert c.radius == 10

    # check that radius change works and updates diameter
    c.radius = 25

    assert c.radius == 25
    assert c.diameter == 50


########
# Step 4
########
"""
Add an area property so the user can get the property of the circle.

Make sure they user can't set the area.
"""


def test_area():

    c = Circle(5)

    # test area gets calculated properly
    assert c.area == 5*5*math.pi

    # test user can't set area property
    with pytest.raises(AttributeError):
        c.area = 12

    # ensure area gets updated with radius and diameter updates
    c.diameter = 20
    assert c.radius == 10
    assert c.area == 100*math.pi

    c.radius = 20
    assert c.diameter == 40
    assert c.area == 20*20*math.pi
