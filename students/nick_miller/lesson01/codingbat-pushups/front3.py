#!/usr/bin/env python


def front3(str):
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front*3
