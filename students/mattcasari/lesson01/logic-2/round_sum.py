#!/usr/bin/python
# -*- coding: utf-8 -*-

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if 5 <= (num % 10):
        return num + 10 - (num % 10)
    else:
        return num - (num % 10)

