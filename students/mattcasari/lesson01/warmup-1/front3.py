#!/usr/bin/python
# -*- coding: ascii -*-

def front3(str):
    if len(str) >= 3:
        str = str[0:3]*3
    else:
        str = str*3
    return str