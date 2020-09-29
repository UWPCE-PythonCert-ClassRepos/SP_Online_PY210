#!/usr/bin/python
# -*- coding: utf-8 -*-


def make_bricks(small, big, goal):
    big_length = big * 5
    small_length = small * 1

    if big_length >= goal:
        num_big = int(goal/5)
        num_small = goal % 5
        if num_small <= small:
            return True 
        else:
            return False
    elif big_length <= goal:
        if big_length + small_length < goal:
            return False
        else:
            return True
    else:
        return True