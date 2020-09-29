class SparseArray:
    def __init__(self):
        self._sequ = None
    @property
    def sequ(self):
        return self._sequ
    @sequ.setter    
    def sequ(self,value):
        self._sequ = value
    
    # x = object[i] supports getitem
    def __getitem__(self,index):
        return self._sequ[index]

    # object[i] = something supports setitem
    def __setitem__(self,index,value):
        self._sequ[index] = value

    def __delitem__(self,index):
        try:
            del self._sequ[index]
        except IndexError:
            raise
    
    def append(self,value):
        self._sequ.append(value)

test1 = SparseArray()
test1.sequ = [1,2,3,4,5,8]
test1[3] = 12
##del test1[]
test1.append(6)