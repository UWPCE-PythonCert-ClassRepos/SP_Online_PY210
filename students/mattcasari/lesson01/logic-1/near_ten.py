#!/usr/bin/python
# -*- coding: utf-8 -*-

def near_ten(num):
    if (num % 10) <= 2 or abs(10 - (num % 10)) <= 2:
        return True 
    else:
        return False