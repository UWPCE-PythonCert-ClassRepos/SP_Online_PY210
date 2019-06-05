#test_circle

import pytest

from circle import *

#test 1
def test_init():
    t = Circle(3)
    assert t.rad == 3

#test 2
def test_dia():
    t = Circle(3)
    assert t.diameter == 6
    
#test 3
def test_dia_set():
    t = Circle(3)
    t.diameter = 3
    assert t.diameter == 3
    assert t.rad == 1.5
    
#test 4
def test_area():
    t = Circle(3)
    assert round(t.area,4) == 28.2743

#test 5
def test_from_dia():
    t = Circle.from_diameter(3)
    assert t.diameter == 3
    assert t.rad == 1.5
    
#test 6
def test_string():
    t = Circle(3)
    assert str(t) == 'Circle with radius 3.0000'
    
def test_repr():
    t = Circle(3)
    assert repr(t) == 'Circle(3)'
    
#test 7
def test_add():
    t1 = Circle(3)
    t2 = Circle(4)
    assert repr(t1+t2) == 'Circle(7)'
    
def test_mult():
    t1 = Circle(3)
    assert repr(t1*4) == 'Circle(12)'
    
#test 8
def test_lt_gt_eq():
    t1 = Circle(3)
    t2 = Circle(2)
    t3 = Circle(3)
    assert t1 > t2
    assert not t1 < t2
    assert t1 == t3
    assert t1 != t2
    
def test_sort():
    circle_list = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circle_list.sort()
    assert circle_list == [Circle(0),Circle(1),Circle(2),Circle(3),Circle(4),Circle(5),Circle(6),Circle(7),Circle(8),Circle(9)]
    
#test 9
def test_sphere():
    t = Sphere(3)
    assert str(t) == 'Sphere with radius 3.0000'
    assert repr(t) == 'Sphere(3)'
    assert round(t.vol,4) == 113.0973
    assert round(t.area,4) == 113.0973
    
    t1 = Sphere.from_diameter(3)
    assert t1.diameter == 3
    assert t1.rad == 1.5