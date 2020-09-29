from big_diff import big_diff

def test_1():
    assert big_diff([10, 3, 5, 6]) == 7


def test_2():
    assert big_diff([7, 2, 10, 9]) == 8


def test_3():
    assert big_diff([2, 10, 7, 2]) == 8