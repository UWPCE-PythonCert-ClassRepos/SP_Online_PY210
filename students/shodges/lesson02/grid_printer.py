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

#part 3
# ed. note -- there was a change between part 2 and 3 in how the grid was calculated. In parts 1 and 2, the "columns" were = spaces + minuses
# in part 3, columns = only minuses.  I'm not sure if that's the spirit of this but I stuck with the change in counting methodology as the examples
# given reflected that change.  Sorry if wrong here!
def print_grid3(n, s):
    horizontal_border = (('+ ' + ('- ' * s)) * n) + '+'
    vertical_border = (('|' + (' ' * ((2*s)+1))) * n) + '|'

    for h in range(0,n):
        print(horizontal_border)
        for v in range(0,s):
            print(vertical_border)
    print(horizontal_border)
