#!/usr/bin/env python3
import sys
##############################################################
# 20200603    djm grid printer function exercise part 3
#
# Duane McCollum Python self-paced winter 2020
#
# Grid Printer Exercise part
# prints a variable sized grid by specified rows and columns
# use two functions, one to make a row of + -'s
# and another to make | |'s
# then use those two functions in a print_grid function
##############################################################

def print_row2(column_size, cell_size):
    #print a row of +/-
    plus = '+'
    minus = '-'
    row = ''
    # if n < 3 default to 3
    if cell_size < 1: cell_size = 1
    if column_size < 1: column_size=1

    i = 1  # loop counter, number of +'s
    #dash = n//2
    for k in range(column_size+1):
        row = row + plus
        i = i + 1
        if i <= column_size+1:
            for y in range(cell_size):
                row = row + minus
    return row
#print (print_row2(1, 1))

def print_vRow2(col_size, cell_size):
    vLine = '|'
    vRow = ''
    if cell_size < 1: cell_size = 1
    if col_size < 1: col_size = 1

    i = 1
    for j in range(col_size + 1):
        vRow = vRow + vLine
        i = i + 1
        if i <= col_size + 1:
            for y in range(cell_size):
                vRow = vRow + ' '
    return vRow

#print(print_vRow2(1,1))


def print_grid2(grid_size, cell_size):
    box = ''

    if grid_size <= 1:  grid_size=2
    if cell_size <= 1:  cell_size = 1

    c = 1

    for i in range(grid_size+1):
        box = box + print_row2(grid_size, cell_size) + '\n'
        c = c + 1
        if c <=grid_size + 1:
            for j in range(cell_size):
                box = box + print_vRow2(grid_size, cell_size) + '\n'
    return box

print(print_grid2(1,1))

