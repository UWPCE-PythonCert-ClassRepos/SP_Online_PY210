#!/usr/bin/env python3
import sys
##############################################################
# 20200603    djm grid printer function exercise part 2
#
# Duane McCollum Python self-paced winter 2020
#
# Grid Printer Exercise part 2
# prints a variable sized grid by specified rows and columns
# use two functions, one to make a row of + -'s
# and another to make | |'s
# then use those two functions in a print_grid function
##############################################################

def print_row(n):
    #print a row of +/-
    plus = '+'
    minus = '-'
    row = ''
    # if n < 3 default to 3
    if n < 3: n = 3

    i = 1  # loop counter, number of +'s
    dash = n//2
    for k in range(3):
        row = row + plus
        i = i + 1
        if i <= 3:
            for y in range(dash):
                row = row + minus
    return row

def print_vRow(n):
    vLine = '|'
    vRow = ''
    if n < 3: n = 3

    i = 1
    dash = n//2
    for j in range(3):
        vRow = vRow + vLine
        i = i + 1
        if i <= 3:
            for y in range(dash):
                vRow = vRow + ' '
    return vRow

def print_grid(n):
    box = ''

    if n < 3: n = 3

    c = 1
    dash = n//2
    for i in range(3):
        box = box + print_row(n) + '\n'
        c = c + 1
        if c <=3:
            for j in range(dash):
                box = box + print_vRow(n) + '\n'
    return box

print(print_grid(-2))
print(print_grid(3))
print(print_grid(15))

