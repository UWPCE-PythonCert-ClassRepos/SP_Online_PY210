# test_circle.py
# opcode6502: SP_Online_PY210

from circle import *

def test_circle_radius():
    c = Circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_set_circle_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.radius == 1