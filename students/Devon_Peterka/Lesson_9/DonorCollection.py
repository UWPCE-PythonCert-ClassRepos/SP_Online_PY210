#!/usr/bin/env python 3

from Donor import Donor

class DonorCollection():
    def __init__(self):
        self.donor_list = []

    def add_donor(self, *input):
        if type(input) is not Donor:
            raise SyntaxError('Input must be a Donor object.')
        self.donor_list.append(input)
