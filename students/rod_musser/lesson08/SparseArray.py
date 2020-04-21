#!/usr/bin/env python3


class SparseArray(object):

    def __init__(self, sequence):
        self.values_map = {}
        self.length = len(sequence)
        for i, item in enumerate(sequence):
            if item != 0:
                self.values_map[i] = item

    def __str__(self):
        return str(self.inflate_sequence())

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if (key > self.length - 1):
            raise IndexError("Index out of bounds.")
        return self.values_map.get(key, 0)

    def __setitem__(self, key, value):
        if (key > self.length - 1):
            raise IndexError("Index out of bounds.")
        self.values_map[key] = value

    # object.__delitem__(self, key)
    # object.__iter__(self)
    # object.__reversed__(self)
    # object.__contains__(self, item)

    # object.__index__(self)

    def inflate_sequence(self):
        sequence = []
        for i in range(self.length):
            sequence.append(self.values_map.get(i, 0))
        return sequence


