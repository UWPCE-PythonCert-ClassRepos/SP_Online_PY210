from Circle_class_exercise import Circle


def test_radius():
    c = Circle(4)
    print(c.radius)
    assert c.radius == 4


def test_diameter():
    c = Circle(4)
    print(c.diameter)
    assert c.diameter == 8


def test_setter_diameter():
    c = Circle(4)
    c.diameter = 2
    print(c.diameter, "and", c.radius)
    assert c.radius == 1


def test_area():
    c = Circle(2)
    print(c.area)
    assert round(c.area,5) == 12.566370


def test_area_Setter():
    c = Circle(2)
    try:
        c.area = 42
    except AttributeError:
        assert True


def test_from_diameter():
    c = Circle.from_diameter(8)
    print(c.radius)
    assert c.radius == 4
    assert c.diameter == 8


def test_str():
    c = Circle(4)
    print(c)
    print(type(print(c)))
    assert print(c) == "Circle with radius: 4.0"


def test_repr():
    c = Circle(4)
    d = eval(repr(c))
    assert repr(c) == 'Circle(4)'
    assert d == Circle(4)