#!/usr/bin/env python
__author__ = 'Tim Lurvey'

import sys

def mySyntaxError():
    "syntax" += 9

def myAttributeError():
    ().add()

def myNameError():
    name.upper()

def myTypeError():
    5 + 'seven'

def main(args):
    # myAttributeError()
    # myNameError()
    # mySyntaxError()
    # myTypeError()

if __name__ == '__main__':
    main(sys.argv[1:])