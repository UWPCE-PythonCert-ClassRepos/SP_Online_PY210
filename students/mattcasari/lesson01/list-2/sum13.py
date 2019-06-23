#!/usr/bin/python
# -*- coding: utf-8 -*-

def sum13(nums):
    flag = False
    val = 0
    for num in nums:
        if num == 13:
            flag = True
        else:
            if flag == True:
                flag = False
            else:
                val += num
    return val