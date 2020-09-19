from circle import Circle, Sphere, Cylinder
import math

c = Circle(5)
c1 = Circle(10)
s = Sphere(5)
s1 = Sphere(10)


def test_1():
    assert c.radius is 5


def test_2():
    assert c.diameter() is 10


def test_3():
    assert c.diameter() > c.radius


def test_4():
    assert c.radius <= c.diameter() <= c.area()
