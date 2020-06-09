class SparseArray():
    def __init__(self,array):
        self.array = array
        self.length = len(array)
        self.sparse = {}
        for index, value in enumerate(array):
            if value !=0:
                self.sparse[index] = value

    def __delitem__(self,index):
        try:
            self.sparse.pop(index)
        except KeyError:
            if index > self.length:
                print(index, 'is out of bounds')

    def __getitem__(self,index):
        try:
            return self.sparse[index]
        except KeyError:
            if index > self.length:
                print(index, 'is out of bounds')
            else:
                return 0

    def __setitem__(self,index,value):
        if value != 0:
            self.sparse[index] = value


sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
