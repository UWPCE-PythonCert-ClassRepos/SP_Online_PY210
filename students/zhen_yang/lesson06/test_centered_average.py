"""
test code for the centered_average.py

centerted_average.py returns the "centered" average of an array of ints,
which we'll say is the mean average of the values, except ignoring the largest
and smallest values in the array. If there are multiple copies of the smallest
value, ignore just one copy, and likewise for the largest value. Use int
int division to produce the final average. You may assume that the array is
length 3 or more.

"""

from centered_average import centered_average


def test_regular():
    list = [1, 2, 3, 4, 100]
    assert centered_average(list) == 3

def test_repeated_smallest():
    list = [1, 1, 5, 5, 10, 8, 7]
    assert centered_average(list) == 5

def test_repeated_largest():
    list = [1, 5, 5, 10, 10, 8, 7]
    assert centered_average(list) == 7

def test_repeated_smallest_largest():
    list = [1, 1, 5, 5, 10, 10, 10, 8, 7]
    assert centered_average(list) == 6

def test_negative():
    list = [-10, -4, -2, -4, -2, 0]
    assert centered_average(list) == -3
