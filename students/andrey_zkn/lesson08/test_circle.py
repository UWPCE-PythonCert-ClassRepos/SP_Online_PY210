
from circle import *
import pytest


def test_init():
    c = Circle(4)
    assert c.radius == 4
	

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2
	

def test_area():
    c = Circle(2)
    assert round(c.area, 5) == 12.56637
    with pytest.raises(AttributeError):
        c.area = 42
		

def test_from_diameter():   
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8
    assert round(c.area, 5) == 50.26548
	

def test_str():
    c = Circle(3)
    assert str(c) == "Circle with radius: 3.000000"
    print(c)


def test_repr():
    c = Circle(3)
    assert repr(c) == "Circle(3)"
    print(repr(c))


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert repr(c3) == "Circle(6)"


def test_mul():
    c1 = Circle(3)
    c2 = c1 * 3
    assert repr(c2) == "Circle(9)"
    c3 = 3 * c1
    assert repr(c3) == "Circle(9)"
	
	

def test_compare():
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle.from_diameter(12)
    c4 = Circle(2)
    assert c1 < c2 
    assert c2 > c1 
    assert c2 == c3 
    assert c1 != c2
    circles = [c1, c2, c4]
    circles.sort()
    assert circles == [Circle(2), Circle(5), Circle(6)]	
	
	
def test_div():
    c1 = Circle(6)
    c2 = c1 / 2
    assert repr(c2) == "Circle(3.0)" 
    c3 = 12 / c1
    assert repr(c3) == "Circle(2.0)"
    c4 = c1 // 2
    assert repr(c4) == "Circle(3)"
    c5 = 12 // c1
    assert repr(c5) == "Circle(2)"


def test_augmentation():   
    c1 = Circle(3)
    c2 = Circle(5)
    c2 += c1
    assert repr(c2) == "Circle(8)"
    c1 *= 2
    assert repr(c1) == "Circle(6)"



def test_sphere():
    #Test sphere
    
    c = Sphere(2)
    assert c.radius == 2
    assert c.diameter == 4
    assert round(c.volume, 2) == 33.51
    assert round(c.area, 2) == 50.27
    assert str(c) == "Sphere with radius: 2.000000"
    assert repr(c) == "Sphere(2)"
    c2 = Sphere.from_diameter(10)
    assert c2.radius == 5
    c3 = Sphere(6)
    assert repr(c + c3) == "Sphere(8)"
    assert repr(c * 2) == "Sphere(4)"
    c4 = Sphere(2)

    assert c < c3
    assert not (c > c3)
    assert c3 > c
    assert not (c3 < c)
    assert c == c4
    assert not (c == c2)
    assert c != c2
    assert not c != c4
    circles = [c3, c, c2]
    circles.sort()
    assert circles == [Sphere(2), Sphere(5), Sphere(6)]
