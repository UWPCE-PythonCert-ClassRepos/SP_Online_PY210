#!/usr/bin/env python3

"""PY210_SP - exercise 3.1 - slicing_lab
author: Nick Miller"""


def fflip(seq):
    """returns a copy of seq with the first and last items exchanged"""
    i = len(seq)
    ffliped = seq[i - 1:] + seq[1:i - 1] + seq[:1]
    return ffliped


def eo(seq):
    """returns a copy of seq with every other item removed"""
    eor = seq[::2]
    return eor


def four_eo_four(seq):
    """returns a copy of seq with first and last 4 items removed, as well as every other after"""
    i = len(seq)
    chop_eo = seq[4:i-4:2]
    return chop_eo


def missy_el(seq):
    """returns a copy of seq with the elements reversed"""
    workit = seq[::-1]
    return workit


tester = "yo imma a string"
tester2 = (4, 8, 15, 16, 23, 42)

assert fflip(tester) == "go imma a striny"
assert fflip(tester2) == (42, 8, 15, 16, 23, 4)
assert eo(tester) == "y maasrn"
assert eo(tester2) == (4, 15, 23)
assert four_eo_four(tester) == "maas"
assert four_eo_four(tester2) == ()
assert missy_el(tester) == "gnirts a ammi oy"
assert missy_el(tester2) == (42, 23, 16, 15, 8, 4)

print("You good.")
