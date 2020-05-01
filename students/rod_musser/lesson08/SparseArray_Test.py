import pytest
from SparseArray import SparseArray


def test_init():
    test_list = [1, 0, 2, 5, 7, 0, 0, 0, 0, 9]
    sa = SparseArray(test_list)
    print(sa)
    assert str(sa) == str(test_list)


def test_len():
    test_list_0 = [0, 0, 0, 0]
    sa = SparseArray(test_list_0)
    assert len(sa) == 4

    test_list_1 = [0, 3, 4, 5, 45, 999, 0]
    sa = SparseArray(test_list_1)
    assert len(sa) == 7


def test_get():
    test_list_1 = [0, 3, 4, 5, 45, 999, 0]
    sa = SparseArray(test_list_1)

    assert sa[0] == 0
    assert sa[1] == 3
    assert sa[4] == 45
    assert sa[6] == 0
    with pytest.raises(IndexError):
        sa[7]


def test_set():
    test_list_1 = [0, 3, 4, 5, 45, 999, 0]
    sa = SparseArray(test_list_1)

    sa[0] = 2
    assert sa[0] == 2

    sa[5] = 33
    assert sa[5] == 33

    with pytest.raises(IndexError):
        sa[7] = 100


def test_del():
    test_list_2 = [0, 3, 4, 5, 0, 0, 45, 999, 0]
    sa = SparseArray(test_list_2)
    assert str(sa) == str(test_list_2)

    del sa[2]
    assert len(sa) == 8
    assert str(sa) == str([0, 3, 5, 0, 0, 45, 999, 0])

    del sa[4]
    assert len(sa) == 7
    assert str(sa) == str([0, 3, 5, 0, 45, 999, 0])


def test_slice():
    test_list_slice = [0, 3, 4, 5, 0, 0, 45, 999, 0]
    sa = SparseArray(test_list_slice)
    assert sa[:] == [0, 3, 4, 5, 0, 0, 45, 999, 0]
    assert sa[4:7] == [0, 0, 45]
    assert sa[2:] == [4, 5, 0, 0, 45, 999, 0]
    assert sa[:5] == [0, 3, 4, 5, 0]
    assert sa[2:7:2] == [4, 0, 45]
    assert sa[-1] == 0
    assert sa[7] == 999
    assert sa[-3] == 45
    assert sa[2:-1] == [4, 5, 0, 0, 45, 999]
    assert sa[::-1] == [0, 999, 45, 0, 0, 5, 4, 3, 0]
    assert sa[2:-1:-1] == [999, 45, 0, 0, 5, 4]


def test_iter():
    test_iter_list = [0, 3, 4, 45, 999, 0]
    sa = SparseArray(test_iter_list)
    sa_iter = iter(sa)
    assert next(sa_iter) == 0
    assert next(sa_iter) == 3
    assert next(sa_iter) == 4
    assert next(sa_iter) == 45
    assert next(sa_iter) == 999
    assert next(sa_iter) == 0
    with pytest.raises(StopIteration):
        next(sa_iter)


def test_reversed():
    test_reserved_list = [0, 3, 4, 45, 999, 0]
    sa = SparseArray(test_reserved_list)
    assert list(reversed(sa)) == [0, 999, 45, 4, 3, 0]


def test_contains():
    test_contains = [0, 3, 4, 45, 999, 0]
    sa = SparseArray(test_contains)
    assert 3 in sa
    assert 0 in sa
    assert (99 in sa) is False








