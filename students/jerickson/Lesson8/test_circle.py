"""Test code for circle.py"""
# pylint: disable=wrong-import-order

import pytest  # pylint: disable=unused-import

import math
import circle


########
# Step 1
########


def test_init():
    """This only tests that it can be initialized"""
    circle.Circle(42)  # pylint: disable=unused-variable


########
# Step 2
########


def test_diam_get():
    """Tests that diameter can be get"""
    inst = circle.Circle(42)
    assert inst.diameter == 84


########
# Step 3
########


def test_diam_set():
    """Tests that diameter can be get"""
    inst = circle.Circle(42)
    inst.diameter = 42
    assert inst.radius == 21
    assert inst.diameter == 42


########
# Step 4
########


def test_area_get():
    """Tests that are can be get"""
    inst = circle.Circle(42)
    assert inst.area == math.pi * (inst.radius ** 2)


def test_area_set():
    """Tests that are can not be set"""
    inst = circle.Circle(42)
    with pytest.raises(AttributeError):
        inst.area = 42


########
# Step 5
########


def test_alt_construct_from_diameter():
    """Tests that a circle can be constructed from the diameter"""
    inst = circle.Circle.from_diameter(42)
    assert inst.radius == 21


########
# Step 6
########


def test_circle_str():
    """Tests the str(Circle) return value"""
    inst = circle.Circle(42)
    assert str(inst) == "Circle with radius: 42.00"


def test_circle_repr():
    """Tests the repr(Circle) return value"""
    inst = circle.Circle(42)
    assert repr(inst) == "Circle(42.00)"


########
# Step 7
########


def test_circle_add():
    """Tests that Circles add together by radius"""
    inst1 = circle.Circle(42)
    inst2 = circle.Circle(1)
    inst3 = inst1 + inst2
    assert repr(inst3) == "Circle(43.00)"


def test_circle_mul():
    """Tests that Circles multiply scalars by radius"""
    inst1 = circle.Circle(42)
    inst2 = inst1 * 2
    assert repr(inst2) == "Circle(84.00)"


def test_circle_rmul():
    """Tests that Circles multiply scalars by radius"""
    inst1 = circle.Circle(42)
    inst2 = 2 * inst1
    assert repr(inst2) == "Circle(84.00)"


########
# Step 8
########


def test_circle_lt():
    """Tests that Circles can compare using '<' operator"""
    inst1 = circle.Circle(1)
    inst2 = circle.Circle(42)
    assert inst1 < inst2
    assert inst1 <= inst2
    assert inst1 != inst2


def test_circle_gt():
    """Tests that Circles can compare using '>' operator"""
    inst1 = circle.Circle(42)
    inst2 = circle.Circle(1)
    assert inst1 > inst2
    assert inst1 >= inst2
    assert inst1 != inst2


def test_circle_eq():
    """Tests that Circles can compare using '==' operator"""
    inst1 = circle.Circle(42)
    inst2 = circle.Circle(42)
    assert inst1 == inst2
    assert inst1 <= inst2
    assert inst1 >= inst2


def test_circle_reflected_math():
    """Tests the reflected operators behavior"""
    inst1 = circle.Circle(42)
    inst2 = circle.Circle(1)
    assert inst1 + inst2 == inst2 + inst1
    assert inst1 * 42 == 42 * inst1


def test_circle_add_augmented():
    """Tests that Circles can add to itself"""
    inst1 = circle.Circle(42)
    inst2 = circle.Circle(1)
    inst1 += inst2
    assert repr(inst1) == "Circle(43.00)"


def test_circle_mul_augmented():
    """Tests that Circles can multiply a scalar to itself"""
    inst1 = circle.Circle(42)
    inst1 *= 2
    assert repr(inst1) == "Circle(84.00)"


def test_circle_div_augmented():
    """Tests that Circles can divide by a scalar to itself"""
    inst1 = circle.Circle(42)
    inst1 /= 2
    assert repr(inst1) == "Circle(21.00)"


########
# Step 9
########


def test_sphere_init():
    """Tests the Sphere init"""
    inst = circle.Sphere(42)
    assert inst.radius == 42


def test_sphere_str():
    """Tests the str(Circle) return value"""
    inst = circle.Sphere(42)
    assert str(inst) == "Sphere with radius: 42.00"


def test_sphere_repr():
    """Tests the repr(Circle) return value"""
    inst = circle.Sphere(42)
    assert repr(inst) == "Sphere(42.00)"


def test_sphere_vol_get():
    """Tests the sphere volume can be retrieved"""
    inst = circle.Sphere(42)
    assert inst.volume == (4 / 3) * math.pi * (inst.radius ** 3)


def test_sphere_vol_set():
    """Tests that volume can not be set"""
    inst = circle.Sphere(42)
    with pytest.raises(AttributeError):
        inst.volume = 42


def test_sphere_area_get():
    """Tests that area can not be retrieved"""
    inst = circle.Sphere(42)
    with pytest.raises(NotImplementedError):
        print(inst.area)


def test_sphere_surface_area_get():
    """Tests the sphere surface area can be retrieved"""
    inst = circle.Sphere(42)
    assert inst.surface_area == 4 * math.pi * (inst.radius ** 2)


def test_sphere_cross_area_get():
    """Tests that cross-sectional area can be retrieved"""
    inst = circle.Sphere(42)
    assert inst.cross_area == math.pi * (inst.radius ** 2)


def test_sphere_alt_construct_from_diameter():
    """Tests that a circle can be constructed from the diameter"""
    inst = circle.Sphere.from_diameter(42)
    assert inst.radius == 21
