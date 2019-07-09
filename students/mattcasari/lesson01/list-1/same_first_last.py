#!/usr/bin/python
# -*- coding: utf-8 -*-

def same_first_last(nums):
    if len(nums) > 0:
        return nums[0] == nums[-1]
    else:
        return False