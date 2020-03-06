#!/usr/bin/env python

import pytest
from circles import *

radii = {1., 2., 3.5, 99., 1000.}

@pytest.fixture
def my_circle():
    return Circle(2.)

def test_init():
    c = Circle()

def test_init2():
    c = Circle(2)
