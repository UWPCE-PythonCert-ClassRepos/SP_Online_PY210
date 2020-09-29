#!/usr/bin/python
# -*- coding: utf-8 -*-

def lone_sum(a, b, c):
    temp = [a, b, c]
    final_list = []
    for num in temp:
        if temp.count(num) == 1:
            final_list.append(num)
    
    return sum(final_list)