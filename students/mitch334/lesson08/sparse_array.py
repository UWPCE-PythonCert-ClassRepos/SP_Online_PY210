
class SparseArray():
    def __init__(self, array):
        self.len = len(array)
        self.sparse = {index: item for index, item in enumerate(array) if item}
        self.array = array

    def __len__(self):
        return self.array_length

    def __delitem__(self, index):
        try:
            del self.sparse[index]
        except KeyError:
            print('Unable to delete index', index)

    def __getitem__(self, index):
        if index >= 0 and index < self.len:
            return self.sparse.get(index, 0)
        elif index > self.len or index < 0:
            print('Index', index, 'not in Array.')
            return None

    def __setitem__(self, index, value):
        if value != 0:
            self.sparse[index] = value
        else:
            try:
                del self.sparse[index]
            except KeyError:
                print('Index', index, 'not in Array.')

    def append(self, value):
        if value != 0:
            self.sparse[self.len] = value
            self.len += 1


if __name__ == "__main__":
    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
