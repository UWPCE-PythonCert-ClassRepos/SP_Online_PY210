# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:10:29 2020
##fib and luc
@author: johnh
"""
import numpy
n=20

def fibby(n):
    nachii = [1,1]
    ##nextElement = nachii[-1]+nachii[-2]
    for i in range(n):
        nextElement = nachii[-1]+nachii[-2]
        nachii.insert(len(nachii),nextElement)
    print (*nachii)
fibby(n)

def lucy(n):
    nachii = [2,1]
    ##nextElement = nachii[-1]+nachii[-2]
    for i in range(n):
        nextElement = nachii[-1]+nachii[-2]
        nachii.insert(len(nachii),nextElement)
    print (*nachii)
lucy(n)

def diffy(n):
    nachii = [1,1]
    nachi2 = [2,1]
    diff = ['']*n
    for i in range(n):
        nextElement = nachii[-1]+nachii[-2]
        nextElement2 = nachi2[-1]+nachi2[-2]    
        nachii.insert(len(nachii),nextElement)
        nachi2.insert(len(nachi2),nextElement2)
        diff[i] = nachi2[i]-nachii[i]
    print(*diff)
diffy(n)