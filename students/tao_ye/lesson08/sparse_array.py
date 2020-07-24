#!/usr/bin/env python3

import operator


class SparseArray():
    def __init__(self, list=None):
        self.size = 0
        self.dic = {}
        if list is not None:
            self.size = len(list)
            for i in range(self.size):
                if (list[i] != 0):
                    self.dic[i] = list[i]

    def __str__(self):
        return str(self.list_array())

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if isinstance(index, slice):
            pass
        elif isinstance(index, tuple):
            pass
        else:
            try:
                # this converts arbitrary objects to an int.
                ind = operator.index(index)
                if ind < self.size:
                    return self.dic.get(ind, 0)
                else:
                    raise IndexError("index out of bound")
            except TypeError:  # not a simple index
                raise

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            pass
        elif isinstance(index, tuple):
            pass
        else:
            try:
                # this converts arbitrary objects to an int.
                ind = operator.index(index)
                if ind < self.size:  # within the bound
                    if ind in self.dic:
                        if value == 0:
                            self.dic.pop(ind)
                        else:
                            self.dic[ind] = value
                    else:
                        if value != 0:
                            self.dic[ind] = value
                else:
                    raise IndexError("index out of bound")
            except TypeError:  # not a simple index
                raise

    def __delitem__(self, index):
        if isinstance(index, slice):
            pass
        elif isinstance(index, tuple):
            pass
        else:
            try:
                # this converts arbitrary objects to an int.
                ind = operator.index(index)
                if ind < self.size:
                    self.size -= 1
                    new_dic = {}
                    for key in self.dic:
                        if key == ind:
                            continue  # skip this index
                        elif key > ind:
                            new_dic[key-1] = self.dic[key]
                        else:
                            new_dic[key] = self.dic[key]
                    self.dic = new_dic
                else:
                    raise IndexError("index out of bound")
            except TypeError:  # not a simple index
                raise

    def list_array(self):
        list = []
        for i in range(self.size):
            if i in self.dic:
                list.append(self.dic[i])
            else:
                list.append(0)
        return list


if __name__ == "__main__":
    a = SparseArray([1, 0, 0, 0, 2, 0, 0, 0, 5])

    print(a[4], a[2])
    #print(a[10])
    print(f"len(array): {len(a)}")

    print(a)
    print(a.dic)

    a[5] = 12
    a[3] = 0

    print(a)
    print(a.dic)
    #val = a[13]

    a[4] = 0
    print(a)
    print(list(a.dic))

    del a[3]
    del a[6]
    print(a)
    print(f"len(array): {len(a)}")
    print(a.dic)
