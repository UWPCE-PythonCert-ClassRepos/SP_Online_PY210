#!/usr/bin/env python3

from mailroom4 import *
import os
import pytest

"""
test code for mailroom4

Adapted from the "coding bat" site: https://codingbat.com/python

Return True if the party with the given values is successful,
or False otherwise.
"""

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }

def test_donor_db ():
    assert list_donors() == ['William Gates, III','Jeff Bezos','Paul Allen','Mark Zuckerberg']

