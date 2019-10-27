#!/usr/bin/env python3
import argparse

#
# printHorizontal
#
# start the box printing on the first line
#
def printHorizontal(totalNumberOfBoxes,sizeOfEachBox):
    # one line total
    for i in range (totalNumberOfBoxes):
        print('+', end = ' ')
        for j in range (sizeOfEachBox):
            print('-', end = ' ')
    #end of line
    print('+')

#
# printVertical
#
# actually continue on the boxes started by printHorizontal
#
def printVertical(totalNumberOfBoxes,sizeOfEachBox):
    # vertically step down the size of each box
    for i in range (sizeOfEachBox):
        # now move vertical for the number of boxes to make
        for j in range (totalNumberOfBoxes):
            print('|', end = ' ')
            # vertically step over the size of each box
            for k in range(sizeOfEachBox):
                print(' ', end = ' ')
        # close final box and go to next
        print("|")

# parse incoming values
parser = argparse.ArgumentParser()
parser.add_argument('val', type=int, nargs=2)
args= parser.parse_args()
# two values, x&y integers
totalNumberOfBoxes, sizeOfEachBox = args.val[0], args.val[1]

for eachBox in range(totalNumberOfBoxes):
    # draw each box
    printHorizontal(totalNumberOfBoxes,sizeOfEachBox)
    printVertical(totalNumberOfBoxes,sizeOfEachBox)
#final line to close
printHorizontal(totalNumberOfBoxes,sizeOfEachBox)
