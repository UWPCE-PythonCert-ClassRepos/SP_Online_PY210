#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the circle class
class Circle(object):
    """This is the circle class"""

    def __init__(self, radius):
        """
        Require parameters: Radius
        """
        self.radius = radius
        self.diameter = radius*2