"""
Programming In Python - Lesson 8 Assignment 1: Circles
Code Poet: Anthony McKeever
Start Date: 09/05/2019
End Date: 09/05/2019
"""

from circle import Circle

def test_make_circle():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5


def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172


def test_from_diameter():
    c = Circle.from_diameter(20)
    assert c.diameter == 20
    assert c.radius == 10


def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4"

    
def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"
    
    c2 = eval(repr(c))
    assert c2.radius == 4


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3.radius == 6

    c1 += c2
    assert c1.radius == 6


def test_multiply():
    c1 = Circle(2)
    c2 = c1 * 2
    assert c2.radius == 4    

    c1 *= 2
    assert c1.radius == 4    


def test_reverse_multiply():
    c1 = Circle(2)
    c2 = 2 * c1
    assert c2.radius == 4


def test_equality():
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1 == c2
    
    c2 = Circle(4)
    assert c1 != c2
    assert c1 < c2
    assert c2 > c1


def test_reflected_numerics():
    c1 = Circle(2)
    assert c1 * 3 == 3 * c1

    c2 = Circle(4)
    assert c1 + c2 == c2 + c1


def test_subtract():
    c1 = Circle(4)
    c2 = c1 - 1

    assert c2.radius == 3

    c1 -= 7
    assert c1.radius == -3


def test_divide():
    c1 = Circle(4)
    c2 = Circle(2)
    c3 = c1 / c2

    assert c3.radius == 2

    c3 = c1 // c2
    assert c3.radius == 2
