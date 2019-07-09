#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_hi(str):
    cnt = 0
    for i in range(len(str)):
        if str[i:].find('hi') == 0:
            cnt += 1
    return cnt