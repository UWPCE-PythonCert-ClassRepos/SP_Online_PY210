#!/usr/bin/env python


def front_times(str, n):
    if len(str) < 3:
        return str*n
    else:
        front = str[0:3]
        return front*n

