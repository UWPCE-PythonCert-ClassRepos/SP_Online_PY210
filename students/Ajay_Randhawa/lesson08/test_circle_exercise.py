

import io
import pytest

from circle_exercise import *


def test_1():
    c = Circle(4)
    assert c.radius == 4

def test_2():
    c = Circle(5)
    assert c.diameter == 10


def test_3():
    c = Circle(6)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_4():
    c = Circle(4)
    assert c.diameter == 8
    assert c.area == 50.27
    with pytest.raises(AttributeError):
        c.area = 5

def test_5():
    c = Circle.from_diameter(10)
    assert c.diameter == 10
    assert c.radius == 5
    
def test_6():
    c = Circle(4)
    print(c)
    print("repr: ",repr(c))
    d = eval(repr(c))
    print("d = ", d)
    


def test_7():
    c1 = Circle(2)
    c2 = Circle(4)
    total = c1 + c2
    print(c1 + c2)
    assert repr(total) == 'Circle(6)'

def test_8():
    c1 = Circle(2)
    c2 = Circle(4)

    total = c1 * 5
    assert repr(total) == 'Circle(10)'


def test_9():
    c1 = Circle(2)
    c2 = Circle(4)
    value = c1 > c2
    assert value is False
    assert (c1 < c2) is True
    assert (c1 == c2) is False

    c3 = Circle(4)

    assert (c2 == c3) is True

def test_10():
    circles = [Circle(1), Circle(0), Circle(3), Circle(2), Circle(4), Circle(5)]
    print(circles)

    circles.sort()
    print(circles)
    assert circles[0] == Circle(0)
    assert circles[3] == Circle(3)
    
def test_11():
    s = Sphere.from_diameter(10)
    assert s.diameter == 10
    assert s.radius == 5
    
    s = Sphere(5)
    assert s.volume == 523.6