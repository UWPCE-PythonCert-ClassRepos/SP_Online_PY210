# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:36:21 2019

@author: Kevin
"""
def print_grid2(num_box, size_box):
    #This section concatenates the symbols to create the first line of the box
    #It considers the number of boxes and size of each box (how many dashes)
    line1 = '+'
    line1 = line1 + num_box*(size_box* ' -' + ' +')

    #This section concatenates the symbols to create the second line of the box
    #It considers the number of spaces between vertical lines, and the number of vertical lines
    line2 = '|'
    line2 = line2 + num_box*(size_box* '  ' + ' |')

    #This prints the first line
    print (line1)

    #This for loop adds on the remaining 3 sides of each box, looped for the number of boxes
    for i in range(num_box):
        #This loop prints the vertical lines for each box, as a function of box size
        for j in range(size_box):
            print (line2)
        #This prints the bottom of the box.
        print (line1)
