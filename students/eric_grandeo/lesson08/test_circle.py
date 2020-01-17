#test cases

import pytest

from circle import *

def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_circle_diameter_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

