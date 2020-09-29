#!/usr/bin/python
# -*- coding: utf-8 -*-

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    
    if 80 < speed:
        return 2
    elif 61 <= speed:
        return 1
    else:
        return 0
