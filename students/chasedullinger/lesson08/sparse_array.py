#!/usr/bin/env python

class SparseArray:

    def __init__(self, input_array):
        self._array = {}
        self._length = len(input_array)

        for position, item in enumerate(input_array):
            if item != 0:
                self._array[position] = item

    def append(self, array_to_append):
        for position, item in enumerate(array_to_append):
            if item != 0:
                self._array[position+self._length] = item
        self._length += len(array_to_append)

    def __len__(self):
        return self._length

    def __repr__(self):
        output_list = []
        for i in range(self._length):
            if i in self._array.keys():
                output_list.append(self._array[i])
            else:
                output_list.append(0)
        return "{}".format(output_list)

    def __getitem__(self, i):
        if i > self._length:
            raise IndexError
        if i in self._array.keys():
            return self._array[i]
        else:
            return 0

    def __setitem__(self, i, val):
        if i > self._length:
            self._length = i + 1
        if i in self._array.keys():
            if val == 0:
                del self._array[i]
            else:
                self._array[i] = val
        elif val != 0:
            self._array[i] = val

    def __delitem__(self, i):
        if i > self._length or i < 0:
            raise ValueError
        if i in self._array.keys():
            del self._array[i]
        for j in range(i, self._length):
            if j in self._array.keys():
                self._array[j-1] = self._array[j]
                del self._array[j]
        self._length -= 1
