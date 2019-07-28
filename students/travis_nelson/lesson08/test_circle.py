"""
test code for circle.py

The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area.
Print the circle and get something nice.
Be able to add two circles together.
Be able to compare two circles to see which is bigger.
Be able to compare to see if they are are equal.
(follows from above) be able to put them in a list and sort them.

"""
import pytest
from circle import *


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    c = Circle(5)
    assert c.radius == 5
