#!/usr/bin/env python3

"""
A class-based system for a SparseArray
"""

class SparseArray(object):

    def __init__(self, tmp_list = None):
        if tmp_list == None:
            self.tmp_list = []
        else:
            self.tmp_list = tmp_list
