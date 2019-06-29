#!/usr/bin/python
# -*- coding: utf-8 -*-

def in1to10(n, outside_mode):
    if outside_mode and ( n <= 1 or 10 <= n):
        return True
    elif not outside_mode and 1 <= n <= 10:
        return True 
    else:
        return False