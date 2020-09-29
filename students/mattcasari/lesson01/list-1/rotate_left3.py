#!/usr/bin/python
# -*- coding: utf-8 -*-

def rotate_left3(nums):
    temp = nums.pop(0)
    nums.insert(3,temp)
    return nums 