#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_events(nums):
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
    return even_count