#!/usr/bin/env python3

from date_fashion import date_fashion

def test_1():
    assert date_fashion(5, 10) is 2


def test_2():
    assert date_fashion(5, 2) is 0


def test_3():
    assert date_fashion(5, 5) is 1


def test_4():
    assert date_fashion(3, 3) is 1


def test_5():
    assert date_fashion(10, 2) is 0


def test_6():
    assert date_fashion(2, 9) is 0


def test_7():
    assert date_fashion(9, 9) is 2


def test_8():
    assert date_fashion(10, 5) is 2


def test_9():
    assert date_fashion(2, 2) is 0


def test_10():
    assert date_fashion(3, 7) is 1


def test_11():
    assert date_fashion(2, 7) is 0


def test_12():
    assert date_fashion(6, 2) is 0
