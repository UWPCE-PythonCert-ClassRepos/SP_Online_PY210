import pytest

from sparse_array import *

sample_list = [0,1,0,0,2,0,0,0,3,0]
sample_dict = {1: 1, 4: 2, 8: 3}

def test_init():
    arr = SparseArray(sample_list)
    assert arr.content == sample_dict
    assert arr.length == 10

def test_len():
    arr = SparseArray(sample_list)
    assert len(arr) == 10
    
def test_get():
    arr = SparseArray(sample_list)
    with pytest.raises(IndexError):
        item = arr[11]
    assert arr[3] == 0
    assert arr[8] == 3
    assert arr.content == sample_dict
    assert len(arr) == 10
 
def test_set():
    arr = SparseArray(sample_list)
    arr[3] = 8
    assert arr.content == {1: 1, 4: 2, 8: 3, 3: 8}
    assert len(arr) == 10
    
    arr[11] = 0
    assert arr.content == {1: 1, 4: 2, 8: 3, 3: 8}
    assert len(arr) == 12
    
    arr[4] = 0
    assert arr.content == {1: 1, 8: 3, 3: 8}
    assert len(arr) == 12

def test_del():
    arr = SparseArray(sample_list)
    del arr[4]
    assert len(arr) == 9
    assert arr.content == {1:1, 7:3}
    
    del arr[4]
    assert len(arr) == 8
    assert arr.content == {1:1, 6:3}

def test_splice():
    arr = SparseArray(sample_list)
    assert arr[1:3] == [1, 0]
    
    arr[2:7:2] = [2,1,0]
    assert arr.content == {1:1, 4:1, 8:3, 2:2}
    
    del arr[::3]
    assert arr.content == {0:1, 2:1, 5:3, 1:2}
    assert len(arr) == 6
    
    del arr[2:6]
    assert arr.content == {0:1, 1:2}
    assert len(arr) == 2
  
