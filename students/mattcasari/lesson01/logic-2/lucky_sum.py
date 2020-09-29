#!/usr/bin/python
# -*- coding: utf-8 -*-

def lucky_sum(a, b, c):
    nums = [a, b, c]
    sum = 0
    for num in nums:
        if num == 13:
            return sum
        else:
            sum += num

    return sum