#!/usr/bin/env python3


import functools
import os

@functools.total_ordering
class Donor(object):

    def __init__(self, name, amount=0, number=0):
        self.name = name
        self.donation = amount
        self.number = number

    def __str__(self):
        return "Donor: {}".format(self.name)

#   def __repr__(self):
#      return "Donor("+self.name+")"

    def __eq__(self, other):
        return self.donation == other.donation

    def __lt__(self, other):
        return self.donation < other.donation

    def donation(self, amount):
        self.donation += amount
        self.number(1)

    def number(self, number):
        self.number += number

    @property
    def average(self):
        return float("{:.2f}".format(self.donation / self.number))

    @property
    def write_letter(self):
        letter = """
        Dear {},
        Thank you for your collective contributions of ${:.2f} over the years.
        Your generous donations have been put to good use!
        Sincerely,
        Kyle at Kelby Doggo, Inc\n""".format(self.name, self.donation)
        return letter

    @property
    def send_letter(self):
        text = self.write_letter
        name_list = (self.name.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(text)



