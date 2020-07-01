# test_circle.py
# opcode6502: SP_Online_PY210

from circle import *

def test_circle():
    c = Circle(4)
    assert c.radius == 4