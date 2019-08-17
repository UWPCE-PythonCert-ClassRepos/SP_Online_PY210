#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 5, Lab 1

"""


def safe_input():
    try:
        return_value = input("Enter>")
    except(EOFError, KeyboardInterrupt):
        return_value = None

    return return_value

if __name__ == "__main__":
    print(safe_input())