#!/usr/bin/python
# -*- coding: ascii -*-

def last2(str):
    subs = str[-2:]
    cnt = 0
    for i in range(0, len(str)):
        if str[i:-1].find(subs) == 0:
            cnt += 1
    return cnt