#!/usr/bin/python
# -*- coding: utf-8 -*-

def sum67(nums):
    flag = False
    val = 0
    for num in nums:
        if num == 6:
            flag = True
        else:
            if flag == False:
                val += num
            else:
                if num == 7:
                    flag = False
    return val