#!/usr/bin/env python3

# Test suite for SparseArray

import pytest

from sparse_array import *

def test_init():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])

def test_len():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    assert len(test_array) == 10

def test_get_value():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    # Make sure both non-zero and zero values return properly
    assert test_array[1] == 2
    assert test_array[3] == 0
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        test_array[10]

def test_set_value():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    test_array[1] = 9
    assert test_array[1] == 9
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        test_array[10] = 7

def test_append():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    test_array.append(7)
    assert len(test_array) == 11
    assert test_array[10] == 7

def test_delete():
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    del test_array[6]
    del test_array[2]
    assert test_array[6] == 0
    assert test_array[2] == 0
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        del test_array[10]
