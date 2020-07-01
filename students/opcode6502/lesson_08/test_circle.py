# test_circle.py
# opcode6502: SP_Online_PY210


from circle import *


def debug_print_attributes(c):
    print("c.raidus:   " + str(c.radius))
    print("c.diameter: " + str(c.diameter))
    print("c.area:     " + str(c.area))


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
    c = Circle(2)
    try:
        c.area = 5
        #
        # If this succeeds, assert False.
        debug_print_attributes(c)
        assert False
    except AttributeError:
        #
        # Since we have an AttributeError, assert True.
        assert True
    except Exception as e:
        #
        # Anything else, print the debug attributes and assert False.
        debug_print_attributes(c)
        print(e)
        assert False
