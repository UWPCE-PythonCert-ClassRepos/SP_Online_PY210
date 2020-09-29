import pytest
from circle import Circle, Sphere
########
# Step 1
########

def test_radius():
    c = Circle(4)
    assert c.radius == 4
    s = Sphere(4)
    assert s.radius == 4

########
# Step 2
########

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    s = Sphere(4)
    assert s.diameter == 8

########
# Step 3
########

def test_setter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

    s = Sphere(4)
    s.diameter = 2
    assert s.diameter == 2
    assert s.radius == 1


########
# Step 4
########

def test_area():
    c = Circle(2)
    assert c.area == 12.566370614359172
    s = Sphere(2)
    assert s.area == 50.26548245743669
    s = Sphere(4)
    assert round(s.area,5) == 201.06193

    with pytest.raises(AttributeError):
        c.area = 42
        s.area = 42

########
# Step 5
########

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8

    s = Sphere.from_diameter(8)
    assert s.radius == 4
    assert s.diameter == 8

########
# Step 6
########

def test_display():
    c = Circle(4)
    d = eval(repr(c))
    assert str(d) == 'Circle with radius: 4'
    assert str(Circle(4)) == "Circle with radius: 4"
    assert repr(c) == 'Circle(4)'

    s = Sphere(4)
    d = eval(repr(s))
    assert str(d) == 'Sphere with radius: 4'
    assert str(s) == 'Sphere with radius: 4'
    assert repr(s) == 'Sphere(4)'

########
# Step 7
########

def test_math():
    c1 = Circle(2)
    c2 = Circle(4)
    c = c1 + c2
    assert str(c) == "Circle with radius: 6"
    assert repr(c) == 'Circle(6)'
    c3 = c2 * 3
    assert str(c3) == "Circle with radius: 12"
    assert repr(c3) == 'Circle(12)'


    s1 = Sphere(2)
    s2 = Sphere(4)
    s = s1 + s2
    assert str(s) == "Sphere with radius: 6"
    assert repr(s) == 'Sphere(6)'
    s3 = s2 * 3
    assert str(s3) == "Sphere with radius: 12"
    assert repr(s3) == 'Sphere(12)'

########
# Step 8
########

def test_orders():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert c1 < c2
    assert c2 == c3
    assert c2 != c1
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
    assert c1 * 3 == 3 * c1
    c1 *= 20
    assert c1 == 40
    c2 += c3
    assert c2 == Circle(8)

    s1 = Sphere(2)
    s2 = Sphere(4)
    s3 = Sphere(4)
    assert s1 < s2
    assert s2 == s3
    assert s2 != s1

    assert s1 * 3 == 3 * s1
    s1 *= 20
    assert s1 == 40
    s2 += s3
    assert s2 == Sphere(8)


########
# Step 9
########

def test_volume():
    s = Sphere(4)
    assert round(s.volume,5) ==268.08257

s = Sphere(4)
s.diameter = 2
assert s.diameter == 2
assert s.radius == 1
