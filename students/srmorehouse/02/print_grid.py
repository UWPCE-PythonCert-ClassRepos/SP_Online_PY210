#!/usr/bin/env python3
import argparse

def printHorizontal(x,y):
    # one line total
    for i in range (x):
        print('+', end = ' ')
        for j in range (y):
            print('-', end = ' ')
    #end of line
    print('+')

def printVertical(x,y):
    # y lines total
    for i in range (y):
        # number of boxes to make
        for j in range (x):
            print('|', end = ' ')
            # size of each box
            for k in range(y):
                print(' ', end = ' ')
        # close box
        print("|")

# parse incoming values
parser = argparse.ArgumentParser()
parser.add_argument('val', type=int, nargs=2)
args= parser.parse_args()
# two values, x&y integers
x, y = args.val[0], args.val[1]

# x is number of boxes
# y is length of each box

for i in range(x):
    printHorizontal(x,y)
    printVertical(x,y)
#final line to close
printHorizontal(x,y)
