# Author: Brian Minsk

from circle import Circle
from math import pi

def test_create_circle():
    """ Test basic circle initiation.
    """
    my_circle = Circle(5)

    assert my_circle.radius == 5
    assert my_circle.diameter == 10

    try:
        your_circle = Circle(-0.5)
    except ValueError:
        pass
    else:
        assert False
        
    try:
        another_circle = Circle("5")
    except ValueError:
        pass
    else:
        assert False

def test_diameter_setter():
    """ Test setting the diameter property. Radius will also get set to half
    the radius value.
    """
    my_circle = Circle(5)

    my_circle.diameter = 8

    assert my_circle.radius == 4
    assert my_circle.diameter == 8

    try:
        my_circle.diameter = -8
    except ValueError:
        pass
    else:
        assert False
        
    try:
        my_circle.diameter = "8"
    except ValueError:
        pass
    else:
        assert False

def test_area():
    my_circle = Circle(5)

    assert my_circle.area == (pi * 5 ** 2)

    # Area should not be able to be set
    try:
        my_circle.area = 10
    except AttributeError:
        pass
    else:
        assert False

def test_constructor_from_diameter():
    my_circle = Circle.from_diameter(10)

    assert my_circle.diameter == 10
    assert my_circle.radius == 5
    assert my_circle.area == (pi * 5 ** 2)

    try:
        your_circle = Circle.from_diameter(-0.5)
    except ValueError:
        pass
    else:
        assert False
        
    try:
        another_circle = Circle.from_diameter("5")
    except ValueError:
        pass
    else:
        assert False