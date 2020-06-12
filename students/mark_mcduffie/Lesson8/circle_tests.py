# Mark McDuffie
# Circle testing units
from circle import *

RADIUS = 4
DIAMETER = 8

# Step 1
def test_init():
    c = Circle(RADIUS)
    assert c.radius == RADIUS


# step 2
def test_diameter():
    d = Circle(RADIUS)
    assert d.diameter == RADIUS * 2

# step 3
def test_diameter_set():
    c = Circle(DIAMETER)
    c.diameter = DIAMETER
    assert c.radius == DIAMETER/2
    assert c.diameter == DIAMETER

# step 4
def test_area():
    c = Circle(RADIUS/2)
    assert c.area == 12.566371

#step 5
def test_from_diameter():
    c = Circle.from_diameter(DIAMETER)
    assert c.diameter == DIAMETER
    assert c.radius == RADIUS

#step 6
def test_string():
    c = Circle(RADIUS)
    assert str(c) == 'Circle with radius: 4.000000'

def test_repr():
    c = Circle(RADIUS)
    assert repr(c) == 'Circle(4)'

#step 7
def test_add():
    c1 = Circle(4)
    c2 = Circle(8)
    c3 = c1 + c2
    assert str(c3) == 'Circle with radius: 12.000000'
    assert repr(c3) == 'Circle(12)'

def test_mul():
    c1 = Circle(4)
    c2 = c1 * 4
    assert c2.radius == 16
    assert str(c2) == 'Circle with radius: 16.000000'
    assert repr(c2) == 'Circle(16)'

#step 8
def test_comparisons():
    c1 = Circle(4)
    c2 = Circle(4)
    c3 = Circle(8)
    assert not c1 > c3
    assert not c1 == c3
    assert c2 < c3
    assert c3 > c1
    assert c1 == c2

def test_sort():
    circle_list = [Circle(8), Circle(4), Circle(6)]
    circle_list.sort()
    assert circle_list == [Circle(4), Circle(6), Circle(8)]

#step 9
def test_sphere():
    s = Sphere(RADIUS)
    v = s.volume
    a = s.area
    assert s.radius == RADIUS
    assert s.diameter == DIAMETER
    assert round(s.volume, 2) == 268.08
    assert round(s.area, 2) == 201.06

    d = Sphere.from_diameter(DIAMETER)
    assert d.diameter == DIAMETER
    assert d.radius == RADIUS



