# Sparse array exercise

class SparseArray(object):
    def __init__(self, full_array):
        self.length = len(full_array)
        self.sparse_dict = {}
        for i, item in enumerate(full_array):
            if not item == 0:
                self.sparse_dict[i] = item

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if key >= self.length:
            raise IndexError
        else:
            try:
                value = self.sparse_dict[key]
            except KeyError:  # if the value is 0 there should not be a key
                return 0
            else:
                return value

    def __setitem__(self, key, value):
        if key >= self.length:
            raise IndexError
        else:
            if value is not 0:
                self.sparse_dict[key] = value
            else:  # value is 0
                if key in self.sparse_dict.keys():
                    self.sparse_dict.pop(key)

    def append(self, value):
        if value == 0:
            pass
        else:
            self.sparse_dict[self.length] = value

        self.length += 1
        return value

    def __delitem__(self, key):
        if key >= self.length:
            raise IndexError
        else:
            if key in self.sparse_dict.keys():
                self.sparse_dict.pop(key)

    def __str__(self):
        values = [str(self.__getitem__(i)) for i in range(self.length)]
        
        return "{}{}{}".format("(", ", ".join(values), ")")

    """ Old implementaton
    def __str__(self):
        values = []
        for i in range(self.length):
            try:
                value = self.sparse_dict[i]
            except KeyError:
                values.append(str(0))
            else:
                values.append(str(value))
        
        return "{}{}{}".format("(", ", ".join(values), ")")
    """

        