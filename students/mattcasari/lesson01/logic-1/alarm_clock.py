#!/usr/bin/python
# -*- coding: utf-8 -*-

def alarm_clock(day, vacation):
    if vacation:
        if  0 < day < 6:
            return '10:00'
        else:
            return 'off'
    else:
        if 0 < day < 6:
            return '7:00'
        else:
            return '10:00'