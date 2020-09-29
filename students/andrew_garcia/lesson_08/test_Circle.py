'''
Andrew Garcia
Circle Test
8/19/19
'''

import pytest
from Circle import *



def test_init():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(2)
    assert c.diameter == 4


def test_set_diameter():
    c = Circle(8)
    c.diameter = 4
    assert c.diameter == 4
    assert c.radius == 2


def test_area():
    c = Circle(2)
    assert c.area == 12.566

def test_from_diameter():
    c = Circle(4)

    c.diameter = 8
    assert c.diameter == 8
    assert c.radius == 4


def test_str():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4'

def test_repr():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6
    assert c3.diameter == 12
    assert repr(c3) == 'Circle(6)'
    assert str(c3) == 'Circle with radius: 6'


def test_mul():
    c1 = Circle(3)
    c2 = c1 * 3
    assert c2.radius == 9
    assert repr(c2) == 'Circle(9)'
    assert str(c2) == 'Circle with radius: 9'


def test_lt():
    c1 = Circle(2)
    c2 = Circle(5)
    assert c1 < c2


def test_gt():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1 > c2


def test_eq():
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2

def sort_circles():
    circles = [Circle(100), Circle(58), Circle(8), Circle(6), Circle(68), Circle(5)]
    assert circles.sort() == [Circle(5), Circle(6), Circle(8), Circle(58), Circle(68), Circle(100)]



def test_str_sphere():
    s = Sphere(4)
    assert str(s) == 'Sphere with radius: 4'

def test_repr_sphere():
    s = Sphere(4)
    assert repr(s) == 'Sphere(4)'

def test_area_sphere():
    s = Sphere(4)
    with pytest.raises(NotImplementedError):
        assert s.area == 5

def test_volume():
    s = Sphere(5)
    assert s.volume == 523.599
