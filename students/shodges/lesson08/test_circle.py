#!/usr/bin/env python3

import pytest
from circle import *

def test_create_circle():
    """
    Test creation of a circle and output of its radius.

    Expected output is 8
    """
    c = Circle(8)

    assert c.radius == 8
