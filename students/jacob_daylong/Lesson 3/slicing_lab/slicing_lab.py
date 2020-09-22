# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:11:31 2020

@author: jaked
"""

"""
with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
"""
import math


txt = "This is a string"
txt2 = "This is a string that has way more letters than the first, but hopefully still works as intended."
numbers = [1, 2, 3, 4, 5, 10, 11, 99, 43, 78, 1002]
print()
print("Unmodified")
print(txt)
print(numbers)
print(txt2)
print()

def exchange_first_last(seq):
    """Exchange first and last element"""
    seq = seq[-1:] + seq[1:-1] + seq[:1]
    return seq

print()
print("Exchange first and last, numbers")
print(exchange_first_last(txt))
print(exchange_first_last(numbers))
print(exchange_first_last(txt2))
print()

def every_other(seq):
    """Remove every other element"""
    seq = seq[::2]
    return seq

print()
print("Remove every other")
print(every_other(txt))
print(every_other(numbers))
print(every_other(txt2))
print()

def first_four_last_four(seq):
    """Remove first four and last four and every other of the remaining elements"""
    seq = seq[4:-4:2]
    return seq

print()
print("Remove first four and last four, and every other remaining element")
print(first_four_last_four(txt))
print(first_four_last_four(numbers))
print(first_four_last_four(txt2))

print()

def reversal(seq):
    """Reverse elements"""
    seq = seq[::-1]
    return seq

print()
print("Reverse")
print(reversal(txt))
print(reversal(numbers))
print(reversal(txt2))
print()

def thirds(seq):
    """Rearrange thirds of the element"""
    third = math.floor(len(seq)/3)
    seq = seq[third:third*2] + seq[third*2:] + seq[0:third]
    return seq

print()
print("Thirds Exchanged")
print(thirds(txt))
print(thirds(numbers))
print(thirds(txt2))
print()