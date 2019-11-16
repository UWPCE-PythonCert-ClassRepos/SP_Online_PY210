#!/usr/bin/env python

"""
Slicing Lab.

All of the functions call functions which convert any sequence to a list, make a shallow \
copy, then (after processing in the parent function), return the modified list back to the \
original sequence type.
"""

import math


def first_last_exch(arg):  # 1st bullet
    list_arg, copy_list_arg = list_then_copy(arg)
    copy_list_arg[0] = list_arg[-1]
    copy_list_arg[-1] = list_arg[0]
    return back_to_orig(copy_list_arg, type(arg))


def every_other(arg):  # 2nd bullet
    list_arg, copy_list_arg = list_then_copy(arg)
    copy_list_arg = list_arg[::2]
    return back_to_orig(copy_list_arg, type(arg))


def first4_last4(arg):  # 3rd bullet
    list_arg, copy_list_arg = list_then_copy(arg)
    del list_arg[:4]
    del list_arg[-4:]
    copy_list_arg = list_arg[::2]
    return back_to_orig(copy_list_arg, type(arg))


def elements_reversed(arg):  # 4th bullet
    list_arg, copy_list_arg = list_then_copy(arg)
    copy_list_arg = list_arg[::-1]
    return back_to_orig(copy_list_arg, type(arg))


def new_thirds(arg):  # 5th bullet
    list_arg, copy_list_arg = list_then_copy(arg)
    n = len(list_arg)
    rem = len(list_arg) % 3
    if rem == 0:  # split into equal thirds for sequence lengths divisible by 3
        first = int(n / 3)
        last = int(n * 2 / 3)
    # first and last thirds are shorter than middle third for sequence lengths with
    # remainders of 2 after division by 3
    elif rem == 2:
        first = math.floor(n / 3) + 1
        last = math.floor(n * 2 / 3)
    elif rem == 1:
        first = math.floor(n / 3)
        last = math.floor(n * 2 / 3) + 1
    copy_list_arg = list_arg[last:] + list_arg[:first] + list_arg[first:last]
    return back_to_orig(copy_list_arg, type(arg))


def list_then_copy(Larg):  # convert any sequence to a list, and make a shallow copy
    Llist_arg = list(Larg)
    Lcopy_list_arg = Llist_arg[:]
    return Llist_arg, Lcopy_list_arg


def back_to_orig(Barg, _type_):  # convert the modified list back to the original sequence type
    if _type_ == str:
        return "".join(Barg)
    elif _type_ == list:
        return Barg
    elif _type_ == tuple:
        return tuple(Barg)


test_str = 'Yes this is a test'
test_lis = [1, 2.0, 3j, 'four', 1e-10, 'a', 6, 7, 'h', 8]
test_tup = (1, 2.0, 3j, 'four', 1e-10, 'a', 6, 7, 'h', 8)
test_tup9 = (1, 2.0, 3j, 'four', 1e-10, 'a', 6, 7, 'h')
test_str11 = '1234567890e'
assert first_last_exch(test_str) == 'tes this is a tesY'
assert every_other(test_lis) == [1, 3j, 1e-10, 6, 'h']
assert first4_last4(test_tup) == (1e-10,)
assert elements_reversed(test_str) == 'tset a si siht seY'
assert new_thirds(test_lis) == [7, 'h', 8, 1, 2.0, 3j, 'four', 1e-10, 'a', 6]
assert new_thirds(test_tup9) == (6, 7, 'h', 1, 2.0, 3j, 'four', 1e-10, 'a')
assert new_thirds(test_str11) == '890e1234567'
