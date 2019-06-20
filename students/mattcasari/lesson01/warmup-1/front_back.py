#!/usr/bin/python
# -*- coding: ascii -*-

def front_back(str1):
    if len(str1) > 1:
        str1 = str1[-1] +  str1[1:-1] + str1[0]

    return str1