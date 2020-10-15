# -*- coding: utf-8 -*-

txt = "This is a string"
txt2 = "This is a string that has way more letters than the first, but hopefully still works as intended."
numbers = [1, 2, 3, 4, 5, 10, 11, 99, 43, 78, 1002]
print()
print("Unmodified")
print(txt)
print(numbers)
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