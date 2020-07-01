# test_circle.py
# opcode6502: SP_Online_PY210

from circle import *

def debug_print_attributes(c):
    print("c.raidus:   " + str(c.radius))
    print("c.diameter: " + str(c.diameter))
    print("c.area:     " + str(c.area))

def test_circle_radius():
    c = Circle(4)
    debug_print_attributes(c)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    debug_print_attributes(c)
    assert c.diameter == 8

def test_set_circle_diameter():
    c = Circle(4)
    c.diameter = 2
    debug_print_attributes(c)
    assert c.radius == 1
    assert c.diameter == 2

def test_circle_area():
    c = Circle(2)
    debug_print_attributes(c)
    assert c.area == 12.566370614359172

    c = Circle(5)
    debug_print_attributes(c)
    assert c.area == 78.53981633974483
