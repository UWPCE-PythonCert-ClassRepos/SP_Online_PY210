#!/usr/bin/python
# -*- coding: utf-8 -*-

def centered_average(nums):
    nums.sort()
    nums.pop(0)
    nums.pop(-1)
    return int(sum(nums)/len(nums))