#!/usr/bin/env python3

# Test suite for SparseArray

import pytest

from sparse_array import *

def test_init():
    # Test that initializer works
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])

def test_len():
    # Test that length returns correct value
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    assert len(test_array) == 10

def test_get_value():
    # Test that getter works
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    # Make sure both non-zero and zero values return properly
    assert test_array[1] == 2
    assert test_array[3] == 0
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        test_array[10]

def test_set_value():
    # Test that setter works
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    test_array[1] = 9
    assert test_array[1] == 9
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        test_array[10] = 7

def test_append():
    # Test that append works
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    test_array.append(7)
    # Length should increase by one
    assert len(test_array) == 11
    assert test_array[10] == 7

def test_append_zero():
    # Test that append zero has no effect
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    test_array.append(0)
    assert len(test_array) == 10

def test_delete():
    # Test that del works
    test_array = SparseArray([1,2,0,0,0,0,3,0,0,4])
    del test_array[6]
    del test_array[2]
    assert test_array[6] == 0
    assert test_array[2] == 0
    # Make sure exception is raised if access is beyond end of array
    with pytest.raises(IndexError):
        del test_array[10]

# The remaining tests make sure various slicing operations work
def test_slice():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[1:6]
    assert slice == [2,0,7,0,5]

def test_slice_step():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[0:4:2]
    assert slice == [1,0]

def test_slice_over():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[6:20]
    assert slice == [3,0,0,4]

def test_slice_nonsense():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[50:60]
    assert slice == []

def test_slice_negative():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[3:0:-1]
    assert slice == [7,0,2]

def test_slice_negative_step():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    slice = test_array[5:0:-2]
    assert slice == [5,7,2]

def test_step_zero():
    test_array = SparseArray([1,2,0,7,0,5,3,0,0,4])
    # Make sure slice step of zero raises error
    with pytest.raises(ValueError):
        test_array[1:5:0]
