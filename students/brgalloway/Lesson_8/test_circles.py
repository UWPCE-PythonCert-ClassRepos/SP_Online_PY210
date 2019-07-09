import pytest
import random
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

def test_addition():
    c1 = Circle(4)
    c2 = Circle(2)
    _sum = c1 + c2
    assert print(c1 + c2) == print(Circle(6))

def test_sort():
    circle_list = [Circle(i) for i in range(10)]
    random.shuffle(circle_list)
    circle_list.sort()
    assert circle_list[:3] == [Circle(0), Circle(1), Circle(2)]

def test_volume():
    s1 = Sphere(4)
    with pytest.raises(NotImplementedError):
        s1.area
    assert s1.volume == 268.082573106329
    