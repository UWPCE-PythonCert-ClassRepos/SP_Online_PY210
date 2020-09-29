import pytest
from circle import *

def test_init():
    c = Circle(2)
    assert c.radius == 2

def test_diameter():
    c = Circle(2)
    assert c.diameter  == 4
    assert c.radius ==  2

def test_area():
    c = Circle(2)
    assert c.area == '12.566371'

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius==4

def test_area():
    c = Circle(3)
    with pytest.raises(AttributeError):
        c.area = 43

def test_str():
    c = Circle(3)
    assert str(c) == 'Circle with radius: 3'

def test_repr():
    c = Circle(3)
    assert repr(c) == 'Circle(3)'

def test_add():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = c1 + c2
    assert c3.radius == 10

def test_mul():
    c1 = Circle(4)
    value = 3
    c2 = c1  * 3
    c3 = 3 * c1
    assert c2.radius == 12
    assert c3.radius == 12

def test_equal():
    c2 = Circle(2)
    c3 = Circle(3)
    c3.radius=2
    assert c2 == c3

def test_not_equal():
    c2=Circle(2)
    c3=Circle(3)
    assert c2 != c3

def test_less():
    c2=Circle(2)
    c3=Circle(3)
    assert c2 < c3
    assert c2 <= c3

def test_sort():
    c1=Circle(1)
    c2=Circle(2)
    c3=Circle(3)
    c4=Circle(4)
    group = [c4, c1, c3, c2]
    group.sort()
    assert group == [c1, c2, c3, c4]

def test_str_Sphere():
    s = Sphere(9)
    assert str(s) == "Sphere with radius:9"
    s = Sphere(4.11)
    assert str(s) == "Sphere with radius:4.11"

def test_repr_Sphere():
    c = Sphere(9)
    assert repr(c) == "Sphere(9)"
    c = Sphere(4.11)
    assert repr(c) == "Sphere(4.11)"
    c = Sphere(84.11)
    assert repr(c) == "Sphere(84.11)"

def test_sphere_volume():
    s = Sphere(9)
    assert s.volume == 3053.6280592892786

def test_multiply_right_Sphere():
    s3=Sphere(4)
    s6= s3 * 2
    assert s6.radius == 8

def test_add_Spheres():
    s1=Sphere(1)
    s2=Sphere(2)
    s3=s1+s2
    assert s3.radius == 3

def test_sort_Sphere():
    s1=Sphere(4)
    s2=Sphere(3)
    s3=Sphere(2)
    s4=Sphere(1)
    group = [s4, s1, s3, s2]
    group.sort()
    assert group == [s4, s3, s2, s1]

def test_Sphere_from_diameter():
    s=Sphere.from_diameter(5)
    assert s.diameter == 5