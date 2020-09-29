#! /usr/bin/env python3

class SparseArray:
    def __init__(self, array):
        self.array = array
        self.d = dict([(i, self.array[i]) for i in range(len(self.array)) if self.array[i] != 0])

    def __repr__(self):
        return "Instance of SparseArray, with a  array = {}".format(self.array)

    @property
    def len(self):
        return len(self.array)

    def __getitem__(self, index):
        if index >= 0 and index < self.len:
            return self.d.get(index, 0)
        else:
            print ("Index {} is not valid index in {}".format(index, self.array))
            return None

    def __setitem__(self, index, value):
        if 0 <= index <= self.len and value != 0:
            self.d[index] = value
            self.array[index] = value
            return self.d

    def __delitem__(self, index):
        try:
            del self.array[index]
        except IndexError:
            print ("Index {} is not valid index in {}".format(index, self.array))

    def append (self, value):
        if value != 0:
            self.array.append(value)
            self.d[self.len] = value

if __name__ = "__main__":
    p = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])


