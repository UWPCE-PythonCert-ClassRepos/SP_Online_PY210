#!/usr/bin/env python

"""
String without its ends.
Given a string, return a version without the first and last char,
so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""


def without_end(in_str):
    if not isinstance(in_str, str):
        raise TypeError('Input value must be of type str.')
    if len(in_str) == 2:
        return ''
    return in_str[1:-1]
