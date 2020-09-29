#!/usr/bin/python
# -*- coding: utf-8 -*-

def xyz_there(str):
    for i in range(len(str)):
        if str[i:].find('xyz') == 0:
            if i == 0 or str[i-1] != '.':
                return True
    return False