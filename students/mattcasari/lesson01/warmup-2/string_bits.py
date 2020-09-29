#!/usr/bin/python
# -*- coding: ascii -*-

def string_bits(str):
    temp = ''
    count = 1
    for s in str:
        if count % 2 == 1:
            temp += s
        count += 1
    return temp