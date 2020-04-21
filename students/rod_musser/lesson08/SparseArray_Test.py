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


