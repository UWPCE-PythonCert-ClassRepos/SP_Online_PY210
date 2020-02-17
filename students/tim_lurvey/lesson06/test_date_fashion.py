
from date_fashion import date_fashion

def test_01():
    assert date_fashion(5, 10) == 2


def test_02():
    assert date_fashion(5, 2) == 0


def test_03():
    assert date_fashion(5, 5) == 1