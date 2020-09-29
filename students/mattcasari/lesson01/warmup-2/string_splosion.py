#!/usr/bin/python
# -*- coding: ascii -*-

def string_splosion(str):
    if len(str) > 0:
        temp = ''
        for i in range(0,len(str)+1):
            temp += str[0:i]
    return temp
