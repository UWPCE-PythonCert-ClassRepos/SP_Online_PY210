#!/usr/bin/env python3


class SparseArray(object):

    def __init__(self, sequence):
        self.iter_current = 0
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
        if isinstance(key, slice):
            return self.get_slice(key)
        else:
            if (key < 0):
                key = self.length + key
            if (key > self.length - 1):
                raise IndexError("Index out of bounds.")
            return self.values_map.get(key, 0)

    def __setitem__(self, key, value):
        if (key > self.length - 1):
            raise IndexError("Index out of bounds.")
        self.values_map[key] = value

    def __delitem__(self, key):
        if (key > self.length - 1):
            raise IndexError("Index out of bounds.")
        try:
            del self.values_map[key]
        except KeyError:
            pass
        finally:
            self.remove_item(key)
            self.length = self.length - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_current >= self.length:
            raise StopIteration
        else:
            self.iter_current += 1
            return self.__getitem__(self.iter_current - 1)


    # object.__reversed__(self)
    # object.__contains__(self, item)

    # object.__index__(self)

    def get_slice(self, key):
        print('Slice Start: ' + str(key.start))
        print('Slice End: ' + str(key.stop))
        print('Slice Step: ' + str(key.step))
        array_slice = []

        start = key.start or 0
        stop = key.stop or self.length
        step = key.step or 1
        if (stop < 0):
            stop = self.length + stop

        if step < 0:
            tmp_stop = stop
            stop = start - 1
            start = tmp_stop - 1

        for i in range(start, stop, step):
            array_slice.append(self.values_map.get(i, 0))
        return array_slice

    def inflate_sequence(self):
        sequence = []
        for i in range(self.length):
            sequence.append(self.values_map.get(i, 0))
        return sequence

    def remove_item(self, key):
        for i in range(self.length):
            if i > key:
                print('Trying ' + str(i))
                try:
                    val = self.values_map[i]
                    del self.values_map[i]
                    self.values_map[i - 1] = val
                except KeyError:
                    pass
