#!/usr/bin/python
# -*- coding: utf-8 -*-

def combo_string(a, b):
    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b