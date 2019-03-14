"""
test code for circle.py
"""

import pytest

from circle import *

########
# Step 1
########

def test_init():
    c = Circle(4)
    assert c.radius == 4
    

########
# Step 2
########

def test_get_diameter():
    c = Circle(4)
    assert c.diameter == 8
    

########
# Step 3
########

def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1
    
    
########
# Step 4
########

def test_area():
    c = Circle(2)
    assert c.area == pytest.approx(12.566370)
    
    
########
# Step 5
########

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4
    

########
# Step 6
########

def test_str():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'
    
def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    
    
########
# Step 7
########

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(6)'
    
def test_mul():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c2 * 3) == 'Circle(12)'
    assert repr(3 * c2) == 'Circle(12)'
    assert repr(c1 * 10) == 'Circle(20)'


########
# Step 8
########

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c2 > c1
    assert c1 < c2
    assert c2 == c3
    
def test_list():
    circles = [Circle(3), Circle(1), Circle(4), Circle(15), Circle(7)]
    circles.sort()
    assert circles == [Circle(1), Circle(3), Circle(4), Circle(7), Circle(15)]
    
    
########
# Step 8 - Optional
########

def test_reflected():
    c1 = Circle(2)
    assert c1 * 3 == 3 * c1
    
def test_division():
    c2 = Circle(4)
    assert c2 // 2 == Circle(2)
    
def test_iadd():
    c1 = Circle(2)
    c2 = Circle(4)
    c1 += c2
    assert c1 == Circle(6)
    
def test_imul():
    c1 = Circle(2)
    c1 *= 4
    assert c1 == Circle(8)