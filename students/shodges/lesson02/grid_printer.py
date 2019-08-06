#!/usr/bin/env python3

import math

#part 1
def print_grid1():
    horizontal_border = (('+ ' + ('- ' * 4)) * 2) + '+'
    vertical_border = (('|' + (' ' * 9)) * 2) + '|'

    for h in range(0,2):
        print(horizontal_border)
        for v in range(0,4):
            print(vertical_border)
    print(horizontal_border)

#part 2
def print_grid2(n):
    if n % 2 == 1: extra_space = ' '
    else: extra_space = ''
    horizontal_border = (('+' + extra_space + ('- ' * math.floor(n/2))) * 2) + '+'
    vertical_border = (('|' + (' ' * n)) * 2) + '|'

    for h in range(0,2):
        print(horizontal_border)
        for v in range(0,math.floor(n/2)):
            print(vertical_border)
    print(horizontal_border)
