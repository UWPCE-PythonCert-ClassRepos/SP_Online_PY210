#!/usr/bin/env python3

import operator

class SparseArray2D(object):
    """
    2D sparse array
    """

    def __init__(self, sequence):
        self.items = list(sequence)
        self.sparse_array = dict(enumerate([[item for item in sublist if item != 0] for sublist in self.items]))

    def __len__(self):
        return sum([len(item) for item in self.items])

    def __getitem__(self, key):
        if isinstance(key, slice):
            print(f"It's a single slice:{key}")
        elif isinstance(key, tuple):
            print(f"It's a multi-dimensional slice:{key}")
        else:
            try:
                index = operator.index(key)
                print(f"It's an index:{index}")
            except TypeError:
                raise
            print("It's a simple index")

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

    def __reversed__(self):
        pass

    def __contains__(self, item):
        if isinstance(item, list):
            return item in self.items
        elif isinstance(item, int):
            return any(item in sublist for sublist in self.items)
        else:
            try:



    def __index__(self):
        pass

    def __str__(self):
        f_string = "[{}]".format(", ".join(["{:3}"] * len(self.items[0])))
        return "[{}]".format("\n ".join([f_string.format(*row) for row in self.items]))

    def __repr__(self):
        return f"SparseArray2D({self.items})"

    def append(self, item):
        pass


if __name__ == "__main__":
    sa2d = SparseArray2D([[1, 0, 0, 0, 0, 0, 1, 0, 2],
                          [4, 5, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 6, 7, 8, 9]])
    print(sa2d)
    print(sa2d.__repr__())
    sa2d.append([0, 0, 0, 0, 0, 0, 0, 0, 7])
    print(sa2d.__contains__([1, 0, 0, 0, 0, 0, 1, 0, 2]))
    print(sa2d.__contains__(6))
