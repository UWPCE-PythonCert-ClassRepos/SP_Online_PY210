#!/usr/bin/python
# -*- coding: utf-8 -*-

def make_chocolate(small, big, goal):
    total = small + big*5
    if goal <= total:
        num_big = int(goal/5)
        if num_big <= big:
            num_small = goal - num_big*5
        else:
            num_small = goal - big*5
        print(num_small)
        if num_small <= small:
            return num_small


    return -1