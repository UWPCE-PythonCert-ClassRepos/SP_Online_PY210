#!/usr/bin/env python

"""
test code for String without its ends.

Adapted from the "coding bat" site: https://codingbat.com/python

Given a string, return a version without the first and last char,
so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""


# you can change this import to test different versions
from string_no_end import without_end
import pytest
# from walnut_party import walnut_party2 as walnut_party
# from walnut_party import walnut_party3 as walnut_party


def test_1():
    assert without_end('Hello') == 'ell'


def test_2():
    assert without_end('java') == 'av'


def test_3():
    assert without_end('coding') == 'odin'


def test_4():
    assert without_end('code') == 'od'


def test_5():
    assert without_end('ab') == ''


def test_6():
    assert without_end('Chocolate!') == 'hocolate'


def test_7():
    assert without_end('kitten') == 'itte'


def test_8():
    assert without_end('Chocolate!') == 'hocolate'


def test_9():
    assert without_end('woohoo') == 'ooho'


def test_10():
    with pytest.raises(Exception):
        without_end(100)


def test_11():
    with pytest.raises(Exception):
        without_end(120.2)