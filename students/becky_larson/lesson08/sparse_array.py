#!/usr/bin/env python3

class SparseArray:

    def __init__(self, array=None):
        self.array = array
        self.dict = {}
        self.length = len(array)
        
        for i in range(0, len(self.array) ):
            if self.array[i] !=0:
                self.dict[i] = self.array[i]

        print(f'init self.dict is:  {self.dict}')

    # getter
    def __get_item__(self,index):
       try:
           return self.dict[index]
       except KeyError:
           if (index > (self.length -1)):
               raise IndexError
           else:
               return 0

    def __set_item__(self,index,value):
       if(value != 0):
           self.dict[index] = value
           print(f'set self.dict is:  {self.dict}')

    def __del_item__(self,index):
       try:
           del self.dict[index] 
           print(f'del self.dict is:  {self.dict}')
       except KeyError:
           print('encountered key error')

    def __append_item__(self,value):
       if(value != 0):
           self.dict[self.length+1] = value
       print(f'append self.dict is:  {self.dict}')


sa = SparseArray([1,2,0,0,0,0,3,0,0,4])
print(sa.__get_item__(6))
print(sa.__set_item__(22,0))
print(sa.__del_item__(41))
print(sa.__append_item__(21))



