#!/usr/bin/python
# -*- coding: ascii -*-

def string_match(a, b):
    if len(a) < len(b):
        length = len(a)
    else:
        length = len(b)
    cnt = 0
    for i in range(0, length-1):
        if a[i:i+2] == b[i:i+2]:
            cnt += 1
    return cnt