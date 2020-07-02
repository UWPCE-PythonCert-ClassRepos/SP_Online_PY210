# test_circle.py
# opcode6502: SP_Online_PY210


from circle import *


def debug_print_attributes(c):
    print('c:          ' + str(c))
    print('c.raidus:   ' + str(c.radius))
    print('c.diameter: ' + str(c.diameter))
    print('c.area:     ' + str(c.area))


def test_circle_radius():
    #
    # Test setup.
    c = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c)
    #
    # Assertion.
    assert c.radius == 4


def test_circle_diameter():
    #
    # Test setup.
    c = Circle(4)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c)
    #
    # Assertion.
    assert c.diameter == 8


def test_set_circle_diameter():
    #
    # Test setup.
    c = Circle(4)
    c.diameter = 2
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c)
    #
    # Assertion.
    assert c.radius == 1
    assert c.diameter == 2


def test_circle_area():
    #
    # Test setup.
    c = Circle(2)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c)
    #
    # Assertion.
    assert c.area == 12.566370614359172
    #
    # Test setup.
    c = Circle(5)
    #
    # Print debug statements (in case of failure).
    debug_print_attributes(c)
    #
    # Assertion.
    assert c.area == 78.53981633974483


def test_circle_area_setter():
    #
    # Test setup.
    c = Circle(2)
    #
    #
    try:
        #
        # Test setup.
        c.area = 5
        #
        # If this succeeds, assert False.
        debug_print_attributes(c)
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
        debug_print_attributes(c)
        print(e)
        #
        # Assertion.
        assert False


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

def test_circle_compare_gt():
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
    # #
    # # Test setup.
    # c1 < c2
    # #
    # # Print debug statements (in case of failure).
    # debug_print_attributes(c1)
    # debug_print_attributes(c2)
    # #
    # # Assertion.
    # assert True
    # #
    # # Test setup.
    # c1 == c2
    # #
    # # Print debug statements (in case of failure).
    # debug_print_attributes(c1)
    # debug_print_attributes(c2)
    # #
    # # Assertion.
    # assert False
    # #
    # # Test setup.
    # c3 = Circle(4)
    # c2 == c3
    # #
    # # Print debug statements (in case of failure).
    # debug_print_attributes(c1)
    # debug_print_attributes(c2)
    # #
    # # Assertion.
    # assert True
