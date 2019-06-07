import pytest
from circles import *


def test_radius():
    c = Circle(4)
    assert c.radius == 4
    assert c.diameter == 8

# test fails after adding setter
# def test_diameter():
#     c = Circle(2)
#     with pytest.raises(AttributeError):
#         c.diameter = 42

def test_set_diameter():
    c = Circle(2)
    c.diameter = 42
    assert c.diameter == 42
    
def test_area():
    c = Circle(3)
    assert f"{c.area:.2f}" == str(28.27)

def test_print():
    c = Circle(4)
    c1 = Circle(8)
    assert repr(c) == "Circle(4)"
    assert c1.__str__() == "circle with radius 8"

def test_classmethod():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4