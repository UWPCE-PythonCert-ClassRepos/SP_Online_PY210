"""
Christine Kim
Lesson 8
Assignment Circle Test
"""

from circle import Circle

#test define circle radius
def test_radius():
    c = Circle(4)
    assert c.radius == 4

#test define cicle diameter
def test_diameter():
    c = Circle(2)
    print("Type: ", type(c.radius))
    print("diameter: ", c.diameter)
    assert c.diameter == 4
    assert c.radius == 2

#test compute circle area
def test_area():
    c = Circle(10)
    assert c.area == 314.1592653589793

#test set diameter
def test_set_diameter():
    c = Circle(6)
    c.diameter = 8

    assert c.diameter == 8
    assert c.radius == 4

def test_from_diameter():
    c = Circle.from_diameter(10)
    assert c.diameter == 10
    assert c.radius == 5

#test print circle
def test_str():
    c = Circle(5)
    assert str(c) == "Circle with radius: 5"

def test_repr():
    c = Circle(6)
    assert repr(c) == "Circle(6)"

#test add circles
def test_add():
    c1 = Circle(24)
    c2 = Circle(12)
    c3 = c1 + c2
    assert c3.radius == 36
    
    c1 += c2
    assert c1.radius == 36

def test_multiply():
    c2 = Circle(12)
    assert c2.radius * 3 == 36
    assert 3 * c2.radius == 36

#test compare circle sizes
def test_compare():
    c1 = Circle(10)
    c2 = Circle(10)
    c3 = Circle(20)

    assert c1 == c2
    assert c1 != c3

    assert c1 < c3
    assert c1 <= c3
    assert c3 > c2
    assert c3 >= c2

#test circle sort and list
def test_sort():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(4)
    c5 = Circle(5)

    unsorted = [c3, c5, c1, c4, c2]
    sorted_cirlcles = sorted(unsorted)

    assert sorted_cirlcles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5)]

#test reflected numerics
def test_r():
    c1 = Circle(3)
    assert c1 * 3 == 3 * c1

    c2 = Circle(4)
    assert c1 + c2 == c2 + c1

#test division
def test_div():
    c1 = Circle(6)
    c2 = Circle(3)
    c3 = c1 / c2

    assert c3.radius == 2