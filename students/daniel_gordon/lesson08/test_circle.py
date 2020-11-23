import pytest
import random

from math import pi
from circle import *

def test_init():
    c = Circle(5)
    assert c.radius == 5
    with pytest.raises(ValueError):
        Circle(-3)

def test_diameter():
    c = Circle(7)
    assert c.diameter == 14
    c.diameter = 8
    assert c.radius == 4
    c = Circle.from_diameter(5)
    c.radius = 2.5

def test_area():
    c = Circle(5)
    assert c.area == 25*pi
    with pytest.raises(AttributeError):
        c.area = 30

def test_print():
    c = Circle(4)
    assert str(c) == "A Circle of radius 4"
    assert repr(c) == "Circle(4)"
    
def test_add():
    c = Circle(3) + Circle(2)
    assert c.radius == 5
    c += Circle(5)
    assert c.radius == 10

def test_sub():
    c = Circle(7) - Circle(3)
    assert c == Circle(4)
    c -= Circle(1)
    assert c == Circle(3)
    with pytest.raises(ValueError):
        c -= c    

def test_mul():
    c = Circle(1) * 4
    assert c.radius == 4
    c *= 3
    assert c.radius == 12
    c = 1.5 * c
    assert c.radius == 18

def test_div():
    c = Circle(15) / 3
    assert c == Circle(5)
    c /= 2
    assert c == Circle(2.5)

def test_comparisons():
    c1 = Circle(2)
    c2 = Circle(5)
    assert (c1 < c2) == True
    assert (c1 > c2) == False
    assert (c1 == c2) == False
    assert (c2 <= c1) == False
    assert (c2 >= c1) == True
    
    c1 = Circle(3.5)
    c2 = Circle(3.5)
    assert (c1 == c2) == True
    assert (c1 <= c2) == True
    assert (c1 >= c2) == True
    assert (c1 < c2) == False
    assert (c1 > c2) == False

def test_sort():
    nums = [num for num in range(1,15)]
    order = [Circle(r) for r in nums]
    random.shuffle(nums)
    circles = [Circle(r) for r in nums] 
    circles.sort()
    assert circles == order

def test_sphere():
    s = Sphere(6)
    assert str(s) == "A Sphere of radius 6"
    assert repr(s) == "Sphere(6)"
    test_vol = pi*4/3*6**3
    assert s.volume == test_vol
    assert s.area == 144*pi