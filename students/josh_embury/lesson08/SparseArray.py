#!/usr/bin/env python3

class SparseArray(object):
    def __init__(self, seq):
        #self.dict_arr = {seq.index(i):i for i in seq}
        self.dict_arr = {}
        for i in range(0,len(seq)):
            self.dict_arr[i] = seq[i]
    def __len__(self):
        return len(self.dict_arr.keys())

    def __index__(self, value):
        return

    def __getitem__(self, index):
        if index not in self.dict_arr:
            return 0
        else:
            return self.dict_arr[index]

    def __setitem__(self, index, value):
        self.dict_arr[index] = value

    def __delitem__(self, index):
        try:
            del self.dict_arr[index]
        except KeyError:
            print('IndexError: No item in this index to delete!!')

    def append(self, value):
        a = max(self.dict_arr.keys())
        self.dict_arr[a + 1] = value

    def pop(self, value=-1):
        if value == -1:
            a = max(self.dict_arr.keys())
            del self.dict_arr[a]
        else:
            del self.dict_arr[value]

if __name__ == "__main__":
# some tests on the sparsearray for TDD:
    # test init:
    sa1 = SparseArray([0,5,0,4,0,0])
    # test append and len:
    sa1.append(8)
    print(len(sa1))
    assert len(sa1) == 7
    # test get:
    assert sa1[3] == 4
    test_var = sa1[54]
    assert test_var == 0
    # test set:
    sa1[12] = 8
    assert sa1[12] == 8
    print(sa1.dict_arr.keys())
    del sa1[40]
    # test pop:
    print(sa1[-1])
    print('length is: ' + str(len(sa1)))
    sa1.pop()
    print(sa1[-1])
    print('after popping length is now: ' + str(len(sa1)))
    sa1.pop(0)