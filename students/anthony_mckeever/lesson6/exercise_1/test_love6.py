"""
Programming In Python - Lesson 6 Exercise 1: Unit Tests
Code Poet: Anthony McKeever
Start Date: 08/19/2019
End Date: 08/19/2019
"""

from love6 import love6

def test_a_6():
    assert love6(6, -2) is True

def test_b_6():
    assert love6(-3, 6) is True

def test_sum_a_b():
    assert love6(1, 5) is True
    assert love6(2, 4) is True
    assert love6(3, 3) is True
    assert love6(4, 2) is True
    assert love6(5, 1) is True

    assert love6(8, -2) is True
    assert love6(-2, 8) is True

def test_subtract_a_b():
    assert love6(7, 1) is True
    assert love6(8, 2) is True
    assert love6(9, 3) is True
    assert love6(10, 4) is True
    assert love6(11, 5) is True
    assert love6(12, 6) is True

def test_subtract_b_a():
    assert love6(1, 7) is True
    assert love6(2, 8) is True
    assert love6(3, 9) is True
    assert love6(4, 10) is True
    assert love6(5, 11) is True
    assert love6(6, 12) is True

def test_never_6():
    assert love6(345, 2) is False
    assert love6(345, 1000) is False
    assert love6(-36, 29) is False
    assert love6(800, 800) is False
    assert love6(0, 0) is False
