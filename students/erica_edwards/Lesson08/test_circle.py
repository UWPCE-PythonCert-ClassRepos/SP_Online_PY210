
from circle import Circle, Sphere
from pytest import approx


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_get_diameter():
    c = Circle(4)
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(8)
    c.diameter = 4
    assert c.radius == 2


def test_get_area():
    c = Circle(4)
    print(c.area)
    assert c.area == approx(50.27, rel=1e-3)


def test_from_diameter():
    c = Circle.from_diameter(4)
    assert c.radius == 2


def test_repr():
    c = Circle(4)
    d = eval(repr(c))
    assert d.radius == 4


def test_str():
    c = Circle(4)
    print(c)
    assert str(c).startswith('Circle with')
    assert str(c).strip().endswith('4.0')


def test_add():
    c1 = Circle(4)
    c2 = Circle(3)
    c3 = c1 + c2
    assert c3.radius == 7


def test_iadd():
    circle_a = Circle(2)
    circle_b = Circle(3)
    circle_a += circle_b    # same as circle_a = circle_a + circle_b
    assert circle_a.radius == 5


def test_multiply():
    c1 = Circle(4)
    c2 = Circle(3)
    c3 = c1 * c2
    assert c3.radius == 12


def test_comparisons():
    c = Circle(4)
    c1 = Circle(3)
    assert c > c1
    assert c1 < c
    assert c1 != c
    assert c == Circle(4)


def test_sort():
    the_list = [Circle(5), Circle(9), Circle(1)]
    the_list.sort(key=Circle.sort_key)
    assert the_list == [Circle(1), Circle(5), Circle(9)]


def test_sphere_radius():
    c = Sphere(4)
    d = eval(repr(c))
    assert d.radius == 4


def test_volume():
    c = Sphere(5)
    assert c.volume == approx(523.6, rel=1e-2)


def test_sphere_from_diameter():
    c = Sphere.from_diameter(5)
    assert isinstance(c, Sphere)
    assert c.radius == approx(2.5, rel=1e-2)


def test_sphere_area():
    c = Sphere(4)
    assert c.area == approx(201.06, rel=1e-2)


def test_sphere_repr():
    c = Sphere(4)
    d = eval(repr(c))
    assert d.radius == 4


def test_sphere_str():
    c = Sphere(4)
    print(c)
    assert str(c).startswith('Sphere with')
    assert str(c).strip().endswith('4.0')


def test_sphere_add():
    s1 = Sphere(4)
    s2 = Sphere(3)
    s3 = s1 + s2
    assert isinstance(s3, Sphere)
    assert s3.radius == 7


def test_Sphere_multiply():
    s1 = Sphere(4)
    s2 = Sphere(3)
    s3 = s1 * s2
    assert isinstance(s3, Sphere)
    assert s3.radius == 12


def test_sphere_comparisons():
    c = Sphere(4)
    c1 = Sphere(3)
    assert c > c1
    assert c1 < c
    assert c1 != c
    assert c == Sphere(4)


def test_sphere_sort():
    the_list = [Sphere(5), Sphere(9), Sphere(1)]
    the_list.sort(key=Sphere.sort_key)
    assert the_list == [Sphere(1), Sphere(5), Sphere(9)]
