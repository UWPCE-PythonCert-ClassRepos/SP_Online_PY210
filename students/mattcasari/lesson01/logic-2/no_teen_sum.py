#!/usr/bin/python
# -*- coding: utf-8 -*-

def no_teen_sum(a, b, c):
    def fix_teen(n):
        if 13 <= n < 15 or 16 < n <= 19:
            return 0
        else:
            return n
    

    return fix_teen(a) + fix_teen(b) + fix_teen(c)