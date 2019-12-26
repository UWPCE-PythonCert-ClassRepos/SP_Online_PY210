#!/usr/bin/env python

print("""Warmup2 array_front9(arg).
Given an array of ints, return True if one of the first 4 elements in the array
 is a 9. The array length may be less than 4.""")

def array_front9(array):
    param=4
    if len(array)>=param:
        n=param
    else:
        n=len(array)
    for i in range(n):
        if array[i]==9:
            status=True
            break
        else:
            status=False
    return status