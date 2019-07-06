"""
Test code for circle.py
"""

import pytest
import math

from circle import *

########
# Step 1
########
"""
Create a circle class that has c = Circle(5) as the signature
Ensure radius is a required attribute
"""


def test_init():
    """
    Test that we pass the
    """
    # check for missing radius intput
    with pytest.raises(TypeError):
        c = Circle()

    c = Circle(5)
    assert c.radius == 5


########
# Step 2
########
"""
Add a diameter property so the user can get the diameter of the circle
"""


def test_diameter():
    """Test that diameter attribute exists and twice the radius"""
    c = Circle(5)

    assert c.diameter == 10


########
# Step 3
########
"""
Allow the user to set the diameter of the circle.
Ensure that the radius and diameter are always in sync.
Make the diameter and radius both properties.
"""


def test_diameter_radius_property():
    c = Circle(5)

    assert c.radius == 5
    assert c.diameter == 10

    # check that diameter change works and updates radius
    c.diameter = 20

    assert c.diameter == 20
    assert c.radius == 10

    # check that radius change works and updates diameter
    c.radius = 25

    assert c.radius == 25
    assert c.diameter == 50


########
# Step 4
########
"""
Add an area property so the user can get the property of the circle.

Make sure they user can't set the area.
"""


def test_area():

    c = Circle(5)

    # test area gets calculated properly
    assert c.area == 5*5*math.pi

    # test user can't set area property
    with pytest.raises(AttributeError):
        c.area = 12

    # ensure area gets updated with radius and diameter updates
    c.diameter = 20
    assert c.radius == 10
    assert c.area == 100*math.pi

    c.radius = 20
    assert c.diameter == 40
    assert c.area == 20*20*math.pi


########
# Step 5
########
"""
Created an alternate initializer so the user can initialize from a diameter.
"""


def test_initialize_diameter():
    c = Circle.from_diameter(10)

    # test radius, area, diameter properties
    assert c.diameter == 10
    assert c.radius == 5
    assert c.area == 25*math.pi

    # test chaning radius updates diameter and area
    c.radius = 10
    assert c.diameter == 20
    assert c.area == 100*math.pi

    # test initializer fails on empty diameter
    with pytest.raises(TypeError):
        c = Circle.from_diameter()


########
# Step 6
########
"""
Create a __str___ method to create the informal string representation of circles
Create a __repr__ method to create the formal string representation of circle

print(c) == "Circle with radius: 4.000000"

repr(c) == "Circle(5)"
"""


def test__str__method():
    c = Circle(5)

    print(c)
    d = c.__str__()
    assert d == "Circle with radius: 5.000000"


def test__repr_method():
    c = Circle(5)

    repr(c)
    d = c.__repr__()
    assert d == "Circle(5)"


########
# Step 7
########
"""
Add numerical protocol to add and multiply circles
"""


def test_add_function():
    c = Circle(5)
    c2 = Circle(5)

    # test operator works
    c3 = c + c2

    # test all properties correctly initialized
    assert c3.radius == 10
    assert c3.diameter == 20
    assert c3.area == 100*math.pi


def test_multiplication_function():
    c = Circle(5)

    # test operator works
    c2 = c * 5

    # test all properties correctly initialized
    assert c2.radius == 25
    assert c2.diameter == 50
    assert c2.area == 25*25*math.pi

    # test reverse order multiplication
    c3 = 5 * c

    # test all properties correctly initialized
    assert c3.radius == 25
    assert c3.diameter == 50
    assert c3.area == 25*25*math.pi


########
# Step 8
########
"""
Add numerical protocol to compare circles
__lt__ = less than
__eq__ = equal

Implementing those two will allow python to fill in the following
__le__
__gt__
__ge__
"""


def test_less_than_equal():
    c = Circle(5)
    c2 = Circle(10)
    c3 = Circle(5)

    assert (c < c2)
    assert not (c2 < c3)
    assert not (c < c3)


def test_euqal():
    c = Circle(5)
    c2 = Circle(5)
    c3 = Circle(1)

    assert (c == c2)
    assert not (c == c3)

def test_filled_in_operators():
    c = Circle(5)
    c2 = Circle(10)
    c3 = Circle(5)

    # test less than or equal too
    assert (c <= c2)
    assert (c <= c3)
    assert not (c2 <= c3)

    # test greater than
    assert (c2 > c3)
    assert not (c > c2)
    assert not (c > c3)

    # test greater than or equal too
    assert (c2 >= c3)
    assert (c >= c3)
    assert not (c >= c2)


def test_sorting():
    circles = [Circle(5), Circle(2), Circle(12), Circle(2), Circle(7), Circle(56)]
    print(circles)

    circles.sort()
    print(circles)

    # test list got sorted properly
    assert circles == [Circle(2), Circle(2), Circle(5), Circle(7), Circle(12), Circle(56)]


########
# Step 8: Optional
########
"""
Make reflected numerics do the right thing.
Add augmented assignment operators where they make sense.
"""


########
# Step 9
########
"""
Subclass a sphere from the circle class.
- Overwrite the __str__ and __repr__ methods.
- Add a volume property.
- Override the area property to show the area of a sphere.
- Ensure numerics work properly.
- Ensure you can instantiate a sphere with the _from_diameter() initializer
"""


def test_initialize_sphere():
    """
    Test we can initialize a sphere and compute basic properties.
    """
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10


def test_sphere__str__method():
    s = Sphere(5)

    print(s)
    d = s.__str__()

    assert d == "Sphere with radius: 5.000000"


def test_sphere__repr__method():
    s = Sphere(5)

    repr(s)
    d = eval(repr(s))

    assert d == "Sphere(5)"


def test_volume_property():
    s = Sphere(5)

    assert s.volume == 4/3*math.pi*math.pow(s.radius, 3)


def test_sphere_area_property():
    s = Sphere(5)

    assert s.area == 4*math.pi*math.pow(s.radius, 2)


def test_sphere_numerics():
    s = Sphere(5)
    s2 = Sphere(2)


    # check addition works
    s3 = s + s2
    print(s3)
    assert s3.radius == 7
    assert s3.diameter == 14

    # check multiplication works
    s4 = s*2
    print(s4)
    assert s4.radius == 10
    assert s4.diameter == 20

    s5 = 2*s
    print(s5)
    assert s5.radius == 10
    assert s5.diameter == 20


def test_total_ordering():
    s = Sphere(5)
    s2 = Sphere(10)
    s3 = Sphere(5)

    # check less than and equal to
    assert s < s2
    assert not s3 < s

    assert s == s3
    assert not s == s2

    # check total ordering
    assert s <= s3
    assert s3 >= s
    assert s2 > s3


def test_sorting():
    s = Sphere(5)
    s2 = Sphere(7)
    s3 = Sphere(10)
    s4 = Sphere(12)
    s5 = Sphere(25)
    s6 = Sphere(30)

    spheres = [s2, s, s5, s4, s6, s3]
    print(spheres)

    spheres.sort()
    print(spheres)

    assert spheres == [s, s2, s3, s4, s5, s6]


def test_from_diameter():
    s = Sphere.from_diameter(10)

    assert s.radius == 5
    assert s.diameter == 10
