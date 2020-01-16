#!/usr/bin/env python


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
