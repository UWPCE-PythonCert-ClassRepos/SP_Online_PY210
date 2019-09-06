import numpy as np

def name_err():
    print(hi)
    
def type_err():
    print(4+'5')

def syntax_err(x=9):
    if x>9:
        print(x+4)
    els:
        print(x-2)
        
# Attributes are functionalities of a particular object        
def att_err():
    aList = [4,5,6]
    print(aList.sum())