#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_code(str):
    result = 0
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            result += 1
    return result