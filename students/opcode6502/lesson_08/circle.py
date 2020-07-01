# circle.py
# opcode6502: SP_Online_PY210

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
