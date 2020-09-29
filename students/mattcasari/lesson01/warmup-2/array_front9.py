#!/usr/bin/python
# -*- coding: ascii -*-

def array_front9(nums):
    if nums[:4].count(9) > 0:
        return True
    else:
        return False