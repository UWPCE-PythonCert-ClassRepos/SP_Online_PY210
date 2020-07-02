# test_circle.py
# opcode6502: SP_Online_PY210


from circle import *


# Helper method.
def debug_print_attributes(c):
    print('c:          ' + str(c))
    print('c.raidus:   ' + str(c.radius))
    print('c.diameter: ' + str(c.diameter))
    print('c.area:     ' + str(c.area))


def test_circle_add():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(4)
    result = c1 + c2
    #
    # Print debug statements (in case of failure).
    print(str(result))
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert result == Circle(6)


def test_circle_area():
    #
    # Test setup.
    c1 = Circle(2)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.area == 12.566370614359172
    #
    # Test setup.
    c1 = Circle(5)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.area == 78.53981633974483


def test_circle_area_setter():
    #
    # Test setup.
    c1 = Circle(2)
    #
    #
    try:
        #
        # Test setup.
        c1.area = 5
        #
        # If this succeeds, assert False.
        debug_print_attributes(c1)
        #
        # Assertion.
        assert False
    except AttributeError:
        #
        # Since we have an AttributeError, assert True.
        #
        # Assertion.
        assert True
    except Exception as e:
        #
        # Anything else, print the debug attributes and assert False.
        debug_print_attributes(c1)
        print(e)
        #
        # Assertion.
        assert False


def test_circle_diameter():
    #
    # Test setup.
    c1 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.diameter == 8


def test_circle_diameter_setter():
    #
    # Test setup.
    c1 = Circle(4)
    c1.diameter = 2
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.radius == 1
    assert c1.diameter == 2


def test_circle_eq_01():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(2)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c1 == c2) is True


def test_circle_eq_02():
    #
    # Test setup.
    c1 = Circle(4)
    c2 = Circle(1)
    c2 = c1
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c1 == c2) is True


def test_from_diameter():
    #
    # Test setup.
    c1 = Circle.from_diameter(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.diameter == 4
    assert c1.radius == 2


def test_circle_ge():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c2 >= c1) is True


def test_circle_gt():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c2 > c1) is True


def test_circle_le():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c1 <= c2) is True


def test_circle_lt():
    #
    # Test setup.
    c1 = Circle(2)
    c2 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    debug_print_attributes(c2)
    #
    # Assertion.
    assert (c1 < c2) is True


def test_circle_mul():
    #
    # Test setup.
    c1 = Circle(5)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert repr(c1 * 5) == repr(Circle(25))


def test_circle_radius():
    #
    # Test setup.
    c1 = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c1)
    #
    # Assertion.
    assert c1.radius == 4


def test_circle_str():
    #
    # Assertion.
    assert str(Circle(100)) == "Circle: Radius: 100"


def test_circle_sort_key():
    #
    # Test setup.
    circles = [Circle(5), Circle(1), Circle(4), Circle(3), Circle(2)]
    circles.sort(key=Circle.sort_key)
    #
    # Print debug statements (in case of failure).
    print(circles)
    #
    # Assertion.
    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5)]



def test_sphere_diameter():
    #
    # Test setup.
    s1 = Sphere(2)
    s2 = Sphere(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(s1)
    debug_print_attributes(s2)
    #
    # Assertion.
    assert s1.diameter == 4
    assert s2.diameter == 8


def test_sphere_radius():
    #
    # Test setup.
    s1 = Sphere(2)
    s2 = Sphere(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(s1)
    debug_print_attributes(s2)
    #
    # Assertion.
    assert s1.radius == 2
    assert s2.radius == 4
