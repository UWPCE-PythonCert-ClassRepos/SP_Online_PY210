#!/usr/bin/python
# -*- coding: utf-8 -*-

def date_fashion(you, date):
    if you <=2 or date <= 2:
        return 0
    elif 8 <= you or 8 <= date:
        return 2
    else:
        return 1