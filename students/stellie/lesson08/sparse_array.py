#!/usr/bin/env python3

# Stella Kim
# Sparse Array Exercise


class SparseArray(object):
    def __init__(self, arr):
        print('Array:', arr)
        self.list = arr
        self.length = len(self.list)
        # Store only non-zero values
        self.dict = {index: value for index, value in
                     enumerate(self.list) if value}
        print('Dictionary:', self.dict)

    def __len__(self):
        return self.length

    def append(self, value):
        self.list.append(value)
        if value:
            self.dict.update({len(self.list) - 1: value})
        print('Array length:', len(self.list))
        print('Value:', value)
        print('Array:', self.list)
        print('Dictionary:', self.dict)

    def __getitem__(self, index):
        if index >= 0 and index < len(self.list):
            return self.list[index]
        elif index < 0 or index >= len(self.list):
            print('Index does not exist.')
            raise IndexError

    def __setitem__(self, index, value):
        if value:
            self.list[index] = value
            self.dict[index] = value
            print('Array:', self.list)
            print('Dictionary:', self.dict)
        else:
            print('Index does not exist.')

    def __delitem__(self, index):
        del self.list[index]
        print('Array:', self.list)
        print('Dictionary:', self.dict)


if __name__ == "__main__":
    sa = SparseArray([1, 2, 0, 0, 0, 0, 3, 0, 0, 4])
