#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

import copy
import sys
from functools import reduce


def _get_class_and_list(x: any) -> (object, list):
    """_get_class_and_list("abc") -> (type("abc"),copy("abc"))"""
    # get the object's class
    t = type(x)
    # get a mutable copy of the sequence
    c = copy.copy(x)
    return t, list(c)


def _cast_return(cls: any, x: any) -> any:
    """cast the variable x to a new type"""
    try:
        if cls == str:
            return "".join(x)
        else:
            return cls(x)
    except:
        raise TypeError("The variable x <{typ}> cannot be cast to {cls}".format(
            typ=type(x),
            cls=cls.__name__
            ))


def reversed(seq: any = ()):
    """elements reversed (just with slicing)."""
    return seq[::-1]


def rearrange(seq: any = (), pieces: int = 3):
    """ last piece, then first piece, then the middle pieces in the new order."""
    #
    # get class, list(lst)
    cls, cpy = _get_class_and_list(x=seq)
    #
    # get length, standard non-pythonic rounding
    n = int(round(len(seq) / pieces))
    #
    # assemble new sections
    # this lambda allows for slices that return values, not lists, to be added to other slices returning lists
    assemble = reduce(lambda a,b: a+b, [cpy[-n:]] + [cpy[:n]] + [cpy[n:-n]], [])
    #
    # return
    return _cast_return(cls=cls, x=assemble)


def remove_leading_trailing_every_other(seq: any = (), n: int = 4):
    """first n and the last n items removed, and then every other item in the remaining sequence"""
    #
    # get class, list(lst)
    cls, cpy = _get_class_and_list(x=seq)
    #
    return _cast_return(cls=cls, x=remove_every_other(seq=cpy[n:-n], offset=False))
    pass


def swap_first_last(seq: any = ()) -> any:
    """swap_first_last(lst) -> [lst[-1],lst[1]...lst[0]]
    Returns a sequence with the first and last items swapped"""
    #
    # get class, list(lst)
    cls, cpy = _get_class_and_list(x=seq)
    #
    # manipulate copy
    # make a list of each element as a list and then join the lists into one list
    # this lambda allows for slices that return values, not lists, to be added to other slices returning lists
    swap = reduce(lambda a,b: a+b, [[cpy[-1]], list(cpy[1:-1]), [cpy[0]]], [])
    #
    # return with class assignment
    return _cast_return(cls=cls, x=swap)


def remove_every_other(seq: any = (), offset: bool = False) -> any:
    """remove every other element
    seq = [1,2,3,4,5,6,7]
    offset=False -> [2,4,6] (default)
    offset=True  -> [1,3,5,7] """
    #
    # get class, list(lst)
    cls, cpy = _get_class_and_list(x=seq)
    #
    # manipulate
    if offset:
        remove = cpy[1::2]
    else:
        remove = cpy[::2]
    #
    # return with class assignment
    return _cast_return(cls=cls, x=remove)


def main(args:list=[], debug: bool = False):
    #
    # first and last items exchanged.
    #
    swap1 = (1, 2, 3, 4)
    if debug: print(swap1, swap_first_last(seq=swap1))
    assert swap_first_last(seq=swap1) == (4, 2, 3, 1)
    #
    swap2 = "a b c d "
    if debug: print(swap2, swap_first_last(seq=swap2))
    assert swap_first_last(seq=swap2) == "  b c da"
    #
    swap3 = [1, 'a', object]
    if debug: print(swap3, swap_first_last(seq=swap3))
    assert swap_first_last(seq=swap3) == [object, 'a', 1]
    #
    # every other item removed
    #
    remove1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    if debug: print(remove1, remove_every_other(seq=remove1))
    assert remove_every_other(seq=remove1) == (1, 3, 5, 7, 9)
    if debug: print(remove1, remove_every_other(seq=remove1, offset=True))
    assert remove_every_other(seq=remove1, offset=True) == (2, 4, 6, 8)
    #
    remove2 = "ababababababababab"
    if debug: print(remove2, remove_every_other(seq=remove2))
    assert remove_every_other(seq=remove2) == "aaaaaaaaa"
    if debug: print(remove2, remove_every_other(seq=remove2, offset=True))
    assert remove_every_other(seq=remove2, offset=True) == "bbbbbbbbb"
    #
    # the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    #
    remove3 = [1, 1, 1, 1, 2, 9, 3, 9, 4, 4, 4, 4]
    if debug: print(remove3, remove_leading_trailing_every_other(seq=remove3))
    assert remove_leading_trailing_every_other(seq=remove3) == [2, 3]
    #
    # elements reversed (just with slicing).
    #
    reverse = 'xyz'
    if debug: print(reverse, reversed(seq=reverse))
    assert reversed(seq=reverse) == "zyx"
    #
    # the last third, then first third, then the middle third in the new order.
    #
    thirds = (1, 1, 1, 3, 3, 3, 5, 5, 5)
    if debug: print(thirds, rearrange(seq=thirds, pieces=3))
    assert rearrange(seq=thirds, pieces=3) == (5, 5, 5, 1, 1, 1, 3, 3, 3,)
    pass


if __name__ == '__main__':
    main(sys.argv[1:], debug=True)
