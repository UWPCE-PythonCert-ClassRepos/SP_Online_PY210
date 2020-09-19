#!/usr/bin/env python3

"""
Lesson 9: Mail Room Part Object Oriented (Donor models)
Course: UW PY210
Author: Jason Jenkins
"""

# Define a multiple inheritance scheme:
class Donor(object):

    def __init__(self, full_name, donation_amount):
        self.full_name = full_name
        self.total_given = 0
        self.num_gifts = 0

        self.give(donation_amount)

    @property
    def average(self):
        if self.num_gifts < 1:
            return 0
        else:
            return self.total_given / self.num_gifts

    def give(self, val):
        if(val > 0):
            self.total_given += val
            self.num_gifts += 1


# Define a multiple inheritance scheme:
class DonorCollection(list):
    pass



