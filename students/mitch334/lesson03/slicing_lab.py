"""Lesson 03 | Slicing Lab"""
# Goal: Get the basics of sequence slicing down.
#
# Tasks: Write some functions that take a sequence as an argument, and return a copy of that sequence:
# * with the first and last items exchanged.
# * with every other item removed.
# * with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# * with the elements reversed (just with slicing).
# * with the last third, then first third, then the middle third in the new order.
# NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

def exchange_first_last(seq):
    """return sequence with the first and last items exchanged."""
    if len(seq) < 2:
        return seq
    else:
        # print(seq,' | ', seq[-1:] + seq[1:-1] + seq[:1])
        return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    """return sequence with every other item removed."""
    # print(seq,' | ', seq[::2])
    return seq[::2]

def every_other_mid(seq):
    """return sequence with the first 4 and the last 4 items removed, and then every other item in the remaining sequence."""
    # print(seq,' | ', seq[4:-4:2])
    return seq[4:-4:2]

def elements_reversed(seq):
    """return sequence with the elements reversed (just with slicing)."""
    # print(seq,' | ', seq[::-1])
    return seq[::-1]

def thirds(seq):
    """return sequence with the last third, then first third, then the middle third in the new order."""
    one_third = len(seq)//3
    # print(seq,' | ', seq[-one_third:] + seq[:one_third] + seq[one_third:-one_third])
    return seq[-one_third:] + seq[:one_third] + seq[one_third:-one_third]


a_string = "this is a string"
a_tuple = (2,54,13,12,5,32)
a_list = [0,2,4,6,8,10]
a_small_string = 'Matthew'
a_small_tuple = ('4',2,99)
a_4_tuple = ('4',2,99,55)
a_tiny_string = 'M'
a_tiny_list = [22]
a_tiny_tuple = (10,)
a_empty_string  = ''


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32,54,13,12,5,2)
assert exchange_first_last(a_list) == [10,2,4,6,8,0]
assert exchange_first_last(a_small_string) == 'wattheM'
assert exchange_first_last(a_small_tuple) == (99,2,'4')
assert exchange_first_last(a_tiny_string) == 'M'
assert exchange_first_last(a_tiny_list) == [22]
assert exchange_first_last(a_tiny_tuple) == (10,)
assert exchange_first_last(a_empty_string) == ''

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2,13,5)
assert remove_every_other(a_list) == [0,4,8]
assert remove_every_other(a_small_string) == 'Mthw'
assert remove_every_other(a_small_tuple) == ('4',99)
assert remove_every_other(a_tiny_string) == 'M'
assert remove_every_other(a_tiny_list) == [22]
assert remove_every_other(a_tiny_tuple) == (10,)
assert remove_every_other(a_empty_string) == ''

assert every_other_mid(a_string) == " sas"
assert every_other_mid(a_tuple) == ()
assert every_other_mid(a_list) == []
assert every_other_mid(a_small_string) == ''
assert every_other_mid(a_small_tuple) == ()
assert every_other_mid(a_tiny_string) == ''
assert every_other_mid(a_tiny_list) == []
assert every_other_mid(a_tiny_tuple) == ()
assert every_other_mid(a_empty_string) == ''

assert elements_reversed(a_string) == "gnirts a si siht"
assert elements_reversed(a_tuple) == (32,5,12,13,54,2)
assert elements_reversed(a_list) == [10,8,6,4,2,0]
assert elements_reversed(a_small_string) == 'wehttaM'
assert elements_reversed(a_small_tuple) == (99,2,'4')
assert elements_reversed(a_tiny_string) == 'M'
assert elements_reversed(a_tiny_list) == [22]
assert elements_reversed(a_tiny_tuple) == (10,)
assert elements_reversed(a_empty_string) == ''

assert thirds(a_string) == "tringthis is a s"
assert thirds(a_tuple) == (5,32,2,54,13,12)
assert thirds(a_list) == [8,10,0,2,4,6]
assert thirds(a_small_string) == 'ewMatth'
assert thirds(a_small_tuple) == (99,'4',2)
assert thirds(a_4_tuple) == (55,'4',2,99)
assert thirds(a_tiny_string) == 'M'
assert thirds(a_tiny_list) == [22]
assert elements_reversed(a_tiny_tuple) == (10,)
assert thirds(a_empty_string) == ''
