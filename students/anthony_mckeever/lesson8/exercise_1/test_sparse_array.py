"""
Programming In Python - Lesson 8 Exercise 1: Sparse Array
Code Poet: Anthony McKeever
Start Date: 09/04/2019
End Date: 09/04/2019
"""

from sparse_array import SparseArray


test_list = [1, 2, 3, 0, 0, 6, 0, 8, 9]


def test_initial_storage():
    sp = SparseArray(test_list)
    assert 0 not in sp.storage.values()
    assert len(sp) == len(test_list)
    
    for i in range(len(test_list)):
        assert test_list[i] == sp[i]


def test_set_item():
    sp = SparseArray(test_list)
    assert test_list[3] == sp[3]
    
    sp[3] = 9
    assert test_list[3] != sp[3]
    assert sp[3] == 9
    
    sp[2] = 9
    assert test_list[2] != sp[2]
    assert sp[2] == 9

    sp[0] = 0
    assert sp[0] == 0
    assert 0 not in sp.storage.values()
    

def test_slice():
    sp = SparseArray(test_list)
    assert sp[1::2] == test_list[1::2]
    assert sp[::-1] == test_list[::-1]
    assert sp[::] == test_list[::]
    assert sp[0:3] == test_list[0:3]
    assert sp[6:0:-2] == test_list[6:0:-2]


def test_append():
    sp = SparseArray(test_list)
    sp.append(20)
    assert sp[len(sp) - 1] == 20

    sp.append(0)
    assert sp[len(sp) - 1] == 0

    assert 0 not in sp.storage.values()


def test_exceptions():
    sp = SparseArray(test_list)

    try:
        sp[300]
    except IndexError as ie:
        assert str(ie) == "SparseArray index out of range."

    try:
        sp[900] = 2353
    except IndexError as ie:
        assert str(ie) == "SparseArray index out of range."        
    
    try:
        sp[-80] = 2
    except IndexError as ie:
        assert str(ie) == "SparseArray index out of range."        

    try:
        sp["Cresenta"]
    except TypeError as te:
        assert str(te) == "SparseArray indicies must be integers or slices, not str"
