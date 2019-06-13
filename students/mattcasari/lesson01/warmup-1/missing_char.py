#!/usr/bin/python
# -*- coding: ascii -*-

def missing_char(str, n):
    if n <= len(str) + 1:
        str = str[0:n] + str[n+1:]
    return str