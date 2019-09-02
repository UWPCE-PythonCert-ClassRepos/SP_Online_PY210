# -*- coding: utf-8 -*-
"""
Created: Mon Sep  2 07:58:20 2019
Author: Philip Behrend
Title: Grid Printer
"""

def print_horizontal(start = '+', border =' - ', box_width = 4, n_boxes = 2, end = '+'):
    print(n_boxes*(start + border*box_width) + end)

def print_vert(char = '|', box_height = 4, n_boxes = 2, white_space = 12):
    segment = (char + white_space*' ')*n_boxes + char
    vert_line = (segment +'\n')* (box_height-1) + segment
    print(vert_line)
    
def print_grid(width = 2, height = 3):
    for i in range(height):
        print_horizontal(n_boxes = width)
        print_vert(n_boxes = width)
    print_horizontal(n_boxes = width)

print_grid(5,5)
