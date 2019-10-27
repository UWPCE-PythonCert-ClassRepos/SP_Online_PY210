from sparse_array import SparseArray

def test_construction():
    sa = SparseArray( (1,0,0,0,2,0,0,0,5) )

    assert len(sa) == 9
    assert sa[0] == 1
    assert sa[1] == 0
    assert sa[2] == 0
    assert sa[3] == 0
    assert sa[4] == 2
    assert sa[5] == 0
    assert sa[6] == 0
    assert sa[7] == 0
    assert sa[8] == 5

def test_set_item():
    sa = SparseArray( (1,0,0,0,2,0,0,0,5) )
    sa[1] = 2
    sa[4] = 0
    sa[7] = 10
    sa[8] = 6

    assert len(sa) == 9
    assert sa[0] == 1
    assert sa[1] == 2
    assert sa[2] == 0
    assert sa[3] == 0
    assert sa[4] == 0
    assert sa[5] == 0
    assert sa[6] == 0
    assert sa[7] == 10
    assert sa[8] == 6

def test_set_item_out_of_range():
    sa = SparseArray( (1,0,0,0,2,0,0,0,5) )

    try:
        sa[9] = 1
    except IndexError:
        pass
    else:
        assert False

    try:
        sa[10] = 0
    except IndexError:
        pass
    else:
        assert False


