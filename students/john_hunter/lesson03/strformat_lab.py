# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:49:47 2020

@author: johnh
"""

#string formatting lab

def str_format_one(myLst):
    #for item in myLst:
    listToReturn = list()
    #alsoList = list() 
    if myLst[0]<=9:
        fileStr = ('file_00{}'.format(str(myLst[0])))
    elif myLst[0]<=99:
        fileStr = ('file_0{}'.format(str(myLst[0])))
    else:
        fileStr = ('file_{}'.format(str(myLst[0])))
    scientific_notation0 = "{:.2g}".format(myLst[1])
    scientific_notation = "{:e}".format(myLst[2])
    scientific_notation1 = "{:2e}".format(myLst[3])
    listToReturn.append(fileStr) 
    listToReturn.append(scientific_notation0) 
    listToReturn.append(scientific_notation) 
    listToReturn.append(scientific_notation1) 
    return listToReturn

stuff = [[1, 245345345, 334534535564, 893429849], [2, 276543, 38765, 2394874], [3, 25432, 387654444,2498274], [4, 276543, 3765433,229847], [5, 276543, 3765432,2349874]]

for item in stuff:
    print(str_format_one(item))