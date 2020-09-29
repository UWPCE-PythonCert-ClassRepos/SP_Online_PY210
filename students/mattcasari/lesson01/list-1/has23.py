#!/usr/bin/python
# -*- coding: utf-8 -*-

def has23(nums):
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False