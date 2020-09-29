#!/usr/bin/python
# -*- coding: utf-8 -*-

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    a_len = len(a)
    b_len = len(b)
    
    if a_len < b_len:
        if b[-a_len:] == a:
            return True
    else:
        if a[-b_len:] == b:
            return True
    return False