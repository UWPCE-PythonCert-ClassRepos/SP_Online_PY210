"""
test code for SparseArray.py

"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from SparseArray import *


def test_init():
    sa = SparseArray()

    assert sa.l == []

    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
    assert sa.l == [1,2,0,0,0,0,3,0,0,4]

    sa = SparseArray((1,0,0,0,2,0,0,0,5))
    assert sa.l == [1,0,0,0,2,0,0,0,5]


def test_len():
    sa = SparseArray()
    assert len(sa) == 0
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
    assert len(sa) == 4


def test_getitem():
    sa = SparseArray((1,0,0,0,2,0,0,0,5))
    assert sa[0] == 1
    assert sa[1] == 0
    assert sa[4] == 2


def test_setitem():
    sa = SparseArray((1,0,0,0,2,0,0,0,5))
    sa[0] = 2
    sa[4] = 0
    assert sa[0] == 2
    assert sa[4] == 2


def test_append():
    sa = SparseArray((1,0,5))
    sa.append(10)
    assert sa[3] == 10


def test_del():
    sa = SparseArray((1,0,5))
    del sa[2]
    assert sa[0] == 1
    with pytest.raises(IndexError):
        sa[2] == 5
