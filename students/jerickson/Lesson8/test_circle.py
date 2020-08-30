"""Test code for circle.py"""

import pytest  # pylint: disable=unused-import

import circle


########
# Step 1
########


def test_init():
    """
    This only tests that it can be initialized
    """
    circle.Circle(42)  # pylint: disable=unused-variable
