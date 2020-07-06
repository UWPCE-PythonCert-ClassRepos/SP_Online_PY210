'''
Write some functions that take a sequence as an argument,
    and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other
     item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
'''


def first_last(seq):
    seq2 = seq[:]
    return seq2[-1:] + seq2[1:-1] + seq2[:1]


def every_other(seq):
    seq2 = seq[:]
    return seq2[::2]


def first_four_last_four(seq):
    seq2 = seq[:]
    return seq2[4:-4:2]


def reverse(seq):
    seq2 = seq[::-1]
    return seq2


def reorder(seq):
    seq2 = seq[:]
    length = len(seq2)
    third = round(length / 3)
    return seq2[-third:] + seq2[:third] + seq2[third:-third]


'Tests'

s = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
s2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

assert first_last(s) == (10, 2, 3, 4, 5, 6, 7, 8, 9, 1)
assert every_other(s) == (1, 3, 5, 7, 9)
assert first_four_last_four(s2) == (5, 7, 9, 11, 13, 15)
assert reverse(s) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
assert reorder(s) == (8, 9, 10, 1, 2, 3, 4, 5, 6, 7)
