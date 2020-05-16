import math
from circle import Circle, Sphere


def test_radius():
	c = Circle(4)
	assert c.radius == 4


def test_diameter():
	c = Circle(5)
	assert c.diameter == 10


def test_setdiameter():
	c = Circle(6)
	c.diameter = 3
	assert c.diameter == 3
	assert c.radius == 1.5


def test_area():
	c = Circle(3)
	assert c.area == 28.274333882308138


def test__repr__():
	c = Circle(4)
	assert repr(c) == 'Circle(4)'


def test__str__():
	c = Circle(4)
	assert str(c) == 'Circle with radius: 4'
	assert eval(repr(c)) == Sphere(4)


def test_from_diameter():
	c = Circle.from_diameter(8)
	assert c.diameter == 8
	assert c.radius == 4


def test_compare_circles():
	c1 = Circle(4)
	c2 = Circle(8)
	c3 = Circle(8)
	assert (c1 > c2) is False
	assert (c1 < c2) is True
	assert (c1 == c2) is False
	assert (c2 == c3) is True
	circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
	circles.sort()
	assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]


def test_circle_numeric_protocol():
	c1 = Circle(4)
	c2 = Circle(8)
	assert c1 + c2 == Circle(12)
	assert c1 * 2 == Circle(8)


def test_reflected():
	c1 = Circle(4)
	assert c1 * 3 == 3 * c1


def test_sphere__repr__():
	s = Sphere(4)
	assert repr(s) == 'Sphere(4)'


def test_sphere__str__():
	s = Sphere(4)
	assert str(s) == 'Sphere with radius: 4'
	assert eval(repr(s)) == Sphere(4)


def test_sphere_volume():
	s = Sphere(4)
	assert s.volume == (4 / 3 * math.pi * 4 ** 3)


def test_sphere_from_diameter():
	s = Sphere.from_diameter(4)
	assert s.diameter == 4
	assert s.radius == 2


def test_sphere_area():
	s = Sphere(4)
	assert s.area == (4 * math.pi * (4 ** 2))
